# iotlabclient.client.ExperimentApi

All URIs are relative to *https://www.iot-lab.info/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**experiments_id_get**](ExperimentApi.md#experiments_id_get) | **GET** /experiments/{id} | Returns experiment.
[**experiments_id_nodes_flash_name_post**](ExperimentApi.md#experiments_id_nodes_flash_name_post) | **POST** /experiments/{id}/nodes/flash/{name} | Send experiment nodes flash firmware store command.
[**experiments_id_token_get**](ExperimentApi.md#experiments_id_token_get) | **GET** /experiments/{id}/token | Returns experiment websocket token.
[**get_experiment_archive**](ExperimentApi.md#get_experiment_archive) | **GET** /experiments/{id}/data | Returns experiment archive.
[**get_experiment_deployment**](ExperimentApi.md#get_experiment_deployment) | **GET** /experiments/{id}/deployment | Returns experiment deployment result.
[**get_experiment_nodes**](ExperimentApi.md#get_experiment_nodes) | **GET** /experiments/{id}/nodes | Returns experiment nodes list.
[**get_experiment_nodes_id**](ExperimentApi.md#get_experiment_nodes_id) | **GET** /experiments/{id}/nodes_ids | Returns experiment nodes id list (eg. 1-5+8).
[**kill_experiment_scripts**](ExperimentApi.md#kill_experiment_scripts) | **POST** /experiments/{id}/scripts/kill | Send frontend SSH kill script command.
[**reload_experiment**](ExperimentApi.md#reload_experiment) | **POST** /experiments/{id}/reload | Reload experiment.
[**run_experiment_scripts**](ExperimentApi.md#run_experiment_scripts) | **POST** /experiments/{id}/scripts/run | Send frontend SSH run script command
[**send_cmd_mobility_robots**](ExperimentApi.md#send_cmd_mobility_robots) | **POST** /experiments/{id}/robots/mobility/{name} | Send update robots mobility.
[**send_cmd_nodes**](ExperimentApi.md#send_cmd_nodes) | **POST** /experiments/{id}/nodes/{cmd} | Send experiment nodes command.
[**send_cmd_profile_nodes**](ExperimentApi.md#send_cmd_profile_nodes) | **POST** /experiments/{id}/nodes/monitoring/{name} | Send experiment nodes update monitoring profile store command.
[**send_cmd_robots**](ExperimentApi.md#send_cmd_robots) | **POST** /experiments/{id}/robots/{cmd} | Returns robots status.
[**send_cmd_update_nodes**](ExperimentApi.md#send_cmd_update_nodes) | **POST** /experiments/{id}/nodes/flash | Send experiment nodes flash firmware command.
[**send_load_profile_nodes**](ExperimentApi.md#send_load_profile_nodes) | **POST** /experiments/{id}/nodes/monitoring | Send experiment nodes load monitoring profile command.
[**status_experiment_scripts**](ExperimentApi.md#status_experiment_scripts) | **POST** /experiments/{id}/scripts/status | Returns frontend SSH status script.
[**stop_experiment**](ExperimentApi.md#stop_experiment) | **DELETE** /experiments/{id} | Stop experiment


# **experiments_id_get**
> ExperimentSubmission experiments_id_get(id)

Returns experiment.

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
api_instance = iotlabclient.client.ExperimentApi(iotlabclient.client.ApiClient(configuration))
id = 56 # int | 

try:
    # Returns experiment.
    api_response = api_instance.experiments_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiments_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ExperimentSubmission**](ExperimentSubmission.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiments_id_nodes_flash_name_post**
> Deployment experiments_id_nodes_flash_name_post(id, name, request_body=request_body)

Send experiment nodes flash firmware store command.

### Example

```python
from __future__ import print_function
import time
import iotlabclient.client
from iotlabclient.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iotlabclient.client.ExperimentApi()
id = 56 # int | 
name = 'name_example' # str | 
request_body = NULL # list[str] |  (optional)

try:
    # Send experiment nodes flash firmware store command.
    api_response = api_instance.experiments_id_nodes_flash_name_post(id, name, request_body=request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiments_id_nodes_flash_name_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **name** | **str**|  | 
 **request_body** | [**list[str]**](list.md)|  | [optional] 

### Return type

[**Deployment**](Deployment.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **experiments_id_token_get**
> InlineResponse2001 experiments_id_token_get(id)

Returns experiment websocket token.

### Example

```python
from __future__ import print_function
import time
import iotlabclient.client
from iotlabclient.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iotlabclient.client.ExperimentApi()
id = 56 # int | 

try:
    # Returns experiment websocket token.
    api_response = api_instance.experiments_id_token_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->experiments_id_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_experiment_archive**
> file get_experiment_archive(id)

Returns experiment archive.

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
api_instance = iotlabclient.client.ExperimentApi(iotlabclient.client.ApiClient(configuration))
id = 56 # int | 

try:
    # Returns experiment archive.
    api_response = api_instance.get_experiment_archive(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->get_experiment_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**file**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_experiment_deployment**
> Deployment get_experiment_deployment(id)

Returns experiment deployment result.

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
api_instance = iotlabclient.client.ExperimentApi(iotlabclient.client.ApiClient(configuration))
id = 56 # int | 

try:
    # Returns experiment deployment result.
    api_response = api_instance.get_experiment_deployment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->get_experiment_deployment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_experiment_nodes**
> NodesResponse get_experiment_nodes(id)

Returns experiment nodes list.

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
api_instance = iotlabclient.client.ExperimentApi(iotlabclient.client.ApiClient(configuration))
id = 56 # int | 

try:
    # Returns experiment nodes list.
    api_response = api_instance.get_experiment_nodes(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->get_experiment_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**NodesResponse**](NodesResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_experiment_nodes_id**
> NodesIdsResponse get_experiment_nodes_id(id)

Returns experiment nodes id list (eg. 1-5+8).

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
api_instance = iotlabclient.client.ExperimentApi(iotlabclient.client.ApiClient(configuration))
id = 56 # int | 

try:
    # Returns experiment nodes id list (eg. 1-5+8).
    api_response = api_instance.get_experiment_nodes_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->get_experiment_nodes_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**NodesIdsResponse**](NodesIdsResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kill_experiment_scripts**
> Deployment kill_experiment_scripts(id, request_body=request_body)

Send frontend SSH kill script command.

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
api_instance = iotlabclient.client.ExperimentApi(iotlabclient.client.ApiClient(configuration))
id = 56 # int | 
request_body = NULL # list[str] |  (optional)

try:
    # Send frontend SSH kill script command.
    api_response = api_instance.kill_experiment_scripts(id, request_body=request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->kill_experiment_scripts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **request_body** | [**list[str]**](list.md)|  | [optional] 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reload_experiment**
> InlineResponse200 reload_experiment(id, reload=reload)

Reload experiment.

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
api_instance = iotlabclient.client.ExperimentApi(iotlabclient.client.ApiClient(configuration))
id = 56 # int | 
reload = iotlabclient.client.Reload() # Reload |  (optional)

try:
    # Reload experiment.
    api_response = api_instance.reload_experiment(id, reload=reload)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->reload_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **reload** | [**Reload**](Reload.md)|  | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_experiment_scripts**
> Deployment run_experiment_scripts(id, script=script, scriptconfig=scriptconfig, scriptassociation=scriptassociation)

Send frontend SSH run script command

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
api_instance = iotlabclient.client.ExperimentApi(iotlabclient.client.ApiClient(configuration))
id = 56 # int | 
script = '/path/to/file' # file | script binary file (optional)
scriptconfig = '/path/to/file' # file | script config file (optional)
scriptassociation = iotlabclient.client.ScriptAssociations() # ScriptAssociations |  (optional)

try:
    # Send frontend SSH run script command
    api_response = api_instance.run_experiment_scripts(id, script=script, scriptconfig=scriptconfig, scriptassociation=scriptassociation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->run_experiment_scripts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **script** | **file**| script binary file | [optional] 
 **scriptconfig** | **file**| script config file | [optional] 
 **scriptassociation** | [**ScriptAssociations**](ScriptAssociations.md)|  | [optional] 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_cmd_mobility_robots**
> Deployment send_cmd_mobility_robots(id, name, request_body=request_body)

Send update robots mobility.

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
api_instance = iotlabclient.client.ExperimentApi(iotlabclient.client.ApiClient(configuration))
id = 56 # int | 
name = 'name_example' # str | 
request_body = NULL # list[str] |  (optional)

try:
    # Send update robots mobility.
    api_response = api_instance.send_cmd_mobility_robots(id, name, request_body=request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->send_cmd_mobility_robots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **name** | **str**|  | 
 **request_body** | [**list[str]**](list.md)|  | [optional] 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_cmd_nodes**
> Deployment send_cmd_nodes(id, cmd, request_body=request_body)

Send experiment nodes command.

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
api_instance = iotlabclient.client.ExperimentApi(iotlabclient.client.ApiClient(configuration))
id = 56 # int | 
cmd = 'cmd_example' # str | 
request_body = NULL # list[str] |  (optional)

try:
    # Send experiment nodes command.
    api_response = api_instance.send_cmd_nodes(id, cmd, request_body=request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->send_cmd_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **cmd** | **str**|  | 
 **request_body** | [**list[str]**](list.md)|  | [optional] 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_cmd_profile_nodes**
> Deployment send_cmd_profile_nodes(id, name, request_body=request_body)

Send experiment nodes update monitoring profile store command.

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
api_instance = iotlabclient.client.ExperimentApi(iotlabclient.client.ApiClient(configuration))
id = 56 # int | 
name = 'name_example' # str | 
request_body = NULL # list[str] |  (optional)

try:
    # Send experiment nodes update monitoring profile store command.
    api_response = api_instance.send_cmd_profile_nodes(id, name, request_body=request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->send_cmd_profile_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **name** | **str**|  | 
 **request_body** | [**list[str]**](list.md)|  | [optional] 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_cmd_robots**
> RobotsStatusResponse send_cmd_robots(id, cmd, request_body=request_body)

Returns robots status.

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
api_instance = iotlabclient.client.ExperimentApi(iotlabclient.client.ApiClient(configuration))
id = 56 # int | 
cmd = 'cmd_example' # str | 
request_body = NULL # list[str] |  (optional)

try:
    # Returns robots status.
    api_response = api_instance.send_cmd_robots(id, cmd, request_body=request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->send_cmd_robots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **cmd** | **str**|  | 
 **request_body** | [**list[str]**](list.md)|  | [optional] 

### Return type

[**RobotsStatusResponse**](RobotsStatusResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_cmd_update_nodes**
> Deployment send_cmd_update_nodes(id, firmware=firmware, nodes=nodes)

Send experiment nodes flash firmware command.

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
api_instance = iotlabclient.client.ExperimentApi(iotlabclient.client.ApiClient(configuration))
id = 56 # int | 
firmware = '/path/to/file' # file | firmware binary file (optional)
nodes = 'nodes_example' # list[str] | nodes list (optional)

try:
    # Send experiment nodes flash firmware command.
    api_response = api_instance.send_cmd_update_nodes(id, firmware=firmware, nodes=nodes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->send_cmd_update_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **firmware** | **file**| firmware binary file | [optional] 
 **nodes** | [**list[str]**](str.md)| nodes list | [optional] 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_load_profile_nodes**
> Deployment send_load_profile_nodes(id, profile=profile, nodes=nodes)

Send experiment nodes load monitoring profile command.

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
api_instance = iotlabclient.client.ExperimentApi(iotlabclient.client.ApiClient(configuration))
id = 56 # int | 
profile = '/path/to/file' # file | monitoring profile file (optional)
nodes = 'nodes_example' # list[str] | nodes list (optional)

try:
    # Send experiment nodes load monitoring profile command.
    api_response = api_instance.send_load_profile_nodes(id, profile=profile, nodes=nodes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->send_load_profile_nodes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **profile** | **file**| monitoring profile file | [optional] 
 **nodes** | [**list[str]**](str.md)| nodes list | [optional] 

### Return type

[**Deployment**](Deployment.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_experiment_scripts**
> StatusResponse status_experiment_scripts(id, request_body=request_body)

Returns frontend SSH status script.

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
api_instance = iotlabclient.client.ExperimentApi(iotlabclient.client.ApiClient(configuration))
id = 56 # int | 
request_body = NULL # list[str] |  (optional)

try:
    # Returns frontend SSH status script.
    api_response = api_instance.status_experiment_scripts(id, request_body=request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->status_experiment_scripts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **request_body** | [**list[str]**](list.md)|  | [optional] 

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_experiment**
> StopResponse stop_experiment(id)

Stop experiment

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
api_instance = iotlabclient.client.ExperimentApi(iotlabclient.client.ApiClient(configuration))
id = 56 # int | 

try:
    # Stop experiment
    api_response = api_instance.stop_experiment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExperimentApi->stop_experiment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**StopResponse**](StopResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

