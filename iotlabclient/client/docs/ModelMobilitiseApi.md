# iotlabclient.client.ModelMobilitiseApi

All URIs are relative to *https://www.iot-lab.info/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_model_mobility**](ModelMobilitiseApi.md#delete_user_model_mobility) | **DELETE** /mobilities/models/{name} | Delete model mobility


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
api_instance = iotlabclient.client.ModelMobilitiseApi(iotlabclient.client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # Delete model mobility
    api_instance.delete_user_model_mobility(name)
except ApiException as e:
    print("Exception when calling ModelMobilitiseApi->delete_user_model_mobility: %s\n" % e)
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

