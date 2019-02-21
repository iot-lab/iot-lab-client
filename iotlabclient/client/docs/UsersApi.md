# iotlabclient.client.UsersApi

All URIs are relative to *https://www.iot-lab.info/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_user**](UsersApi.md#activate_user) | **POST** /users/activate | Activate user.
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /user | Delete user.
[**delete_user_ssh_keys**](UsersApi.md#delete_user_ssh_keys) | **DELETE** /user/keys/{id} | Delete user ssh key.
[**get_user**](UsersApi.md#get_user) | **GET** /user | Returns user
[**get_user_ssh_keys**](UsersApi.md#get_user_ssh_keys) | **GET** /user/keys | Returns user ssh keys list.
[**modify_user**](UsersApi.md#modify_user) | **PUT** /user | Modify user
[**reset_password**](UsersApi.md#reset_password) | **POST** /users/reset_password | Reset user password by email
[**set_user_ssh_keys**](UsersApi.md#set_user_ssh_keys) | **POST** /user/keys | Add user ssh keys.
[**signup_user**](UsersApi.md#signup_user) | **POST** /users | Signup user.
[**update_password**](UsersApi.md#update_password) | **PUT** /user/password | Modify user password.


# **activate_user**
> activate_user(request=request)

Activate user.

### Example

```python
from __future__ import print_function
import time
import iotlabclient.client
from iotlabclient.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iotlabclient.client.UsersApi()
request = iotlabclient.client.ActivateUserRequest() # ActivateUserRequest |  (optional)

try:
    # Activate user.
    api_instance.activate_user(request=request)
except ApiException as e:
    print("Exception when calling UsersApi->activate_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ActivateUserRequest**](ActivateUserRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user()

Delete user.

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
api_instance = iotlabclient.client.UsersApi(iotlabclient.client.ApiClient(configuration))

try:
    # Delete user.
    api_instance.delete_user()
except ApiException as e:
    print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_ssh_keys**
> delete_user_ssh_keys(id)

Delete user ssh key.

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
api_instance = iotlabclient.client.UsersApi(iotlabclient.client.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete user ssh key.
    api_instance.delete_user_ssh_keys(id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user_ssh_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserResponse get_user()

Returns user

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
api_instance = iotlabclient.client.UsersApi(iotlabclient.client.ApiClient(configuration))

try:
    # Returns user
    api_response = api_instance.get_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_ssh_keys**
> UserSshKeys get_user_ssh_keys()

Returns user ssh keys list.

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
api_instance = iotlabclient.client.UsersApi(iotlabclient.client.ApiClient(configuration))

try:
    # Returns user ssh keys list.
    api_response = api_instance.get_user_ssh_keys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_ssh_keys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserSshKeys**](UserSshKeys.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_user**
> modify_user(request=request)

Modify user

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
api_instance = iotlabclient.client.UsersApi(iotlabclient.client.ApiClient(configuration))
request = iotlabclient.client.UserRequest() # UserRequest |  (optional)

try:
    # Modify user
    api_instance.modify_user(request=request)
except ApiException as e:
    print("Exception when calling UsersApi->modify_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**UserRequest**](UserRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> reset_password(request=request)

Reset user password by email

### Example

```python
from __future__ import print_function
import time
import iotlabclient.client
from iotlabclient.client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = iotlabclient.client.UsersApi()
request = iotlabclient.client.ResetPasswordRequest() # ResetPasswordRequest |  (optional)

try:
    # Reset user password by email
    api_instance.reset_password(request=request)
except ApiException as e:
    print("Exception when calling UsersApi->reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ResetPasswordRequest**](ResetPasswordRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_ssh_keys**
> set_user_ssh_keys(user_ssh_keys=user_ssh_keys)

Add user ssh keys.

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
api_instance = iotlabclient.client.UsersApi(iotlabclient.client.ApiClient(configuration))
user_ssh_keys = iotlabclient.client.UserSshKeys() # UserSshKeys |  (optional)

try:
    # Add user ssh keys.
    api_instance.set_user_ssh_keys(user_ssh_keys=user_ssh_keys)
except ApiException as e:
    print("Exception when calling UsersApi->set_user_ssh_keys: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_ssh_keys** | [**UserSshKeys**](UserSshKeys.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signup_user**
> UserResponse signup_user(request=request)

Signup user.

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
api_instance = iotlabclient.client.UsersApi(iotlabclient.client.ApiClient(configuration))
request = iotlabclient.client.UserRequest() # UserRequest |  (optional)

try:
    # Signup user.
    api_response = api_instance.signup_user(request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->signup_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**UserRequest**](UserRequest.md)|  | [optional] 

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_password**
> update_password(request=request)

Modify user password.

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
api_instance = iotlabclient.client.UsersApi(iotlabclient.client.ApiClient(configuration))
request = iotlabclient.client.UpdatePasswordRequest() # UpdatePasswordRequest |  (optional)

try:
    # Modify user password.
    api_instance.update_password(request=request)
except ApiException as e:
    print("Exception when calling UsersApi->update_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**UpdatePasswordRequest**](UpdatePasswordRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

