# iotlabclient.client.NodesApi

All URIs are relative to *https://www.iot-lab.info/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_nodes**](NodesApi.md#get_nodes) | **GET** /nodes | Returns testbed nodes list.
[**get_nodes_id**](NodesApi.md#get_nodes_id) | **GET** /nodes/ids | Returns testbed nodes ids list (eg. 1-5+8).


# **get_nodes**
> NodesResponse get_nodes(site=site, archi=archi, state=state)

Returns testbed nodes list.

### Example

```python
from __future__ import print_function
import time
import iotlabclient.client
from iotlabclient.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iotlabclient.client.NodesApi()
site = 'all' # str | Filter by site (optional) (default to 'all')
archi = 'archi_example' # str | Filter by archi (optional)
state = 'state_example' # str | Filter by state (optional)

try:
    # Returns testbed nodes list.
    api_response = api_instance.get_nodes(site=site, archi=archi, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodesApi->get_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site** | **str**| Filter by site | [optional] [default to &#39;all&#39;]
 **archi** | **str**| Filter by archi | [optional] 
 **state** | **str**| Filter by state | [optional] 

### Return type

[**NodesResponse**](NodesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Testbed nodes list response. |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodes_id**
> NodesIdsResponse get_nodes_id()

Returns testbed nodes ids list (eg. 1-5+8).

### Example

```python
from __future__ import print_function
import time
import iotlabclient.client
from iotlabclient.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iotlabclient.client.NodesApi()

try:
    # Returns testbed nodes ids list (eg. 1-5+8).
    api_response = api_instance.get_nodes_id()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NodesApi->get_nodes_id: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NodesIdsResponse**](NodesIdsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Testbed nodes ids list response. |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

