# coding: utf-8

"""

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class PricesApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def get_price_ticks(self, instrument_id, from_timestamp, to_timestamp, **kwargs):
        """
        Returns the prices ticks.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_price_ticks(instrument_id, from_timestamp, to_timestamp, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str instrument_id:  (required)
        :param int from_timestamp: From timestamp in milliseconds UTC (required)
        :param int to_timestamp: To timestamp in milliseconds UTC (required)
        :return: list[PriceTick]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_price_ticks_with_http_info(instrument_id, from_timestamp, to_timestamp, **kwargs)
        else:
            (data) = self.get_price_ticks_with_http_info(instrument_id, from_timestamp, to_timestamp, **kwargs)
            return data

    def get_price_ticks_with_http_info(self, instrument_id, from_timestamp, to_timestamp, **kwargs):
        """
        Returns the prices ticks.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_price_ticks_with_http_info(instrument_id, from_timestamp, to_timestamp, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str instrument_id:  (required)
        :param int from_timestamp: From timestamp in milliseconds UTC (required)
        :param int to_timestamp: To timestamp in milliseconds UTC (required)
        :return: list[PriceTick]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instrument_id', 'from_timestamp', 'to_timestamp']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_price_ticks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instrument_id' is set
        if ('instrument_id' not in params) or (params['instrument_id'] is None):
            raise ValueError("Missing the required parameter `instrument_id` when calling `get_price_ticks`")
        # verify the required parameter 'from_timestamp' is set
        if ('from_timestamp' not in params) or (params['from_timestamp'] is None):
            raise ValueError("Missing the required parameter `from_timestamp` when calling `get_price_ticks`")
        # verify the required parameter 'to_timestamp' is set
        if ('to_timestamp' not in params) or (params['to_timestamp'] is None):
            raise ValueError("Missing the required parameter `to_timestamp` when calling `get_price_ticks`")


        collection_formats = {}

        resource_path = '/prices/{instrumentId}'.replace('{format}', 'json')
        path_params = {}
        if 'instrument_id' in params:
            path_params['instrumentId'] = params['instrument_id']

        query_params = {}
        if 'from_timestamp' in params:
            query_params['fromTimestamp'] = params['from_timestamp']
        if 'to_timestamp' in params:
            query_params['toTimestamp'] = params['to_timestamp']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type='list[PriceTick]',
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)

    def get_price_ticks_avro(self, instrument_id, from_timestamp, to_timestamp, **kwargs):
        """
        Returns the prices ticks in Avro format.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_price_ticks_avro(instrument_id, from_timestamp, to_timestamp, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str instrument_id:  (required)
        :param int from_timestamp: From timestamp in milliseconds UTC (required)
        :param int to_timestamp: To timestamp in milliseconds UTC (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_price_ticks_avro_with_http_info(instrument_id, from_timestamp, to_timestamp, **kwargs)
        else:
            (data) = self.get_price_ticks_avro_with_http_info(instrument_id, from_timestamp, to_timestamp, **kwargs)
            return data

    def get_price_ticks_avro_with_http_info(self, instrument_id, from_timestamp, to_timestamp, **kwargs):
        """
        Returns the prices ticks in Avro format.
        

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_price_ticks_avro_with_http_info(instrument_id, from_timestamp, to_timestamp, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str instrument_id:  (required)
        :param int from_timestamp: From timestamp in milliseconds UTC (required)
        :param int to_timestamp: To timestamp in milliseconds UTC (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['instrument_id', 'from_timestamp', 'to_timestamp']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_price_ticks_avro" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'instrument_id' is set
        if ('instrument_id' not in params) or (params['instrument_id'] is None):
            raise ValueError("Missing the required parameter `instrument_id` when calling `get_price_ticks_avro`")
        # verify the required parameter 'from_timestamp' is set
        if ('from_timestamp' not in params) or (params['from_timestamp'] is None):
            raise ValueError("Missing the required parameter `from_timestamp` when calling `get_price_ticks_avro`")
        # verify the required parameter 'to_timestamp' is set
        if ('to_timestamp' not in params) or (params['to_timestamp'] is None):
            raise ValueError("Missing the required parameter `to_timestamp` when calling `get_price_ticks_avro`")


        collection_formats = {}

        resource_path = '/prices/{instrumentId}/avro'.replace('{format}', 'json')
        path_params = {}
        if 'instrument_id' in params:
            path_params['instrumentId'] = params['instrument_id']

        query_params = {}
        if 'from_timestamp' in params:
            query_params['fromTimestamp'] = params['from_timestamp']
        if 'to_timestamp' in params:
            query_params['toTimestamp'] = params['to_timestamp']

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/octet-stream'])
        if not header_params['Accept']:
            del header_params['Accept']

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type([])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(resource_path, 'GET',
                                            path_params,
                                            query_params,
                                            header_params,
                                            body=body_params,
                                            post_params=form_params,
                                            files=local_var_files,
                                            response_type=None,
                                            auth_settings=auth_settings,
                                            callback=params.get('callback'),
                                            _return_http_data_only=params.get('_return_http_data_only'),
                                            _preload_content=params.get('_preload_content', True),
                                            _request_timeout=params.get('_request_timeout'),
                                            collection_formats=collection_formats)
