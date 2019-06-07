# iotlabclient.client.SitesApi

All URIs are relative to *https://www.iot-lab.info/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sites**](SitesApi.md#get_sites) | **GET** /sites | Returns testbed sites list.
[**get_sites_details**](SitesApi.md#get_sites_details) | **GET** /sites/details | Returns tesbed sites details list.


# **get_sites**
> SitesResponse get_sites()

Returns testbed sites list.

### Example

```python
from __future__ import print_function
import time
import iotlabclient.client
from iotlabclient.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iotlabclient.client.SitesApi()

try:
    # Returns testbed sites list.
    api_response = api_instance.get_sites()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->get_sites: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SitesResponse**](SitesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Testbed sites list response. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sites_details**
> SitesDetailsResponse get_sites_details()

Returns tesbed sites details list.

### Example

```python
from __future__ import print_function
import time
import iotlabclient.client
from iotlabclient.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iotlabclient.client.SitesApi()

try:
    # Returns tesbed sites details list.
    api_response = api_instance.get_sites_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SitesApi->get_sites_details: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SitesDetailsResponse**](SitesDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Testbed sites details list response. |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

