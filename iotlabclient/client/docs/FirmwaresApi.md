# iotlabclient.client.FirmwaresApi

All URIs are relative to *https://www.iot-lab.info/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_firmware**](FirmwaresApi.md#delete_firmware) | **DELETE** /firmwares/{name} | Delete a user firmware
[**get_firmware**](FirmwaresApi.md#get_firmware) | **GET** /firmwares/{name} | get a stored firmware metadata
[**get_firmware_file**](FirmwaresApi.md#get_firmware_file) | **GET** /firmwares/{name}/file | get a stored firmware file
[**get_firmware_format**](FirmwaresApi.md#get_firmware_format) | **POST** /firmwares/checker | Returns firwmare format.
[**get_firmwares**](FirmwaresApi.md#get_firmwares) | **GET** /firmwares | get a list of stored firmware metadatas
[**modify_firmware**](FirmwaresApi.md#modify_firmware) | **PUT** /firmwares/{name} | modify a stored user firmware
[**save_firmware**](FirmwaresApi.md#save_firmware) | **POST** /firmwares | save a user firmware


# **delete_firmware**
> delete_firmware(name)

Delete a user firmware

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import iotlabclient.client
from iotlabclient.client.rest import ApiException
from pprint import pprint
configuration = iotlabclient.client.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = iotlabclient.client.FirmwaresApi(iotlabclient.client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # Delete a user firmware
    api_instance.delete_firmware(name)
except ApiException as e:
    print("Exception when calling FirmwaresApi->delete_firmware: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | the user firmware was correctly deleted |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firmware**
> Firmware get_firmware(name)

get a stored firmware metadata

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import iotlabclient.client
from iotlabclient.client.rest import ApiException
from pprint import pprint
configuration = iotlabclient.client.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = iotlabclient.client.FirmwaresApi(iotlabclient.client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # get a stored firmware metadata
    api_response = api_instance.get_firmware(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmwaresApi->get_firmware: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**Firmware**](Firmware.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns the stored user firmware metadata |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firmware_file**
> file get_firmware_file(name)

get a stored firmware file

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import iotlabclient.client
from iotlabclient.client.rest import ApiException
from pprint import pprint
configuration = iotlabclient.client.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = iotlabclient.client.FirmwaresApi(iotlabclient.client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # get a stored firmware file
    api_response = api_instance.get_firmware_file(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmwaresApi->get_firmware_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

**file**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns the stored user firmware file |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firmware_format**
> InlineResponse2002 get_firmware_format(firmware=firmware)

Returns firwmare format.

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import iotlabclient.client
from iotlabclient.client.rest import ApiException
from pprint import pprint
configuration = iotlabclient.client.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = iotlabclient.client.FirmwaresApi(iotlabclient.client.ApiClient(configuration))
firmware = '/path/to/file' # file | firmware binary file (optional)

try:
    # Returns firwmare format.
    api_response = api_instance.get_firmware_format(firmware=firmware)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmwaresApi->get_firmware_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firmware** | **file**| firmware binary file | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Firmware format response. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_firmwares**
> list[Firmware] get_firmwares(type=type, archi=archi)

get a list of stored firmware metadatas

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import iotlabclient.client
from iotlabclient.client.rest import ApiException
from pprint import pprint
configuration = iotlabclient.client.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = iotlabclient.client.FirmwaresApi(iotlabclient.client.ApiClient(configuration))
type = iotlabclient.client.ResourceType() # ResourceType | Filter by type (userde (optional)
archi = iotlabclient.client.ArchiString() # ArchiString | Filter by archi (optional)

try:
    # get a list of stored firmware metadatas
    api_response = api_instance.get_firmwares(type=type, archi=archi)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmwaresApi->get_firmwares: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**ResourceType**](.md)| Filter by type (userde | [optional] 
 **archi** | [**ArchiString**](.md)| Filter by archi | [optional] 

### Return type

[**list[Firmware]**](Firmware.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | returns a list of firmware metadatas |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_firmware**
> modify_firmware(name, firmware=firmware, metadata=metadata)

modify a stored user firmware

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import iotlabclient.client
from iotlabclient.client.rest import ApiException
from pprint import pprint
configuration = iotlabclient.client.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = iotlabclient.client.FirmwaresApi(iotlabclient.client.ApiClient(configuration))
name = 'name_example' # str | 
firmware = '/path/to/file' # file | firmware binary file (optional)
metadata = iotlabclient.client.Firmware() # Firmware |  (optional)

try:
    # modify a stored user firmware
    api_instance.modify_firmware(name, firmware=firmware, metadata=metadata)
except ApiException as e:
    print("Exception when calling FirmwaresApi->modify_firmware: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **firmware** | **file**| firmware binary file | [optional] 
 **metadata** | [**Firmware**](Firmware.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user firmware was correctly modified |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_firmware**
> Firmware save_firmware(firmware=firmware, metadata=metadata)

save a user firmware

### Example

* Basic Authentication (BasicAuth):
```python
from __future__ import print_function
import time
import iotlabclient.client
from iotlabclient.client.rest import ApiException
from pprint import pprint
configuration = iotlabclient.client.Configuration()
# Configure HTTP basic authorization: BasicAuth
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = iotlabclient.client.FirmwaresApi(iotlabclient.client.ApiClient(configuration))
firmware = '/path/to/file' # file | firmware binary file (optional)
metadata = iotlabclient.client.Firmware() # Firmware |  (optional)

try:
    # save a user firmware
    api_response = api_instance.save_firmware(firmware=firmware, metadata=metadata)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmwaresApi->save_firmware: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firmware** | **file**| firmware binary file | [optional] 
 **metadata** | [**Firmware**](Firmware.md)|  | [optional] 

### Return type

[**Firmware**](Firmware.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The user firmware was correctly modified |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

