# iotlabclient.client.ModelMobilitiesApi

All URIs are relative to *https://www.iot-lab.info/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_model_mobility**](ModelMobilitiesApi.md#delete_user_model_mobility) | **DELETE** /mobilities/models/{name} | Delete model mobility
[**get_model_mobilities**](ModelMobilitiesApi.md#get_model_mobilities) | **GET** /mobilities/models | Returns models list
[**get_model_mobility**](ModelMobilitiesApi.md#get_model_mobility) | **GET** /mobilities/models/{name} | Returns model
[**get_model_mobility_script**](ModelMobilitiesApi.md#get_model_mobility_script) | **GET** /mobilities/models/{name}/file | Returns model script file
[**modify_user_model_mobility**](ModelMobilitiesApi.md#modify_user_model_mobility) | **PUT** /mobilities/models/{name} | Modify model mobility
[**save_user_model_mobility**](ModelMobilitiesApi.md#save_user_model_mobility) | **POST** /mobilities/models | Create model mobility


# **delete_user_model_mobility**
> delete_user_model_mobility(name)

Delete model mobility

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
api_instance = iotlabclient.client.ModelMobilitiesApi(iotlabclient.client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # Delete model mobility
    api_instance.delete_user_model_mobility(name)
except ApiException as e:
    print("Exception when calling ModelMobilitiesApi->delete_user_model_mobility: %s\n" % e)
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
**204** | The model mobility has been successfully deleted. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_mobilities**
> ModelsListResponse get_model_mobilities(type=type)

Returns models list

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
api_instance = iotlabclient.client.ModelMobilitiesApi(iotlabclient.client.ApiClient(configuration))
type = iotlabclient.client.ResourceType() # ResourceType | Filter with mobility type (optional)

try:
    # Returns models list
    api_response = api_instance.get_model_mobilities(type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelMobilitiesApi->get_model_mobilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**ResourceType**](.md)| Filter with mobility type | [optional] 

### Return type

[**ModelsListResponse**](ModelsListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | models list response. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_mobility**
> Model get_model_mobility(name)

Returns model

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
api_instance = iotlabclient.client.ModelMobilitiesApi(iotlabclient.client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # Returns model
    api_response = api_instance.get_model_mobility(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelMobilitiesApi->get_model_mobility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**Model**](Model.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Model response. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_model_mobility_script**
> file get_model_mobility_script(name)

Returns model script file

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
api_instance = iotlabclient.client.ModelMobilitiesApi(iotlabclient.client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # Returns model script file
    api_response = api_instance.get_model_mobility_script(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelMobilitiesApi->get_model_mobility_script: %s\n" % e)
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
**200** | Model response. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_user_model_mobility**
> modify_user_model_mobility(name, model=model, script=script)

Modify model mobility

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
api_instance = iotlabclient.client.ModelMobilitiesApi(iotlabclient.client.ApiClient(configuration))
name = 'name_example' # str | 
model = iotlabclient.client.Model() # Model |  (optional)
script = '/path/to/file' # file | the script that will be started on the robot (optional)

try:
    # Modify model mobility
    api_instance.modify_user_model_mobility(name, model=model, script=script)
except ApiException as e:
    print("Exception when calling ModelMobilitiesApi->modify_user_model_mobility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **model** | [**Model**](Model.md)|  | [optional] 
 **script** | **file**| the script that will be started on the robot | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/mixed
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The circuit mobility has been successfully modified. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_user_model_mobility**
> Model save_user_model_mobility(model=model, script=script)

Create model mobility

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
api_instance = iotlabclient.client.ModelMobilitiesApi(iotlabclient.client.ApiClient(configuration))
model = iotlabclient.client.Model() # Model |  (optional)
script = '/path/to/file' # file | the script that will be started on the robot (optional)

try:
    # Create model mobility
    api_response = api_instance.save_user_model_mobility(model=model, script=script)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelMobilitiesApi->save_user_model_mobility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**Model**](Model.md)|  | [optional] 
 **script** | **file**| the script that will be started on the robot | [optional] 

### Return type

[**Model**](Model.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/mixed
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The model has been successfully created. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

