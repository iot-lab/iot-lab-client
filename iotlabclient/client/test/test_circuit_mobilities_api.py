# coding: utf-8

"""
    IoT-LAB REST API

    REST API documentation of [IoT-LAB](http://www.iot-lab.info) testbed.  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import iotlabclient.client
from iotlabclient.client.api.circuit_mobilities_api import CircuitMobilitiesApi  # noqa: E501
from iotlabclient.client.rest import ApiException


class TestCircuitMobilitiesApi(unittest.TestCase):
    """CircuitMobilitiesApi unit test stubs"""

    def setUp(self):
        self.api = iotlabclient.client.api.circuit_mobilities_api.CircuitMobilitiesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_user_mobility(self):
        """Test case for delete_user_mobility

        Delete circuit mobility  # noqa: E501
        """
        pass

    def test_get_mobilities(self):
        """Test case for get_mobilities

        Returns circuits list  # noqa: E501
        """
        pass

    def test_get_mobility(self):
        """Test case for get_mobility

        Returns circuit  # noqa: E501
        """
        pass

    def test_modify_user_mobility(self):
        """Test case for modify_user_mobility

        Modify circuit mobility  # noqa: E501
        """
        pass

    def test_save_user_mobility(self):
        """Test case for save_user_mobility

        Create circuit  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
