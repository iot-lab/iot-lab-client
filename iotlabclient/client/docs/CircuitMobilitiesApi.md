# iotlabclient.client.CircuitMobilitiesApi

All URIs are relative to *https://www.iot-lab.info/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_user_mobility**](CircuitMobilitiesApi.md#delete_user_mobility) | **DELETE** /mobilities/circuits/{name} | Delete circuit mobility
[**get_mobilities**](CircuitMobilitiesApi.md#get_mobilities) | **GET** /mobilities/circuits | Returns circuits list
[**get_mobility**](CircuitMobilitiesApi.md#get_mobility) | **GET** /mobilities/circuits/{name} | Returns circuit
[**modify_user_mobility**](CircuitMobilitiesApi.md#modify_user_mobility) | **PUT** /mobilities/circuits/{name} | Modify circuit mobility
[**save_user_mobility**](CircuitMobilitiesApi.md#save_user_mobility) | **POST** /mobilities/circuits | Create circuit


# **delete_user_mobility**
> delete_user_mobility(name)

Delete circuit mobility

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
api_instance = iotlabclient.client.CircuitMobilitiesApi(iotlabclient.client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # Delete circuit mobility
    api_instance.delete_user_mobility(name)
except ApiException as e:
    print("Exception when calling CircuitMobilitiesApi->delete_user_mobility: %s\n" % e)
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
**204** | The circuit mobility has been successfully deleted. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mobilities**
> CircuitsListResponse get_mobilities(site=site, type=type)

Returns circuits list

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
api_instance = iotlabclient.client.CircuitMobilitiesApi(iotlabclient.client.ApiClient(configuration))
site = 'site_example' # str | Filter with site name (optional)
type = iotlabclient.client.ResourceType() # ResourceType | Filter with resource type (optional)

try:
    # Returns circuits list
    api_response = api_instance.get_mobilities(site=site, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitMobilitiesApi->get_mobilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site** | **str**| Filter with site name | [optional] 
 **type** | [**ResourceType**](.md)| Filter with resource type | [optional] 

### Return type

[**CircuitsListResponse**](CircuitsListResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Circuits list response. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mobility**
> Circuit get_mobility(name)

Returns circuit

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
api_instance = iotlabclient.client.CircuitMobilitiesApi(iotlabclient.client.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # Returns circuit
    api_response = api_instance.get_mobility(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitMobilitiesApi->get_mobility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**Circuit**](Circuit.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Circuit response. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_user_mobility**
> modify_user_mobility(name, circuit=circuit)

Modify circuit mobility

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
api_instance = iotlabclient.client.CircuitMobilitiesApi(iotlabclient.client.ApiClient(configuration))
name = 'name_example' # str | 
circuit = iotlabclient.client.Circuit() # Circuit |  (optional)

try:
    # Modify circuit mobility
    api_instance.modify_user_mobility(name, circuit=circuit)
except ApiException as e:
    print("Exception when calling CircuitMobilitiesApi->modify_user_mobility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **circuit** | [**Circuit**](Circuit.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The circuit mobility has been successfully modified. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_user_mobility**
> Circuit save_user_mobility(circuit=circuit)

Create circuit

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
api_instance = iotlabclient.client.CircuitMobilitiesApi(iotlabclient.client.ApiClient(configuration))
circuit = iotlabclient.client.Circuit() # Circuit |  (optional)

try:
    # Create circuit
    api_response = api_instance.save_user_mobility(circuit=circuit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CircuitMobilitiesApi->save_user_mobility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **circuit** | [**Circuit**](Circuit.md)|  | [optional] 

### Return type

[**Circuit**](Circuit.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The circuit has been successfully created. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

