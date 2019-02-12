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
from iotlabclient.client.api.firmwares_api import FirmwaresApi  # noqa: E501
from iotlabclient.client.rest import ApiException


class TestFirmwaresApi(unittest.TestCase):
    """FirmwaresApi unit test stubs"""

    def setUp(self):
        self.api = iotlabclient.client.api.firmwares_api.FirmwaresApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_firmwares_get(self):
        """Test case for firmwares_get

        get a list of stored firmware metadatas  # noqa: E501
        """
        pass

    def test_firmwares_name_delete(self):
        """Test case for firmwares_name_delete

        Delete a user firmware  # noqa: E501
        """
        pass

    def test_firmwares_name_file_get(self):
        """Test case for firmwares_name_file_get

        get a stored firmaware file  # noqa: E501
        """
        pass

    def test_firmwares_name_get(self):
        """Test case for firmwares_name_get

        get a stored firmware metadata  # noqa: E501
        """
        pass

    def test_firmwares_name_put(self):
        """Test case for firmwares_name_put

        modify a stored user firmware  # noqa: E501
        """
        pass

    def test_firmwares_post(self):
        """Test case for firmwares_post

        save a user firmware  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()