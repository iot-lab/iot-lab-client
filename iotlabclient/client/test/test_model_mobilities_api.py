# coding: utf-8

"""
    IoT-LAB REST API

    REST API documentation of [IoT-LAB](http://www.iot-lab.info) testbed.  # noqa: E501

    OpenAPI spec version: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import iotlabclient.client
from iotlabclient.client.api.model_mobilities_api import ModelMobilitiesApi  # noqa: E501
from iotlabclient.client.rest import ApiException


class TestModelMobilitiesApi(unittest.TestCase):
    """ModelMobilitiesApi unit test stubs"""

    def setUp(self):
        self.api = iotlabclient.client.api.model_mobilities_api.ModelMobilitiesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_model_mobility(self):
        """Test case for get_model_mobility

        Returns model  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()