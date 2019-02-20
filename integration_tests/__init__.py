""" integration tests """
import os

HOST = os.environ.get('IOTLAB-HOST', 'https://devwww.iot-lab.info/api')
print('HOST: ' + HOST)

# should have a few m3 nodes
SITE = os.environ.get('IOTLAB-SITE', 'devgrenoble')
SITE_TLD = SITE + '.iot-lab.info'

# site with some robots
ROBOT_SITE = os.environ.get('IOTLAB-ROBOT-SITE', 'devlille')
