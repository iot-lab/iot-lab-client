# coding: utf-8

"""
    IoT-LAB REST API

    REST API documentation of [IoT-LAB](http://www.iot-lab.info) testbed.  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from iotlabclient.client.api_client import ApiClient
from iotlabclient.client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class RobotsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def are_coordinates_reachable(self, site, **kwargs):  # noqa: E501
        """Returns if robots coordinates (eg. ROS points) are reachable  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.are_coordinates_reachable(site, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str site: (required)
        :param dict(str, Point) points:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CoordinatesReachable
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.are_coordinates_reachable_with_http_info(site, **kwargs)  # noqa: E501

    def are_coordinates_reachable_with_http_info(self, site, **kwargs):  # noqa: E501
        """Returns if robots coordinates (eg. ROS points) are reachable  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.are_coordinates_reachable_with_http_info(site, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str site: (required)
        :param dict(str, Point) points:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CoordinatesReachable, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['site', 'points']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method are_coordinates_reachable" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'site' is set
        if ('site' not in local_var_params or
                local_var_params['site'] is None):
            raise ApiValueError("Missing the required parameter `site` when calling `are_coordinates_reachable`")  # noqa: E501

        if 'site' in local_var_params and not re.search(r'^[a-z0-9]*$', local_var_params['site']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `site` when calling `are_coordinates_reachable`, must conform to the pattern `/^[a-z0-9]*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'site' in local_var_params:
            path_params['site'] = local_var_params['site']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        post_content_types = {}
        multipart_header_params = {}

        body_params = None
        if 'points' in local_var_params:
            body_params = local_var_params['points']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        # multiple potential response types
        response_types = {
            200: 'CoordinatesReachable',
            401: 'Error',
            403: 'Error',
            500: 'Error'
        }

        return self.api_client.call_api(
            '/robots/{site}/coordinates/isreachable', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            post_content_types=post_content_types,
            response_types=response_types,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_dock_config(self, site, **kwargs):  # noqa: E501
        """Returns robots site dock config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dock_config(site, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str site: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: RobotsDockConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_dock_config_with_http_info(site, **kwargs)  # noqa: E501

    def get_dock_config_with_http_info(self, site, **kwargs):  # noqa: E501
        """Returns robots site dock config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_dock_config_with_http_info(site, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str site: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(RobotsDockConfig, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['site']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_dock_config" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'site' is set
        if ('site' not in local_var_params or
                local_var_params['site'] is None):
            raise ApiValueError("Missing the required parameter `site` when calling `get_dock_config`")  # noqa: E501

        if 'site' in local_var_params and not re.search(r'^[a-z0-9]*$', local_var_params['site']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `site` when calling `get_dock_config`, must conform to the pattern `/^[a-z0-9]*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'site' in local_var_params:
            path_params['site'] = local_var_params['site']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        post_content_types = {}
        multipart_header_params = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        # multiple potential response types
        response_types = {
            200: 'RobotsDockConfig',
            401: 'Error',
            403: 'Error',
            500: 'Error'
        }

        return self.api_client.call_api(
            '/robots/{site}/dock/config', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            post_content_types=post_content_types,
            response_types=response_types,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_map_config(self, site, **kwargs):  # noqa: E501
        """Returns robots site map config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_map_config(site, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str site: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: RobotsMapConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_map_config_with_http_info(site, **kwargs)  # noqa: E501

    def get_map_config_with_http_info(self, site, **kwargs):  # noqa: E501
        """Returns robots site map config  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_map_config_with_http_info(site, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str site: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(RobotsMapConfig, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['site']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_map_config" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'site' is set
        if ('site' not in local_var_params or
                local_var_params['site'] is None):
            raise ApiValueError("Missing the required parameter `site` when calling `get_map_config`")  # noqa: E501

        if 'site' in local_var_params and not re.search(r'^[a-z0-9]*$', local_var_params['site']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `site` when calling `get_map_config`, must conform to the pattern `/^[a-z0-9]*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'site' in local_var_params:
            path_params['site'] = local_var_params['site']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        post_content_types = {}
        multipart_header_params = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        # multiple potential response types
        response_types = {
            200: 'RobotsMapConfig',
            401: 'Error',
            403: 'Error',
            500: 'Error'
        }

        return self.api_client.call_api(
            '/robots/{site}/map/config', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            post_content_types=post_content_types,
            response_types=response_types,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_map_coordinates(self, site, **kwargs):  # noqa: E501
        """Returns robots map coordinates from ros coordinates.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_map_coordinates(site, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str site: (required)
        :param Point point:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Point
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_map_coordinates_with_http_info(site, **kwargs)  # noqa: E501

    def get_map_coordinates_with_http_info(self, site, **kwargs):  # noqa: E501
        """Returns robots map coordinates from ros coordinates.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_map_coordinates_with_http_info(site, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str site: (required)
        :param Point point:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Point, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['site', 'point']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_map_coordinates" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'site' is set
        if ('site' not in local_var_params or
                local_var_params['site'] is None):
            raise ApiValueError("Missing the required parameter `site` when calling `get_map_coordinates`")  # noqa: E501

        if 'site' in local_var_params and not re.search(r'^[a-z0-9]*$', local_var_params['site']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `site` when calling `get_map_coordinates`, must conform to the pattern `/^[a-z0-9]*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'site' in local_var_params:
            path_params['site'] = local_var_params['site']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        post_content_types = {}
        multipart_header_params = {}

        body_params = None
        if 'point' in local_var_params:
            body_params = local_var_params['point']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        # multiple potential response types
        response_types = {
            200: 'Point',
            401: 'Error',
            403: 'Error',
            500: 'Error'
        }

        return self.api_client.call_api(
            '/robots/{site}/coordinates/map', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            post_content_types=post_content_types,
            response_types=response_types,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_map_image(self, site, **kwargs):  # noqa: E501
        """Returns robots site map image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_map_image(site, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str site: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_map_image_with_http_info(site, **kwargs)  # noqa: E501

    def get_map_image_with_http_info(self, site, **kwargs):  # noqa: E501
        """Returns robots site map image  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_map_image_with_http_info(site, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str site: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(file, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['site']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_map_image" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'site' is set
        if ('site' not in local_var_params or
                local_var_params['site'] is None):
            raise ApiValueError("Missing the required parameter `site` when calling `get_map_image`")  # noqa: E501

        if 'site' in local_var_params and not re.search(r'^[a-z0-9]*$', local_var_params['site']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `site` when calling `get_map_image`, must conform to the pattern `/^[a-z0-9]*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'site' in local_var_params:
            path_params['site'] = local_var_params['site']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        post_content_types = {}
        multipart_header_params = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/octet-stream', 'application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        # multiple potential response types
        response_types = {
            200: 'file',
            401: 'Error',
            403: 'Error',
            500: 'Error'
        }

        return self.api_client.call_api(
            '/robots/{site}/map/image', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            post_content_types=post_content_types,
            response_types=response_types,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_ros_coordinates(self, site, **kwargs):  # noqa: E501
        """Returns robots ros coordinates from map coordinates.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ros_coordinates(site, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str site: (required)
        :param Point point:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Point
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_ros_coordinates_with_http_info(site, **kwargs)  # noqa: E501

    def get_ros_coordinates_with_http_info(self, site, **kwargs):  # noqa: E501
        """Returns robots ros coordinates from map coordinates.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_ros_coordinates_with_http_info(site, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str site: (required)
        :param Point point:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Point, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['site', 'point']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_ros_coordinates" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'site' is set
        if ('site' not in local_var_params or
                local_var_params['site'] is None):
            raise ApiValueError("Missing the required parameter `site` when calling `get_ros_coordinates`")  # noqa: E501

        if 'site' in local_var_params and not re.search(r'^[a-z0-9]*$', local_var_params['site']):  # noqa: E501
            raise ApiValueError("Invalid value for parameter `site` when calling `get_ros_coordinates`, must conform to the pattern `/^[a-z0-9]*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'site' in local_var_params:
            path_params['site'] = local_var_params['site']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        post_content_types = {}
        multipart_header_params = {}

        body_params = None
        if 'point' in local_var_params:
            body_params = local_var_params['point']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        # multiple potential response types
        response_types = {
            200: 'Point',
            401: 'Error',
            403: 'Error',
            500: 'Error'
        }

        return self.api_client.call_api(
            '/robots/{site}/coordinates/ros', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            post_content_types=post_content_types,
            response_types=response_types,
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
