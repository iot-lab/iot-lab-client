# iotlabclient.client.ExperimentsApi

All URIs are relative to *https://www.iot-lab.info/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_experiments**](ExperimentsApi.md#get_experiments) | **GET** /experiments | Returns experiments list
[**get_experiments_total**](ExperimentsApi.md#get_experiments_total) | **GET** /experiments/total | Returns total number of experiments
[**get_running_experiments**](ExperimentsApi.md#get_running_experiments) | **GET** /experiments/running | Returns running testbed experiments list
[**submit_experiment**](ExperimentsApi.md#submit_experiment) | **POST** /experiments | Submit an experiment


# **get_experiments**
> ExperimentsResponse get_experiments(state=state, limit=limit, offset=offset)

Returns experiments list

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
api_instance = iotlabclient.client.ExperimentsApi(iotlabclient.client.ApiClient(configuration))
state = 'Running,Terminated,Stopped,Waiting' # str | Filter with state (optional) (default to 'Running,Terminated,Stopped,Waiting')
limit = 500 # int | Filter with number (optional) (default to 500)
offset = 0 # int | Filter with index (optional) (default to 0)

try:
    # Returns experiments list
    api_response = api_instance.get_experiments(state=state, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentsApi->get_experiments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **str**| Filter with state | [optional] [default to &#39;Running,Terminated,Stopped,Waiting&#39;]
 **limit** | **int**| Filter with number | [optional] [default to 500]
 **offset** | **int**| Filter with index | [optional] [default to 0]

### Return type

[**ExperimentsResponse**](ExperimentsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_experiments_total**
> TotalResponse get_experiments_total()

Returns total number of experiments

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
api_instance = iotlabclient.client.ExperimentsApi(iotlabclient.client.ApiClient(configuration))

try:
    # Returns total number of experiments
    api_response = api_instance.get_experiments_total()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentsApi->get_experiments_total: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TotalResponse**](TotalResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_running_experiments**
> ExperimentsResponse get_running_experiments(limit=limit, offset=offset)

Returns running testbed experiments list

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
api_instance = iotlabclient.client.ExperimentsApi(iotlabclient.client.ApiClient(configuration))
limit = 500 # int | Filter with number (optional) (default to 500)
offset = 0 # int | Filter with index (optional) (default to 0)

try:
    # Returns running testbed experiments list
    api_response = api_instance.get_running_experiments(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentsApi->get_running_experiments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Filter with number | [optional] [default to 500]
 **offset** | **int**| Filter with index | [optional] [default to 0]

### Return type

[**ExperimentsResponse**](ExperimentsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_experiment**
> InlineResponse200 submit_experiment(experiment=experiment, files=files)

Submit an experiment

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
api_instance = iotlabclient.client.ExperimentsApi(iotlabclient.client.ApiClient(configuration))
experiment = iotlabclient.client.ExperimentRequest() # ExperimentRequest |  (optional)
files = '/path/to/file' # list[file] | firmware/script/scriptconfig files (optional)

try:
    # Submit an experiment
    api_response = api_instance.submit_experiment(experiment=experiment, files=files)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentsApi->submit_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **experiment** | [**ExperimentRequest**](ExperimentRequest.md)|  | [optional] 
 **files** | **list[file]**| firmware/script/scriptconfig files | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

