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
from iotlabclient.client.api.sites_api import SitesApi  # noqa: E501
from iotlabclient.client.rest import ApiException


class TestSitesApi(unittest.TestCase):
    """SitesApi unit test stubs"""

    def setUp(self):
        self.api = iotlabclient.client.api.sites_api.SitesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_sites(self):
        """Test case for get_sites

        Returns testbed sites list.  # noqa: E501
        """
        pass

    def test_get_sites_details(self):
        """Test case for get_sites_details

        Returns tesbed sites details list.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
