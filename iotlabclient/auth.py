# -*- coding:utf-8 -*-

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

""" Authentication file management """

import os
import os.path
import getpass
from base64 import b64decode

RC_FILE = (os.getenv('IOTLAB_PASSWORD_FILE') or
           os.path.expanduser('~/.iotlabrc'))


def get_user_credentials(username=None, password=None):
    """ Return user credentials.
    If provided in arguments return them, if password missing, ask on console,
    or try to read them from password file """

    if (password is not None) and (username is not None):
        pass
    elif (password is None) and (username is not None):
        password = getpass.getpass()
    else:
        username, password = _read_password_file()
    return username, password


def _read_password_file():
    """ Try to read password file (.iotlabrc) in user home directory when
    command-line option username and password are not used. If password
    file exist whe return username and password for basic auth http
    authentication
    """
    if not os.path.exists(RC_FILE):
        return None, None
    try:
        with open(RC_FILE, 'r') as password_file:
            username, enc_password = password_file.readline().split(':')
            # encode/decode for python3
            password = b64decode(enc_password.encode('utf-8')).decode('utf-8')
            return username, password
    except ValueError:
        raise ValueError('Bad password file format: %r' % RC_FILE)
