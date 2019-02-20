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
import uuid

import pytest

from integration_tests import API
from iotlabclient.client import Profile, ProfileConsumption, ProfileRadio
from iotlabclient.client.rest import ApiException

api = API.monitoring
"""
[**delete_profile**](MonitoringApi.md#delete_profile)
[**get_profile**](MonitoringApi.md#get_profile)
[**get_profiles**](MonitoringApi.md#get_profiles)
[**modify_profile**](MonitoringApi.md#modify_profile)
[**save_profile**](MonitoringApi.md#save_profile)
"""


@pytest.fixture
def saved_profile():
    profile = Profile(
        profilename='%032x' % uuid.uuid4().int,  # unique name
        nodearch='m3',
        power='dc',
        consumption=ProfileConsumption(
            power=True,
            current=False,
            voltage=False,
            period=2116,
            average=1
        ),
        radio=ProfileRadio(
            mode='rssi',
            num_per_channel=0,
            period=1000,
            channels=[11]

        )

    )
    saved_profile = api.save_profile(profile=profile)

    assert saved_profile.to_dict() == profile.to_dict()

    yield saved_profile

    api.delete_profile(saved_profile.profilename)

    try:
        api.get_profile(saved_profile.profilename)
    except ApiException as e:
        assert e.status == 500


@pytest.mark.dependency()
def test_save(saved_profile):
    # GET on should get us the same

    get = api.get_profile(name=saved_profile.profilename)
    assert saved_profile.to_dict() == get.to_dict()

    # POST with the same should fail
    try:
        result = api.save_profile(profile=saved_profile)
    except ApiException as e:
        assert e.status == 500


@pytest.mark.dependency(depends=["test_save"])
def test_modify(saved_profile):
    saved_profile.consumption = ProfileConsumption(
            power=False,
            current=True,
            voltage=False,
            period=2116,
            average=4
        )

    # modify
    api.modify_profile(saved_profile.profilename, profile=saved_profile)

    get = api.get_profile(name=saved_profile.profilename)
    assert saved_profile.to_dict() == get.to_dict()


@pytest.mark.dependency(depends=["test_save"])
def test_rename(saved_profile):

    # rename
    old_name = saved_profile.profilename
    saved_profile.profilename = saved_profile.profilename + '_modified'

    api.modify_profile(name=old_name, profile=saved_profile)

    try:
        api.get_profile(name=old_name)
    except ApiException as e:
        assert e.status == 500

    get = api.get_profile(name=saved_profile.profilename)
    assert saved_profile.to_dict() == get.to_dict()
