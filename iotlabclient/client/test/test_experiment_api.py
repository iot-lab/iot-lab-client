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
from iotlabclient.client.api.experiment_api import ExperimentApi  # noqa: E501
from iotlabclient.client.rest import ApiException


class TestExperimentApi(unittest.TestCase):
    """ExperimentApi unit test stubs"""

    def setUp(self):
        self.api = iotlabclient.client.api.experiment_api.ExperimentApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_flash_experiment_nodes(self):
        """Test case for flash_experiment_nodes

        Send experiment nodes flash firmware store command.  # noqa: E501
        """
        pass

    def test_get_experiment(self):
        """Test case for get_experiment

        Returns experiment.  # noqa: E501
        """
        pass

    def test_get_experiment_archive(self):
        """Test case for get_experiment_archive

        Returns experiment archive.  # noqa: E501
        """
        pass

    def test_get_experiment_deployment(self):
        """Test case for get_experiment_deployment

        Returns experiment deployment result.  # noqa: E501
        """
        pass

    def test_get_experiment_nodes(self):
        """Test case for get_experiment_nodes

        Returns experiment nodes list.  # noqa: E501
        """
        pass

    def test_get_experiment_nodes_id(self):
        """Test case for get_experiment_nodes_id

        Returns experiment nodes id list (eg. 1-5+8).  # noqa: E501
        """
        pass

    def test_get_experiment_token(self):
        """Test case for get_experiment_token

        Returns experiment websocket token.  # noqa: E501
        """
        pass

    def test_kill_experiment_scripts(self):
        """Test case for kill_experiment_scripts

        Send frontend SSH kill script command.  # noqa: E501
        """
        pass

    def test_reload_experiment(self):
        """Test case for reload_experiment

        Reload experiment.  # noqa: E501
        """
        pass

    def test_run_experiment_scripts(self):
        """Test case for run_experiment_scripts

        Send frontend SSH run script command  # noqa: E501
        """
        pass

    def test_send_cmd_mobility_robots(self):
        """Test case for send_cmd_mobility_robots

        Send update robots mobility.  # noqa: E501
        """
        pass

    def test_send_cmd_nodes(self):
        """Test case for send_cmd_nodes

        Send experiment nodes command.  # noqa: E501
        """
        pass

    def test_send_cmd_profile_nodes(self):
        """Test case for send_cmd_profile_nodes

        Send experiment nodes update monitoring profile store command.  # noqa: E501
        """
        pass

    def test_send_cmd_robots(self):
        """Test case for send_cmd_robots

        Returns robots status.  # noqa: E501
        """
        pass

    def test_send_cmd_update_nodes(self):
        """Test case for send_cmd_update_nodes

        Send experiment nodes flash firmware command.  # noqa: E501
        """
        pass

    def test_send_load_profile_nodes(self):
        """Test case for send_load_profile_nodes

        Send experiment nodes load monitoring profile command.  # noqa: E501
        """
        pass

    def test_status_experiment_scripts(self):
        """Test case for status_experiment_scripts

        Returns frontend SSH status script.  # noqa: E501
        """
        pass

    def test_stop_experiment(self):
        """Test case for stop_experiment

        Stop experiment  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
