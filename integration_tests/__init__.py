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

""" integration tests """
import os

from dotenv import load_dotenv, find_dotenv
from iotlabclient.client.rest import ApiException

from iotlabclient.api import Api
from iotlabclient.client import Configuration

load_dotenv(find_dotenv())

HOST = os.environ.get('IOTLAB-HOST', 'https://devwww.iot-lab.info/api')
print('HOST: ' + HOST)

# should have a few m3 nodes
SITE = os.environ.get('IOTLAB-M3-SITE', 'devgrenoble')
TLD = '.iot-lab.info'
SITE_TLD = SITE + TLD

# site with some robots
ROBOT_SITE = os.environ.get('IOTLAB-ROBOT-SITE', 'devlille')

WSN430_SITE = os.environ.get('IOTLAB-WSN430-SITE', 'devstrasbourg')
TESTUSER_LOGIN = os.environ.get('IOTLAB-TESTUSER-LOGIN')
TESTUSER_PASSWORD = os.environ.get('IOTLAB-TESTUSER-PASSWORD')

configuration = Configuration()
configuration.username = TESTUSER_LOGIN
configuration.password = TESTUSER_PASSWORD
configuration.host = HOST
API = Api(configuration=configuration)
unauth = Configuration()
UNAUTH = Api(configuration=unauth)

# try login
API.users.get_user()
