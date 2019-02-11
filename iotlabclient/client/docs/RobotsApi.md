# iotlabclient.client.RobotsApi

All URIs are relative to *https://www.iot-lab.info/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**are_coordinates_reachable**](RobotsApi.md#are_coordinates_reachable) | **POST** /robots/{site}/coordinates/isreachable | Returns if robots coordinates (eg. ROS points) are reachable
[**get_dock_config**](RobotsApi.md#get_dock_config) | **GET** /robots/{site}/dock/config | Returns robots site dock config
[**get_map_config**](RobotsApi.md#get_map_config) | **GET** /robots/{site}/map/config | Returns robots site map config
[**get_map_coordinates**](RobotsApi.md#get_map_coordinates) | **POST** /robots/{site}/coordinates/map | Returns robots map coordinates from ros coordinates.
[**get_map_image**](RobotsApi.md#get_map_image) | **GET** /robots/{site}/map/image | Returns robots site map image
[**get_ros_coordinates**](RobotsApi.md#get_ros_coordinates) | **POST** /robots/{site}/coordinates/ros | Returns robots ros coordinates from map coordinates.


# **are_coordinates_reachable**
> CoordinatesReachable are_coordinates_reachable(site, request_body=request_body)

Returns if robots coordinates (eg. ROS points) are reachable

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
api_instance = iotlabclient.client.RobotsApi(iotlabclient.client.ApiClient(configuration))
site = 'site_example' # str | 
request_body = {'key': iotlabclient.client.Point()} # dict(str, Point) |  (optional)

try:
    # Returns if robots coordinates (eg. ROS points) are reachable
    api_response = api_instance.are_coordinates_reachable(site, request_body=request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotsApi->are_coordinates_reachable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site** | **str**|  | 
 **request_body** | [**dict(str, Point)**](Point.md)|  | [optional] 

### Return type

[**CoordinatesReachable**](CoordinatesReachable.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dock_config**
> RobotsDockConfig get_dock_config(site)

Returns robots site dock config

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
api_instance = iotlabclient.client.RobotsApi(iotlabclient.client.ApiClient(configuration))
site = 'site_example' # str | 

try:
    # Returns robots site dock config
    api_response = api_instance.get_dock_config(site)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotsApi->get_dock_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site** | **str**|  | 

### Return type

[**RobotsDockConfig**](RobotsDockConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_map_config**
> RobotsMapConfig get_map_config(site)

Returns robots site map config

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
api_instance = iotlabclient.client.RobotsApi(iotlabclient.client.ApiClient(configuration))
site = 'site_example' # str | 

try:
    # Returns robots site map config
    api_response = api_instance.get_map_config(site)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotsApi->get_map_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site** | **str**|  | 

### Return type

[**RobotsMapConfig**](RobotsMapConfig.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_map_coordinates**
> Point get_map_coordinates(site, point=point)

Returns robots map coordinates from ros coordinates.

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
api_instance = iotlabclient.client.RobotsApi(iotlabclient.client.ApiClient(configuration))
site = 'site_example' # str | 
point = iotlabclient.client.Point() # Point |  (optional)

try:
    # Returns robots map coordinates from ros coordinates.
    api_response = api_instance.get_map_coordinates(site, point=point)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotsApi->get_map_coordinates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site** | **str**|  | 
 **point** | [**Point**](Point.md)|  | [optional] 

### Return type

[**Point**](Point.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_map_image**
> file get_map_image(site)

Returns robots site map image

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
api_instance = iotlabclient.client.RobotsApi(iotlabclient.client.ApiClient(configuration))
site = 'site_example' # str | 

try:
    # Returns robots site map image
    api_response = api_instance.get_map_image(site)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotsApi->get_map_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site** | **str**|  | 

### Return type

**file**

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ros_coordinates**
> Point get_ros_coordinates(site, point=point)

Returns robots ros coordinates from map coordinates.

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
api_instance = iotlabclient.client.RobotsApi(iotlabclient.client.ApiClient(configuration))
site = 'site_example' # str | 
point = iotlabclient.client.Point() # Point |  (optional)

try:
    # Returns robots ros coordinates from map coordinates.
    api_response = api_instance.get_ros_coordinates(site, point=point)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RobotsApi->get_ros_coordinates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site** | **str**|  | 
 **point** | [**Point**](Point.md)|  | [optional] 

### Return type

[**Point**](Point.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

