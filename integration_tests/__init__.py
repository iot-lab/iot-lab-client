""" integration tests """
import os

from iotlabclient.api import Api

HOST = os.environ.get('IOTLAB-HOST', 'https://devwww.iot-lab.info/api')
print('HOST: ' + HOST)

# should have a few m3 nodes
SITE = os.environ.get('IOTLAB-SITE', 'devgrenoble')
TLD = '.iot-lab.info'
SITE_TLD = SITE + TLD

# site with some robots
ROBOT_SITE = os.environ.get('IOTLAB-ROBOT-SITE', 'devlille')

API = Api(host=HOST)
