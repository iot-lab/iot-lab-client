"""
*FirmwaresApi* | [**firmwares_get**](iotlabclient/client/docs/FirmwaresApi.md#firmwares_get) | **GET** /firmwares | get a list of stored firmware metadatas
*FirmwaresApi* | [**firmwares_name_delete**](iotlabclient/client/docs/FirmwaresApi.md#firmwares_name_delete) | **DELETE** /firmwares/{name} | Delete a user firmware
*FirmwaresApi* | [**firmwares_name_file_get**](iotlabclient/client/docs/FirmwaresApi.md#firmwares_name_file_get) | **GET** /firmwares/{name}/file | get a stored firmaware file
*FirmwaresApi* | [**firmwares_name_get**](iotlabclient/client/docs/FirmwaresApi.md#firmwares_name_get) | **GET** /firmwares/{name} | get a stored firmware metadata
*FirmwaresApi* | [**firmwares_name_put**](iotlabclient/client/docs/FirmwaresApi.md#firmwares_name_put) | **PUT** /firmwares/{name} | modify a stored user firmware
*FirmwaresApi* | [**firmwares_post**](iotlabclient/client/docs/FirmwaresApi.md#firmwares_post) | **POST** /firmwares | save a user firmware
*FirmwaresApi* | [**get_firmware_format**](iotlabclient/client/docs/FirmwaresApi.md#get_firmware_format) | **POST** /firmwares/checker | Returns firwmare f
"""
from pprint import pprint

from iotlabclient.api import Api
from iotlabclient.client import ArchiString
from iotlabclient.client.models.resource_type import ResourceType

api = Api().firmwares


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
