# This file is a part of IoT-LAB client
# Copyright (C) 2019 INRIA (Contact: admin@iot-lab.info)
# Contributor(s) : see AUTHORS file
#
# This software is governed by the CeCILL license under French law
# and abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# http://www.cecill.info.
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.

from integration_tests import HOST
from iotlabclient.api import Api

api = Api(host=HOST).experiment

"""
endpoints:

[**get_experiment**](ExperimentApi.md#get_experiment)
[**flash_experiment_nodes**](ExperimentApi.md#flash_experiment_nodes)
[**get_experiment_token**](ExperimentApi.md#get_experiment_token)
[**get_experiment_archive**](ExperimentApi.md#get_experiment_archive)
[**get_experiment_deployment**](ExperimentApi.md#get_experiment_deployment)
[**get_experiment_nodes**](ExperimentApi.md#get_experiment_nodes)
[**get_experiment_nodes_id**](ExperimentApi.md#get_experiment_nodes_id)
[**kill_experiment_scripts**](ExperimentApi.md#kill_experiment_scripts)
[**reload_experiment**](ExperimentApi.md#reload_experiment)
[**run_experiment_scripts**](ExperimentApi.md#run_experiment_scripts)
[**send_cmd_mobility_robots**](ExperimentApi.md#send_cmd_mobility_robots)
[**send_cmd_nodes**](ExperimentApi.md#send_cmd_nodes)
[**send_cmd_profile_nodes**](ExperimentApi.md#send_cmd_profile_nodes)
[**send_cmd_robots**](ExperimentApi.md#send_cmd_robots)
[**send_cmd_update_nodes**](ExperimentApi.md#send_cmd_update_nodes)
[**send_load_profile_nodes**](ExperimentApi.md#send_load_profile_nodes)
[**status_experiment_scripts**](ExperimentApi.md#status_experiment_scripts)
[**stop_experiment**](ExperimentApi.md#stop_experiment)
"""


def test_get():
    experiment_id = 13921
    experiment = api.get_experiment(experiment_id)

    assert experiment.to_dict() == {
        'id': 13921,
        'name': '',
        'type': 'physical',
        'user': 'berthome',
        'nb_nodes': 2,
        'state': 'Stopped',
        'submitted_duration': 20,
        'effective_duration': 5,
        'scheduled_date': '1970-01-01T00:00:00Z',
        'start_date': '2019-02-15T13:34:54Z',
        'stop_date': '2019-02-15T13:40:30Z',
        'submission_date': '2019-02-15T13:34:53Z', 'profiles': None,
        'mobilities': {'mobilityname': None},
        'nodes': [
            'm3-202.devlille.iot-lab.info',
            'm3-203.devlille.iot-lab.info'
        ],
        'duration': None,
        'reservation': None,
        'profileassociations': None,
        'firmwareassociations': None,
        'mobilityassociations': None,
        'siteassociations': None
    }
