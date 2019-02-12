# iotlabclient.client.FirmwaresApi

All URIs are relative to *https://www.iot-lab.info/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**firmwares_get**](FirmwaresApi.md#firmwares_get) | **GET** /firmwares | get a list of stored firmware metadatas
[**firmwares_name_delete**](FirmwaresApi.md#firmwares_name_delete) | **DELETE** /firmwares/{name} | Delete a user firmware
[**firmwares_name_file_get**](FirmwaresApi.md#firmwares_name_file_get) | **GET** /firmwares/{name}/file | get a stored firmaware file
[**firmwares_name_get**](FirmwaresApi.md#firmwares_name_get) | **GET** /firmwares/{name} | get a stored firmware metadata
[**firmwares_name_put**](FirmwaresApi.md#firmwares_name_put) | **PUT** /firmwares/{name} | modify a stored user firmware
[**firmwares_post**](FirmwaresApi.md#firmwares_post) | **POST** /firmwares | save a user firmware
[**get_firmware_format**](FirmwaresApi.md#get_firmware_format) | **POST** /firmwares/checker | Returns firwmare format.


# **firmwares_get**
> InlineResponse2003 firmwares_get(type=type, archi=archi, state=state)

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
type = 'all' # str | Filter by type (userde (optional) (default to 'all')
archi = 'archi_example' # str | Filter by archi (optional)
state = 'state_example' # str | Filter by state (optional)

try:
    # get a list of stored firmware metadatas
    api_response = api_instance.firmwares_get(type=type, archi=archi, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmwaresApi->firmwares_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Filter by type (userde | [optional] [default to &#39;all&#39;]
 **archi** | **str**| Filter by archi | [optional] 
 **state** | **str**| Filter by state | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmwares_name_delete**
> firmwares_name_delete(name)

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
    api_instance.firmwares_name_delete(name)
except ApiException as e:
    print("Exception when calling FirmwaresApi->firmwares_name_delete: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmwares_name_file_get**
> file firmwares_name_file_get(name)

get a stored firmaware file

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
    # get a stored firmaware file
    api_response = api_instance.firmwares_name_file_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmwaresApi->firmwares_name_file_get: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmwares_name_get**
> Firmware firmwares_name_get(name)

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
    api_response = api_instance.firmwares_name_get(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FirmwaresApi->firmwares_name_get: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmwares_name_put**
> firmwares_name_put(name, firmware=firmware, metadata=metadata)

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
    api_instance.firmwares_name_put(name, firmware=firmware, metadata=metadata)
except ApiException as e:
    print("Exception when calling FirmwaresApi->firmwares_name_put: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **firmwares_post**
> firmwares_post(firmware=firmware, metadata=metadata)

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
    api_instance.firmwares_post(firmware=firmware, metadata=metadata)
except ApiException as e:
    print("Exception when calling FirmwaresApi->firmwares_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firmware** | **file**| firmware binary file | [optional] 
 **metadata** | [**Firmware**](Firmware.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

