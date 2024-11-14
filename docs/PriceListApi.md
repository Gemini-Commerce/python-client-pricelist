# pricelist.PriceListApi

All URIs are relative to *https://pricelist.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_price_list**](PriceListApi.md#create_price_list) | **POST** /pricelist.PriceList/CreatePriceList | Create new list
[**delete_price_list_items**](PriceListApi.md#delete_price_list_items) | **POST** /pricelist.PriceList/DeletePriceListItems | Get prices for items
[**get_full_price_items_by_pricelist_id**](PriceListApi.md#get_full_price_items_by_pricelist_id) | **POST** /pricelist.PriceList/GetFullPriceItemsByPricelistId | List detailed items
[**get_price_list**](PriceListApi.md#get_price_list) | **POST** /pricelist.PriceList/GetPriceList | Get specific list
[**get_price_list_by_code**](PriceListApi.md#get_price_list_by_code) | **POST** /pricelist.PriceList/GetPriceListByCode | Get list by code
[**get_price_list_items**](PriceListApi.md#get_price_list_items) | **POST** /pricelist.PriceList/GetPriceListItems | Get items in list
[**get_prices_items**](PriceListApi.md#get_prices_items) | **POST** /pricelist.PriceList/GetPricesItems | Get detailed items
[**list_full_price_items_by_pricelist_id**](PriceListApi.md#list_full_price_items_by_pricelist_id) | **POST** /pricelist.PriceList/ListFullPriceItemsByPricelistId | List detailed price items for a specific price list
[**list_price_lists**](PriceListApi.md#list_price_lists) | **POST** /pricelist.PriceList/ListPriceLists | List all price lists
[**price_list_get_price_items_by_price_list_item_ids**](PriceListApi.md#price_list_get_price_items_by_price_list_item_ids) | **POST** /pricelist.PriceList/GetPriceItemsByPriceListItemIds | 
[**set_price_list_items**](PriceListApi.md#set_price_list_items) | **POST** /pricelist.PriceList/SetPriceListItems | Set items in list
[**update_price_list**](PriceListApi.md#update_price_list) | **POST** /pricelist.PriceList/UpdatePriceList | Update list


# **create_price_list**
> PricelistCreatePriceListResponse create_price_list(body)

Create new list

Allows the creation of a new price list with specified details such as code, name, currency, and type.

### Example

* Api Key Authentication (Authorization):

```python
import pricelist
from pricelist.models.pricelist_create_price_list_request import PricelistCreatePriceListRequest
from pricelist.models.pricelist_create_price_list_response import PricelistCreatePriceListResponse
from pricelist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pricelist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = pricelist.Configuration(
    host = "https://pricelist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with pricelist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricelist.PriceListApi(api_client)
    body = pricelist.PricelistCreatePriceListRequest() # PricelistCreatePriceListRequest | 

    try:
        # Create new list
        api_response = api_instance.create_price_list(body)
        print("The response of PriceListApi->create_price_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListApi->create_price_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PricelistCreatePriceListRequest**](PricelistCreatePriceListRequest.md)|  | 

### Return type

[**PricelistCreatePriceListResponse**](PricelistCreatePriceListResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_price_list_items**
> object delete_price_list_items(body)

Get prices for items

Deletes specified items from a price list based on their unique identifiers.

### Example

* Api Key Authentication (Authorization):

```python
import pricelist
from pricelist.models.pricelist_delete_price_list_items_request import PricelistDeletePriceListItemsRequest
from pricelist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pricelist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = pricelist.Configuration(
    host = "https://pricelist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with pricelist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricelist.PriceListApi(api_client)
    body = pricelist.PricelistDeletePriceListItemsRequest() # PricelistDeletePriceListItemsRequest | 

    try:
        # Get prices for items
        api_response = api_instance.delete_price_list_items(body)
        print("The response of PriceListApi->delete_price_list_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListApi->delete_price_list_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PricelistDeletePriceListItemsRequest**](PricelistDeletePriceListItemsRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_full_price_items_by_pricelist_id**
> PricelistGetFullPriceItemsResponse get_full_price_items_by_pricelist_id(body)

List detailed items

Fetches detailed information about items, including historical price data, for a specific price list.

### Example

* Api Key Authentication (Authorization):

```python
import pricelist
from pricelist.models.pricelist_get_full_price_items_request import PricelistGetFullPriceItemsRequest
from pricelist.models.pricelist_get_full_price_items_response import PricelistGetFullPriceItemsResponse
from pricelist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pricelist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = pricelist.Configuration(
    host = "https://pricelist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with pricelist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricelist.PriceListApi(api_client)
    body = pricelist.PricelistGetFullPriceItemsRequest() # PricelistGetFullPriceItemsRequest | 

    try:
        # List detailed items
        api_response = api_instance.get_full_price_items_by_pricelist_id(body)
        print("The response of PriceListApi->get_full_price_items_by_pricelist_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListApi->get_full_price_items_by_pricelist_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PricelistGetFullPriceItemsRequest**](PricelistGetFullPriceItemsRequest.md)|  | 

### Return type

[**PricelistGetFullPriceItemsResponse**](PricelistGetFullPriceItemsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_list**
> PricelistGetPriceListResponse get_price_list(body)

Get specific list

Returns information about a particular price list identified by tenant ID and price list ID. The response includes details such as code, name, currency, and type.

### Example

* Api Key Authentication (Authorization):

```python
import pricelist
from pricelist.models.pricelist_get_price_list_request import PricelistGetPriceListRequest
from pricelist.models.pricelist_get_price_list_response import PricelistGetPriceListResponse
from pricelist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pricelist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = pricelist.Configuration(
    host = "https://pricelist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with pricelist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricelist.PriceListApi(api_client)
    body = pricelist.PricelistGetPriceListRequest() # PricelistGetPriceListRequest | 

    try:
        # Get specific list
        api_response = api_instance.get_price_list(body)
        print("The response of PriceListApi->get_price_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListApi->get_price_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PricelistGetPriceListRequest**](PricelistGetPriceListRequest.md)|  | 

### Return type

[**PricelistGetPriceListResponse**](PricelistGetPriceListResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_list_by_code**
> PricelistGetPriceListByCodeResponse get_price_list_by_code(body)

Get list by code

Retrieves information about a specific price list using the unique code associated with it. The response includes details such as code, name, currency, and type.

### Example

* Api Key Authentication (Authorization):

```python
import pricelist
from pricelist.models.pricelist_get_price_list_by_code_request import PricelistGetPriceListByCodeRequest
from pricelist.models.pricelist_get_price_list_by_code_response import PricelistGetPriceListByCodeResponse
from pricelist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pricelist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = pricelist.Configuration(
    host = "https://pricelist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with pricelist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricelist.PriceListApi(api_client)
    body = pricelist.PricelistGetPriceListByCodeRequest() # PricelistGetPriceListByCodeRequest | 

    try:
        # Get list by code
        api_response = api_instance.get_price_list_by_code(body)
        print("The response of PriceListApi->get_price_list_by_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListApi->get_price_list_by_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PricelistGetPriceListByCodeRequest**](PricelistGetPriceListByCodeRequest.md)|  | 

### Return type

[**PricelistGetPriceListByCodeResponse**](PricelistGetPriceListByCodeResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_price_list_items**
> PricelistGetPriceListItemsResponse get_price_list_items(body)

Get items in list

Fetches a paginated list of items associated with a particular price list.

### Example

* Api Key Authentication (Authorization):

```python
import pricelist
from pricelist.models.pricelist_get_price_list_items_request import PricelistGetPriceListItemsRequest
from pricelist.models.pricelist_get_price_list_items_response import PricelistGetPriceListItemsResponse
from pricelist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pricelist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = pricelist.Configuration(
    host = "https://pricelist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with pricelist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricelist.PriceListApi(api_client)
    body = pricelist.PricelistGetPriceListItemsRequest() # PricelistGetPriceListItemsRequest | 

    try:
        # Get items in list
        api_response = api_instance.get_price_list_items(body)
        print("The response of PriceListApi->get_price_list_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListApi->get_price_list_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PricelistGetPriceListItemsRequest**](PricelistGetPriceListItemsRequest.md)|  | 

### Return type

[**PricelistGetPriceListItemsResponse**](PricelistGetPriceListItemsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_prices_items**
> PricelistGetPricesResponse get_prices_items(body)

Get detailed items

Retrieves the current prices of specified items considering the provided context, such as currency and market.

### Example

* Api Key Authentication (Authorization):

```python
import pricelist
from pricelist.models.pricelist_get_prices_request import PricelistGetPricesRequest
from pricelist.models.pricelist_get_prices_response import PricelistGetPricesResponse
from pricelist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pricelist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = pricelist.Configuration(
    host = "https://pricelist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with pricelist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricelist.PriceListApi(api_client)
    body = pricelist.PricelistGetPricesRequest() # PricelistGetPricesRequest | 

    try:
        # Get detailed items
        api_response = api_instance.get_prices_items(body)
        print("The response of PriceListApi->get_prices_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListApi->get_prices_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PricelistGetPricesRequest**](PricelistGetPricesRequest.md)|  | 

### Return type

[**PricelistGetPricesResponse**](PricelistGetPricesResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_full_price_items_by_pricelist_id**
> PricelistListFullPriceItemsResponse list_full_price_items_by_pricelist_id(body)

List detailed price items for a specific price list

Retrieves a paginated list of detailed price items, including historical data, for a specific price list.

### Example

* Api Key Authentication (Authorization):

```python
import pricelist
from pricelist.models.pricelist_list_full_price_items_request import PricelistListFullPriceItemsRequest
from pricelist.models.pricelist_list_full_price_items_response import PricelistListFullPriceItemsResponse
from pricelist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pricelist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = pricelist.Configuration(
    host = "https://pricelist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with pricelist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricelist.PriceListApi(api_client)
    body = pricelist.PricelistListFullPriceItemsRequest() # PricelistListFullPriceItemsRequest | 

    try:
        # List detailed price items for a specific price list
        api_response = api_instance.list_full_price_items_by_pricelist_id(body)
        print("The response of PriceListApi->list_full_price_items_by_pricelist_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListApi->list_full_price_items_by_pricelist_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PricelistListFullPriceItemsRequest**](PricelistListFullPriceItemsRequest.md)|  | 

### Return type

[**PricelistListFullPriceItemsResponse**](PricelistListFullPriceItemsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_price_lists**
> PricelistListPriceListsResponse list_price_lists(body)

List all price lists

Retrieves a list of price lists based on optional filters such as name, code, and other attributes. The response includes details such as code, name, currency, and type.

### Example

* Api Key Authentication (Authorization):

```python
import pricelist
from pricelist.models.pricelist_list_price_lists_request import PricelistListPriceListsRequest
from pricelist.models.pricelist_list_price_lists_response import PricelistListPriceListsResponse
from pricelist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pricelist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = pricelist.Configuration(
    host = "https://pricelist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with pricelist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricelist.PriceListApi(api_client)
    body = pricelist.PricelistListPriceListsRequest() # PricelistListPriceListsRequest | 

    try:
        # List all price lists
        api_response = api_instance.list_price_lists(body)
        print("The response of PriceListApi->list_price_lists:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListApi->list_price_lists: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PricelistListPriceListsRequest**](PricelistListPriceListsRequest.md)|  | 

### Return type

[**PricelistListPriceListsResponse**](PricelistListPriceListsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **price_list_get_price_items_by_price_list_item_ids**
> PricelistGetPriceItemsByPriceListItemIdsResponse price_list_get_price_items_by_price_list_item_ids(body)



### Example

* Api Key Authentication (Authorization):

```python
import pricelist
from pricelist.models.pricelist_get_price_items_by_price_list_item_ids_request import PricelistGetPriceItemsByPriceListItemIdsRequest
from pricelist.models.pricelist_get_price_items_by_price_list_item_ids_response import PricelistGetPriceItemsByPriceListItemIdsResponse
from pricelist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pricelist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = pricelist.Configuration(
    host = "https://pricelist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with pricelist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricelist.PriceListApi(api_client)
    body = pricelist.PricelistGetPriceItemsByPriceListItemIdsRequest() # PricelistGetPriceItemsByPriceListItemIdsRequest | 

    try:
        api_response = api_instance.price_list_get_price_items_by_price_list_item_ids(body)
        print("The response of PriceListApi->price_list_get_price_items_by_price_list_item_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListApi->price_list_get_price_items_by_price_list_item_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PricelistGetPriceItemsByPriceListItemIdsRequest**](PricelistGetPriceItemsByPriceListItemIdsRequest.md)|  | 

### Return type

[**PricelistGetPriceItemsByPriceListItemIdsResponse**](PricelistGetPriceItemsByPriceListItemIdsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_price_list_items**
> PricelistSetPriceListItemsResponse set_price_list_items(body)

Set items in list

Updates or creates items for a given price list, allowing bulk modifications.

### Example

* Api Key Authentication (Authorization):

```python
import pricelist
from pricelist.models.pricelist_set_price_list_items_request import PricelistSetPriceListItemsRequest
from pricelist.models.pricelist_set_price_list_items_response import PricelistSetPriceListItemsResponse
from pricelist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pricelist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = pricelist.Configuration(
    host = "https://pricelist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with pricelist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricelist.PriceListApi(api_client)
    body = pricelist.PricelistSetPriceListItemsRequest() # PricelistSetPriceListItemsRequest | 

    try:
        # Set items in list
        api_response = api_instance.set_price_list_items(body)
        print("The response of PriceListApi->set_price_list_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListApi->set_price_list_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PricelistSetPriceListItemsRequest**](PricelistSetPriceListItemsRequest.md)|  | 

### Return type

[**PricelistSetPriceListItemsResponse**](PricelistSetPriceListItemsResponse.md)

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_price_list**
> object update_price_list(body)

Update list

Modifies the attributes of an existing price list based on the provided payload and field mask. The field mask is used to specify which attributes of the price list are to be updated. The field mask is a comma-separated list of fully qualified names of fields. Example: `code,name,currency,type`

### Example

* Api Key Authentication (Authorization):

```python
import pricelist
from pricelist.models.pricelist_update_price_list_request import PricelistUpdatePriceListRequest
from pricelist.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://pricelist.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = pricelist.Configuration(
    host = "https://pricelist.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Authorization
configuration.api_key['Authorization'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# Enter a context with an instance of the API client
with pricelist.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pricelist.PriceListApi(api_client)
    body = pricelist.PricelistUpdatePriceListRequest() # PricelistUpdatePriceListRequest | 

    try:
        # Update list
        api_response = api_instance.update_price_list(body)
        print("The response of PriceListApi->update_price_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PriceListApi->update_price_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PricelistUpdatePriceListRequest**](PricelistUpdatePriceListRequest.md)|  | 

### Return type

**object**

### Authorization

[Authorization](../README.md#Authorization)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

