# openapi_client.DefaultApi

All URIs are relative to *https://api.classifyai.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_new_model**](DefaultApi.md#create_new_model) | **PUT** /models | Create New Model
[**delete_model**](DefaultApi.md#delete_model) | **DELETE** /models | Delete Model
[**get_models_list**](DefaultApi.md#get_models_list) | **GET** /models | Get Models List
[**index_by_image_url**](DefaultApi.md#index_by_image_url) | **GET** /index_by_image_url | Index by Using Image URL
[**index_image**](DefaultApi.md#index_image) | **POST** /index_image | Index Local Image
[**tag_image_by_url**](DefaultApi.md#tag_image_by_url) | **GET** /predict_by_image_url | Tag Image by Using Image Url
[**tag_local_image**](DefaultApi.md#tag_local_image) | **POST** /predict | Predict by Image
[**update_model**](DefaultApi.md#update_model) | **POST** /models | Update Model


# **create_new_model**
> create_new_model(model_name)

Create New Model

Create a new custom image recognition model

### Example

* Api Key Authentication (x-api-key):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.classifyai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.classifyai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration = openapi_client.Configuration(
    host = "https://api.classifyai.com",
    api_key = {
        'x-api-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    model_name = '{\"model_name\":\"\\\"Test model name\\\"\"}' # str | Set a name for your model

    try:
        # Create New Model
        api_instance.create_new_model(model_name)
    except ApiException as e:
        print("Exception when calling DefaultApi->create_new_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_name** | **str**| Set a name for your model | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created |  -  |
**400** | Bad request, parameter or format error. Please check your query. |  -  |
**401** | You are not authorized to create a new model |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_model**
> delete_model(model_id)

Delete Model

Delete Model

### Example

* Api Key Authentication (x-api-key):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.classifyai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.classifyai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration = openapi_client.Configuration(
    host = "https://api.classifyai.com",
    api_key = {
        'x-api-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    model_id = 'model_id_example' # str | You can find your model ids from Classify Dashboard.

    try:
        # Delete Model
        api_instance.delete_model(model_id)
    except ApiException as e:
        print("Exception when calling DefaultApi->delete_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**| You can find your model ids from Classify Dashboard. | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Deleted. |  -  |
**400** | Bad request, parameter or format error. please check your query. |  -  |
**401** | You are not authorized to delete this model. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_models_list**
> str get_models_list()

Get Models List

Get the list of of models created 

### Example

* Api Key Authentication (x-api-key):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.classifyai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.classifyai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration = openapi_client.Configuration(
    host = "https://api.classifyai.com",
    api_key = {
        'x-api-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    
    try:
        # Get Models List
        api_response = api_instance.get_models_list()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_models_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Query executed succesfully. |  -  |
**401** | You don&#39;t have authorization to get the model list. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_by_image_url**
> str index_by_image_url(model_id, image_url)

Index by Using Image URL

Index by Using Image URL

### Example

* Api Key Authentication (x-api-key):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.classifyai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.classifyai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration = openapi_client.Configuration(
    host = "https://api.classifyai.com",
    api_key = {
        'x-api-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    model_id = 'model_id_example' # str | Model ID
image_url = 'image_url_example' # str | Image URL

    try:
        # Index by Using Image URL
        api_response = api_instance.index_by_image_url(model_id, image_url)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->index_by_image_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**| Model ID | 
 **image_url** | **str**| Image URL | 

### Return type

**str**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image Indexed |  -  |
**400** | Bad request, parameter or format error. Please check your query, image format and image size. |  -  |
**401** | You are not authorized for this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_image**
> str index_image(model_id, file=file)

Index Local Image

Index Local Image

### Example

* Api Key Authentication (x-api-key):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.classifyai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.classifyai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration = openapi_client.Configuration(
    host = "https://api.classifyai.com",
    api_key = {
        'x-api-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    model_id = 'model_id_example' # str | Model ID
file = '/path/to/file' # file |  (optional)

    try:
        # Index Local Image
        api_response = api_instance.index_image(model_id, file=file)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->index_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**| Model ID | 
 **file** | **file**|  | [optional] 

### Return type

**str**

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Image Indexed |  -  |
**400** | Bad request, parameter or format error. Please check your query, image format and image size. |  -  |
**401** | You are not authorized for this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_image_by_url**
> tag_image_by_url(model_id, image_url)

Tag Image by Using Image Url

Predict image tags by providing image url

### Example

* Api Key Authentication (x-api-key):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.classifyai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.classifyai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration = openapi_client.Configuration(
    host = "https://api.classifyai.com",
    api_key = {
        'x-api-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    model_id = 'model_id_example' # str | Type your trained model id to predict. You get your model's id from Classify Dashboard.
image_url = 'image_url_example' # str | Provide image url to predict

    try:
        # Tag Image by Using Image Url
        api_instance.tag_image_by_url(model_id, image_url)
    except ApiException as e:
        print("Exception when calling DefaultApi->tag_image_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**| Type your trained model id to predict. You get your model&#39;s id from Classify Dashboard. | 
 **image_url** | **str**| Provide image url to predict | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom trained model prediction response. |  -  |
**400** | Bad request, parameter or format error. Please check your query, image format and image size. |  -  |
**401** | You are not authorized for this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tag_local_image**
> tag_local_image(model_id, file=file)

Predict by Image

Send a local image to tag

### Example

* Api Key Authentication (x-api-key):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.classifyai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.classifyai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration = openapi_client.Configuration(
    host = "https://api.classifyai.com",
    api_key = {
        'x-api-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    model_id = 'model_id_example' # str | Type your trained model id to predict. You get your model's id from Classify Dashboard.
file = '/path/to/file' # file |  (optional)

    try:
        # Predict by Image
        api_instance.tag_local_image(model_id, file=file)
    except ApiException as e:
        print("Exception when calling DefaultApi->tag_local_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**| Type your trained model id to predict. You get your model&#39;s id from Classify Dashboard. | 
 **file** | **file**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom trained model prediction response. |  -  |
**400** | Bad request, parameter or format error. Please check your query, image format and image size. |  -  |
**401** | You are not authorized for this operation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_model**
> update_model(model_name, model_id)

Update Model

Update Model Name

### Example

* Api Key Authentication (x-api-key):
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.classifyai.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.classifyai.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x-api-key
configuration = openapi_client.Configuration(
    host = "https://api.classifyai.com",
    api_key = {
        'x-api-key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.DefaultApi(api_client)
    model_name = 'model_name_example' # str | Model Name
model_id = 'model_id_example' # str | Model id to be renamed.

    try:
        # Update Model
        api_instance.update_model(model_name, model_id)
    except ApiException as e:
        print("Exception when calling DefaultApi->update_model: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_name** | **str**| Model Name | 
 **model_id** | **str**| Model id to be renamed. | 

### Return type

void (empty response body)

### Authorization

[x-api-key](../README.md#x-api-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfull |  -  |
**400** | Bad request, parameter or format error. Please check your query. |  -  |
**401** | You are not authorized to edit this model. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

