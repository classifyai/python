# coding: utf-8

"""
    Classify

    Classify Custom Image Recognition Service  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: info@inoven.ai
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_new_model(self, model_name, **kwargs):  # noqa: E501
        """Create New Model  # noqa: E501

        Create a new custom image recognition model  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_new_model(model_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str model_name: Set a name for your model (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_new_model_with_http_info(model_name, **kwargs)  # noqa: E501

    def create_new_model_with_http_info(self, model_name, **kwargs):  # noqa: E501
        """Create New Model  # noqa: E501

        Create a new custom image recognition model  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_new_model_with_http_info(model_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str model_name: Set a name for your model (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_hosts = [
            'https://api.classifyai.com'
        ]
        local_var_host = local_var_hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(local_var_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(local_var_host)
                )
            local_var_host = local_var_hosts[_host_index]
        local_var_params = locals()

        all_params = [
            'model_name'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params and key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_new_model" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'model_name' is set
        if self.api_client.client_side_validation and ('model_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['model_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `model_name` when calling `create_new_model`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'model_name' in local_var_params and local_var_params['model_name'] is not None:  # noqa: E501
            query_params.append(('model_name', local_var_params['model_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/models', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            _host=local_var_host,
            collection_formats=collection_formats)

    def delete_model(self, model_id, **kwargs):  # noqa: E501
        """Delete Model  # noqa: E501

        Delete Model  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_model(model_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str model_id: You can find your model ids from Classify Dashboard. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_model_with_http_info(model_id, **kwargs)  # noqa: E501

    def delete_model_with_http_info(self, model_id, **kwargs):  # noqa: E501
        """Delete Model  # noqa: E501

        Delete Model  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_model_with_http_info(model_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str model_id: You can find your model ids from Classify Dashboard. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_hosts = [
            'https://api.classifyai.com'
        ]
        local_var_host = local_var_hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(local_var_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(local_var_host)
                )
            local_var_host = local_var_hosts[_host_index]
        local_var_params = locals()

        all_params = [
            'model_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params and key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_model" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'model_id' is set
        if self.api_client.client_side_validation and ('model_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['model_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `model_id` when calling `delete_model`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'model_id' in local_var_params and local_var_params['model_id'] is not None:  # noqa: E501
            query_params.append(('model_id', local_var_params['model_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/models', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            _host=local_var_host,
            collection_formats=collection_formats)

    def get_models_list(self, **kwargs):  # noqa: E501
        """Get Models List  # noqa: E501

        Get the list of of models created   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_models_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_models_list_with_http_info(**kwargs)  # noqa: E501

    def get_models_list_with_http_info(self, **kwargs):  # noqa: E501
        """Get Models List  # noqa: E501

        Get the list of of models created   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_models_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_hosts = [
            'https://api.classifyai.com'
        ]
        local_var_host = local_var_hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(local_var_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(local_var_host)
                )
            local_var_host = local_var_hosts[_host_index]
        local_var_params = locals()

        all_params = [
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params and key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_models_list" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/models', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            _host=local_var_host,
            collection_formats=collection_formats)

    def tag_image_by_url(self, model_id, image_url, **kwargs):  # noqa: E501
        """Tag Image by Using Image Url  # noqa: E501

        Predict image tags by providing image url  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tag_image_by_url(model_id, image_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str model_id: Type your trained model id to predict. You get your model's id from Classify Dashboard. (required)
        :param str image_url: Provide image url to predict (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.tag_image_by_url_with_http_info(model_id, image_url, **kwargs)  # noqa: E501

    def tag_image_by_url_with_http_info(self, model_id, image_url, **kwargs):  # noqa: E501
        """Tag Image by Using Image Url  # noqa: E501

        Predict image tags by providing image url  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tag_image_by_url_with_http_info(model_id, image_url, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str model_id: Type your trained model id to predict. You get your model's id from Classify Dashboard. (required)
        :param str image_url: Provide image url to predict (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_hosts = [
            'https://api.classifyai.com'
        ]
        local_var_host = local_var_hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(local_var_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(local_var_host)
                )
            local_var_host = local_var_hosts[_host_index]
        local_var_params = locals()

        all_params = [
            'model_id',
            'image_url'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params and key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tag_image_by_url" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'model_id' is set
        if self.api_client.client_side_validation and ('model_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['model_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `model_id` when calling `tag_image_by_url`")  # noqa: E501
        # verify the required parameter 'image_url' is set
        if self.api_client.client_side_validation and ('image_url' not in local_var_params or  # noqa: E501
                                                        local_var_params['image_url'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `image_url` when calling `tag_image_by_url`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'model_id' in local_var_params and local_var_params['model_id'] is not None:  # noqa: E501
            query_params.append(('model_id', local_var_params['model_id']))  # noqa: E501
        if 'image_url' in local_var_params and local_var_params['image_url'] is not None:  # noqa: E501
            query_params.append(('image_url', local_var_params['image_url']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/predict_by_image_url', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            _host=local_var_host,
            collection_formats=collection_formats)

    def tag_local_image(self, model_id, **kwargs):  # noqa: E501
        """Predict by Image  # noqa: E501

        Send a local image to tag  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tag_local_image(model_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str model_id: Type your trained model id to predict. You get your model's id from Classify Dashboard. (required)
        :param file file:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.tag_local_image_with_http_info(model_id, **kwargs)  # noqa: E501

    def tag_local_image_with_http_info(self, model_id, **kwargs):  # noqa: E501
        """Predict by Image  # noqa: E501

        Send a local image to tag  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.tag_local_image_with_http_info(model_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str model_id: Type your trained model id to predict. You get your model's id from Classify Dashboard. (required)
        :param file file:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_hosts = [
            'https://api.classifyai.com'
        ]
        local_var_host = local_var_hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(local_var_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(local_var_host)
                )
            local_var_host = local_var_hosts[_host_index]
        local_var_params = locals()

        all_params = [
            'model_id',
            'file'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params and key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tag_local_image" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'model_id' is set
        if self.api_client.client_side_validation and ('model_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['model_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `model_id` when calling `tag_local_image`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'model_id' in local_var_params and local_var_params['model_id'] is not None:  # noqa: E501
            query_params.append(('model_id', local_var_params['model_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in local_var_params:
            local_var_files['file'] = local_var_params['file']  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/predict', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            _host=local_var_host,
            collection_formats=collection_formats)

    def update_model(self, model_name, model_id, **kwargs):  # noqa: E501
        """Update Model  # noqa: E501

        Update Model Name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_model(model_name, model_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str model_name: Model Name (required)
        :param str model_id: Model id to be renamed. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_model_with_http_info(model_name, model_id, **kwargs)  # noqa: E501

    def update_model_with_http_info(self, model_name, model_id, **kwargs):  # noqa: E501
        """Update Model  # noqa: E501

        Update Model Name  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_model_with_http_info(model_name, model_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str model_name: Model Name (required)
        :param str model_id: Model id to be renamed. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_hosts = [
            'https://api.classifyai.com'
        ]
        local_var_host = local_var_hosts[0]
        if kwargs.get('_host_index'):
            _host_index = int(kwargs.get('_host_index'))
            if _host_index < 0 or _host_index >= len(local_var_hosts):
                raise ApiValueError(
                    "Invalid host index. Must be 0 <= index < %s"
                    % len(local_var_host)
                )
            local_var_host = local_var_hosts[_host_index]
        local_var_params = locals()

        all_params = [
            'model_name',
            'model_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params and key != "_host_index":
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_model" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'model_name' is set
        if self.api_client.client_side_validation and ('model_name' not in local_var_params or  # noqa: E501
                                                        local_var_params['model_name'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `model_name` when calling `update_model`")  # noqa: E501
        # verify the required parameter 'model_id' is set
        if self.api_client.client_side_validation and ('model_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['model_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `model_id` when calling `update_model`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'model_name' in local_var_params and local_var_params['model_name'] is not None:  # noqa: E501
            query_params.append(('model_name', local_var_params['model_name']))  # noqa: E501
        if 'model_id' in local_var_params and local_var_params['model_id'] is not None:  # noqa: E501
            query_params.append(('model_id', local_var_params['model_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['x-api-key']  # noqa: E501

        return self.api_client.call_api(
            '/models', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            _host=local_var_host,
            collection_formats=collection_formats)