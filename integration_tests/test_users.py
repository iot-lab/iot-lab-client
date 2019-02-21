# This file is a part of IoT-LAB client
# Copyright (C) 2019 INRIA (Contact: admin@iot-lab.info)
# Contributor(s) : see AUTHORS file
#
# This software is governed by the CeCILL license under French law
# and abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# http://www.cecill.info.
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

"""
[**signup_user**](UsersApi.md#signup_user)
[**activate_user**](UsersApi.md#activate_user)
[**get_user**](UsersApi.md#get_user)
[**get_user_ssh_keys**](UsersApi.md#get_user_ssh_keys)
[**modify_user**](UsersApi.md#modify_user)


[**delete_user**](UsersApi.md#delete_user)
[**delete_user_ssh_keys**](UsersApi.md#delete_user_ssh_keys)
[**reset_password**](UsersApi.md#reset_password)
[**set_user_ssh_keys**](UsersApi.md#set_user_ssh_keys)
[**update_password**](UsersApi.md#update_password)
"""
import os
import re
import uuid

import pytest
import six
from pytest import fail

from integration_tests import API, HOST
from integration_tests.mail import wait_email
from iotlabclient.api import Api
from iotlabclient.client import UserRequest, Configuration, ActivateUserRequest

api = API.users

# configuration for "Test User" user

TESTUSER_LOGIN = os.environ.get('TESTUSER-LOGIN')
TESTUSER_PASSWORD = os.environ.get('TESTUSER-PASSWORD')

configuration = Configuration()
configuration.username = TESTUSER_LOGIN
configuration.password = TESTUSER_PASSWORD
configuration.host = HOST
api = Api(configuration=configuration).users


def get_ssh_keys():
    return [open(os.path.expanduser('~/.ssh/id_rsa.pub'), 'r').read()]


@pytest.mark.skipif(not pytest.config.option.signup,
                    reason="needs --signup option to run")
def test_create_activate_user(uid=None):
    ACTIVATE = re.compile(r'http://.*/activate\?hash=([0-9a-f]{64})')
    PASSWORD = re.compile(r'.*password\s:\s([^ ]*)')
    LOGIN = re.compile(r'.*login:\s([^ ]*)')
    DEAR = 'Dear %s %s,'

    if uid is None:
        uid = uuid.uuid4().hex
        create_new = True
    else:
        create_new = False

    user = UserRequest(
        first_name='test%s' % uid[:6],
        last_name='user%s' % uid[6:12],
        email='matthieu.berthome+%s@gmail.com' % uid,
        country='Westeros',
        city='King\'s Landing',
        organization='INRIA',
        motivations='I ♥ FIT IoT-LAB',
        category='Startup',
        sshkeys=get_ssh_keys(),
    )

    # signup as unauthenticated
    configuration = Configuration()
    configuration.host = HOST
    api = Api(configuration=configuration).users

    if create_new:
        api.signup_user(user_request=user)

    def match_email(msg, subject, first_name, last_name):
        if msg.get('Subject') == subject:
            payload = msg.get_payload().splitlines()

            dear = DEAR % (first_name.capitalize(), last_name.capitalize())
            for line in payload:
                if line.strip() == dear.strip():
                    return True
        return False

    def activate_user(msg):
        payload = msg.get_payload().splitlines()

        for line in payload:
            matched = ACTIVATE.match(line)
            if matched:
                request = ActivateUserRequest(hash=matched.group(1))
                api.activate_user(activate_user_request=request)
                return True
        fail('The validation through email failed')

    def find_match(msg, regex):
        payload = msg.get_payload().splitlines()

        for line in payload:
            matched = regex.match(line)
            if matched:
                return regex.match(line).group(1)
        fail('regex %s failed in the email' % regex)

    def do_activate_user(msg):
        if match_email(msg, 'FIT IoT-LAB account email validation',
                       user.first_name, user.last_name):
            if activate_user(msg):
                return True
            fail('the activation link in the email failed')

    def do_get_password(msg):
        if match_email(msg, 'FIT IoT-LAB account activation',
                       user.first_name, user.last_name):
            configuration.login = find_match(msg, LOGIN)
            configuration.password = find_match(msg, PASSWORD)
            return True

    # click on the activate link
    wait_email(do_activate_user)

    # get the generated login / password
    wait_email(do_get_password)

    api = Api(configuration=configuration).users

    created_user = api.get_user()

    assert created_user.status == 'active'


def test_get_user():
    user = api.get_user()

    assert user.to_dict() == dict(
        category='Startup', city="King's Landing",
        country='Westeros',
        created='2019-02-21T10:53:15Z',
        email='matthieu.berthome@gmail.com',
        first_name='Test',
        groups=[],
        last_name='User',
        login='userbfe',
        motivations='I ♥ FIT IoT-LAB',
        organization='INRIA',
        sshkeys=get_ssh_keys(),
        status='active'
    )


def test_get_user_ssh_keys():
    keys = api.get_user_ssh_keys()

    assert keys.sshkeys == get_ssh_keys()


def test_roundtrip_modify_user():
    data = {k: v for k, v in six.iteritems(api.get_user().to_dict())
            if k not in ['created', 'login', 'status']}
    user_request = UserRequest(**data)
    user_request.motivations = 'motivations'

    api.modify_user(user_request=user_request)
    modified = api.get_user()

    assert modified.motivations == 'motivations'

    user_request = UserRequest(**data)
    api.modify_user(user_request=user_request)
    modified_back = api.get_user()

    assert modified_back.motivations == 'I ♥ FIT IoT-LAB'
