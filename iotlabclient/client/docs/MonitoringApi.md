# iotlabclient.client.MonitoringApi

All URIs are relative to *https://www.iot-lab.info/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_profile**](MonitoringApi.md#delete_profile) | **DELETE** /monitoring/{name} | Delete monitoring profile.
[**get_profile**](MonitoringApi.md#get_profile) | **GET** /monitoring/{name} | Returns monitoring profile.
[**get_profiles**](MonitoringApi.md#get_profiles) | **GET** /monitoring | Returns monitoring profiles list.
[**modify_profile**](MonitoringApi.md#modify_profile) | **PUT** /monitoring/{name} | Modify monitoring profile.
[**save_profile**](MonitoringApi.md#save_profile) | **POST** /monitoring | Create monitoring profile.


# **delete_profile**
> delete_profile(name)

Delete monitoring profile.

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
api_instance = iotlabclient.client.MonitoringApi(iotlabclient.client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # Delete monitoring profile.
    api_instance.delete_profile(name)
except ApiException as e:
    print("Exception when calling MonitoringApi->delete_profile: %s\n" % e)
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

# **get_profile**
> Profile get_profile(name)

Returns monitoring profile.

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
api_instance = iotlabclient.client.MonitoringApi(iotlabclient.client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # Returns monitoring profile.
    api_response = api_instance.get_profile(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringApi->get_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**Profile**](Profile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profiles**
> list[Profile] get_profiles(archi=archi)

Returns monitoring profiles list.

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
api_instance = iotlabclient.client.MonitoringApi(iotlabclient.client.ApiClient(configuration))
archi = 'archi_example' # str | Filter by archi (optional)

try:
    # Returns monitoring profiles list.
    api_response = api_instance.get_profiles(archi=archi)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringApi->get_profiles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **archi** | **str**| Filter by archi | [optional] 

### Return type

[**list[Profile]**](Profile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_profile**
> modify_profile(name, profile=profile)

Modify monitoring profile.

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
api_instance = iotlabclient.client.MonitoringApi(iotlabclient.client.ApiClient(configuration))
name = 'name_example' # str | 
profile = iotlabclient.client.Profile() # Profile |  (optional)

try:
    # Modify monitoring profile.
    api_instance.modify_profile(name, profile=profile)
except ApiException as e:
    print("Exception when calling MonitoringApi->modify_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **profile** | [**Profile**](Profile.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_profile**
> Profile save_profile(profile=profile)

Create monitoring profile.

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
api_instance = iotlabclient.client.MonitoringApi(iotlabclient.client.ApiClient(configuration))
profile = iotlabclient.client.Profile() # Profile |  (optional)

try:
    # Create monitoring profile.
    api_response = api_instance.save_profile(profile=profile)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringApi->save_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile** | [**Profile**](Profile.md)|  | [optional] 

### Return type

[**Profile**](Profile.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

