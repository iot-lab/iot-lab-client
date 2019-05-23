
"""
*FirmwaresApi* | [**firmwares_name_file_get**]
*FirmwaresApi* | [**firmwares_name_get**]
*FirmwaresApi* | [**firmwares_name_put**]
*FirmwaresApi* | [**firmwares_post**]
*FirmwaresApi* | [**get_firmware_format**]
"""
from pprint import pprint

from iotlabclient.client.rest import ApiException

from iotlabclient.api import Api
from iotlabclient.client import ArchiString, Firmware
from iotlabclient.client.models.resource_type import ResourceType

api = Api().firmwares


def delete_if_exists(firmware_name):
    try:
        api.delete_firmware(firmware_name)
        print('OK, firmware %s deleted' % firmware_name)
    except ApiException:
        print('OK, firmware %s already inexistent' % firmware_name)


print('all firmwares')
pprint(api.get_firmwares())

print('all M3 firmwares')
pprint(api.get_firmwares(
    archi=ArchiString.M3
))

print('explicit ALL M3 firmwares')
pprint(api.get_firmwares(
    archi=ArchiString.M3,
    type=ResourceType.ALL
))

print('PREDEFINED M3 firmwares')
pprint(api.get_firmwares(
    archi=ArchiString.M3,
    type=ResourceType.PREDEFINED
))

print('USERDEFINED firefly firmwares')
pprint(api.get_firmwares(
    archi=ArchiString.FIREFLY,
    type=ResourceType.USERDEFINED
))

delete_if_exists('my_firmware')
firmware = Firmware(
    name='my_firmware',
    description='test firmware',
    archi=ArchiString.M3,
    filename='tutorial_m3.elf')

print('create my_firmware firmware')
api.save_firmware(firmware='tutorial_m3.elf', metadata=firmware)

print('get my_firmware firmware')
pprint(api.get_firmware(name='my_firmware'))

print('get my_firmware firmware file')
api.get_firmware_file(name='my_firmware')

print('delete my_firmware firmware')
pprint(api.delete_firmware('my_firmware'))

print('get my_firmware firmware should fail')
try:
    pprint(api.get_firmware(name='my_firmware'))
except ApiException as e:
    assert e.status == 500
