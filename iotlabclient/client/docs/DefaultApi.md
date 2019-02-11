# iotlabclient.client.DefaultApi

All URIs are relative to *https://www.iot-lab.info/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_firmware_format**](DefaultApi.md#get_firmware_format) | **POST** /firmwares/checker | Returns firwmare format.


# **get_firmware_format**
> InlineResponse2002 get_firmware_format(firmware=firmware)

Returns firwmare format.

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
api_instance = iotlabclient.client.DefaultApi(iotlabclient.client.ApiClient(configuration))
firmware = '/path/to/file' # file | firmware binary file (optional)

try:
    # Returns firwmare format.
    api_response = api_instance.get_firmware_format(firmware=firmware)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_firmware_format: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firmware** | **file**| firmware binary file | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

