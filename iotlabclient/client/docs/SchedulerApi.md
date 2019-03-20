# iotlabclient.client.SchedulerApi

All URIs are relative to *https://www.iot-lab.info/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_experiments_jobs**](SchedulerApi.md#get_experiments_jobs) | **GET** /experiments/jobs | Returns past &amp; future testbed experiments jobs lists
[**get_nodes_states**](SchedulerApi.md#get_nodes_states) | **GET** /experiments/nodes_states | Returns nodes states, past &amp; current


# **get_experiments_jobs**
> ExperimentsResponse get_experiments_jobs(start=start, stop=stop)

Returns past & future testbed experiments jobs lists

### Example

```python
from __future__ import print_function
import time
import iotlabclient.client
from iotlabclient.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iotlabclient.client.SchedulerApi()
start = 'start_example' # str |  (optional)
stop = 'stop_example' # str |  (optional)

try:
    # Returns past & future testbed experiments jobs lists
    api_response = api_instance.get_experiments_jobs(start=start, stop=stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulerApi->get_experiments_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **str**|  | [optional] 
 **stop** | **str**|  | [optional] 

### Return type

[**ExperimentsResponse**](ExperimentsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nodes_states**
> NodesStatesResponse get_nodes_states(start=start, stop=stop)

Returns nodes states, past & current

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
api_instance = iotlabclient.client.SchedulerApi(iotlabclient.client.ApiClient(configuration))
start = 'start_example' # str |  (optional)
stop = 'stop_example' # str |  (optional)

try:
    # Returns nodes states, past & current
    api_response = api_instance.get_nodes_states(start=start, stop=stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulerApi->get_nodes_states: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **str**|  | [optional] 
 **stop** | **str**|  | [optional] 

### Return type

[**NodesStatesResponse**](NodesStatesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

