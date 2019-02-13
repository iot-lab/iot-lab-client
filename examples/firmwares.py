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
*FirmwaresApi* | [**firmwares_name_file_get**](iotlabclient/client/docs/FirmwaresApi.md#firmwares_name_file_get) | **GET** /firmwares/{name}/file | get a stored firmaware file
*FirmwaresApi* | [**firmwares_name_get**](iotlabclient/client/docs/FirmwaresApi.md#firmwares_name_get) | **GET** /firmwares/{name} | get a stored firmware metadata
*FirmwaresApi* | [**firmwares_name_put**](iotlabclient/client/docs/FirmwaresApi.md#firmwares_name_put) | **PUT** /firmwares/{name} | modify a stored user firmware
*FirmwaresApi* | [**firmwares_post**](iotlabclient/client/docs/FirmwaresApi.md#firmwares_post) | **POST** /firmwares | save a user firmware
*FirmwaresApi* | [**get_firmware_format**](iotlabclient/client/docs/FirmwaresApi.md#get_firmware_format) | **POST** /firmwares/checker | Returns firwmare f
"""
import json
from pprint import pprint

from iotlabclient.client.rest import ApiException

from iotlabclient.api import Api
from iotlabclient.client import ArchiString, Firmware
from iotlabclient.client.models.resource_type import ResourceType

api = Api().firmwares


def delete_if_exists(firmware_name):
    try:
        api.firmwares_name_delete(firmware_name)
        print('OK, firmware %s deleted' % firmware_name)
    except ApiException:
        print('OK, firmware %s already inexistent' % firmware_name)


print('all firmwares')
pprint(api.firmwares_get())

print('all M3 firmwares')
pprint(api.firmwares_get(archi=ArchiString.M3))

print('explicit ALL M3 firmwares')
pprint(api.firmwares_get(archi=ArchiString.M3, type=ResourceType.ALL))

print('PREDEFINED M3 firmwares')
pprint(api.firmwares_get(archi=ArchiString.M3, type=ResourceType.PREDEFINED))

print('USERDEFINED firefly firmwares')
pprint(api.firmwares_get(archi=ArchiString.FIREFLY, type=ResourceType.USERDEFINED))

delete_if_exists('my_firmware')
firmware = Firmware(name='my_firmware', description='test firmware', archi=ArchiString.M3, filename='tutorial_m3.elf')

print('create my_firmware firmware')
api.firmwares_post(firmware='tutorial_m3.elf', metadata=json.dumps(firmware.to_dict()))

print('get my_firmware firmware')
pprint(api.firmwares_name_get(name='my_firmware'))

print('get my_firmware firmware file')
api.firmwares_name_file_get(name='my_firmware')

print('delete my_firmware firmware')
pprint(api.firmwares_name_delete('my_firmware'))

print('get my_firmware firmware should fail')
try:
    pprint(api.firmwares_name_get(name='my_firmware'))
except ApiException as e:
    assert e.status == 500


