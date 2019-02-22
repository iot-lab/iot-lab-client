# iotlabclient.client.ModelsApi

All URIs are relative to *https://www.iot-lab.info/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_model_mobility_script**](ModelsApi.md#get_model_mobility_script) | **GET** /mobilities/models/{name}/file | Returns model script file
[**save_user_model_mobility**](ModelsApi.md#save_user_model_mobility) | **POST** /mobilities/models | Create model mobility


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
api_instance = iotlabclient.client.ModelsApi(iotlabclient.client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # Returns model script file
    api_response = api_instance.get_model_mobility_script(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->get_model_mobility_script: %s\n" % e)
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
api_instance = iotlabclient.client.ModelsApi(iotlabclient.client.ApiClient(configuration))
model = iotlabclient.client.Model() # Model |  (optional)
script = '/path/to/file' # file | the script that will be started on the robot (optional)

try:
    # Create model mobility
    api_response = api_instance.save_user_model_mobility(model=model, script=script)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelsApi->save_user_model_mobility: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

