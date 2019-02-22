# iotlabclient.client.ModelmobilitiseApi

All URIs are relative to *https://www.iot-lab.info/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_model_mobility**](ModelmobilitiseApi.md#delete_user_model_mobility) | **DELETE** /mobilities/models/{name} | Delete model mobility
[**modify_user_model_mobility**](ModelmobilitiseApi.md#modify_user_model_mobility) | **PUT** /mobilities/models/{name} | Modify model mobility


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
api_instance = iotlabclient.client.ModelmobilitiseApi(iotlabclient.client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # Delete model mobility
    api_instance.delete_user_model_mobility(name)
except ApiException as e:
    print("Exception when calling ModelmobilitiseApi->delete_user_model_mobility: %s\n" % e)
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
api_instance = iotlabclient.client.ModelmobilitiseApi(iotlabclient.client.ApiClient(configuration))
name = 'name_example' # str | 
model = iotlabclient.client.Model() # Model |  (optional)
script = '/path/to/file' # file | the script that will be started on the robot (optional)

try:
    # Modify model mobility
    api_instance.modify_user_model_mobility(name, model=model, script=script)
except ApiException as e:
    print("Exception when calling ModelmobilitiseApi->modify_user_model_mobility: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

