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
import json
import os
import tarfile
import time
from uuid import UUID

import pytest
from pytest import fail

from integration_tests import SITE, SITE_TLD, API
from iotlabclient.client import (ExperimentAlias, AliasProperties,
                                 FirmwareAliasAssociation, Alias,
                                 ScriptAssociations, ScriptAssociationsScript,
                                 ScriptAssociationsScriptconfig,
                                 Profile, ProfileConsumption,
                                 ProfileRadio, rest)

api = API.experiment
experiments = API.experiments

cur_dir = os.path.dirname(__file__)


"""
endpoints:

[**get_experiment**](ExperimentApi.md#get_experiment)
[**flash_experiment_nodes**](ExperimentApi.md#flash_experiment_nodes)
[**get_experiment_token**](ExperimentApi.md#get_experiment_token)
[**get_experiment_archive**](ExperimentApi.md#get_experiment_archive)
[**send_cmd_nodes**](ExperimentApi.md#send_cmd_nodes)
[**get_experiment_deployment**](ExperimentApi.md#get_experiment_deployment)
[**get_experiment_nodes**](ExperimentApi.md#get_experiment_nodes)
[**get_experiment_nodes_id**](ExperimentApi.md#get_experiment_nodes_id)
[**run_experiment_scripts**](ExperimentApi.md#run_experiment_scripts)
[**kill_experiment_scripts**](ExperimentApi.md#kill_experiment_scripts)
[**status_experiment_scripts**](ExperimentApi.md#status_experiment_scripts)
[**send_cmd_update_nodes**](ExperimentApi.md#send_cmd_update_nodes)
[**send_cmd_profile_nodes**](ExperimentApi.md#send_cmd_profile_nodes)
[**send_load_profile_nodes**](ExperimentApi.md#send_load_profile_nodes)


[**reload_experiment**](ExperimentApi.md#reload_experiment)

[**send_cmd_robots**](ExperimentApi.md#send_cmd_robots)
[**send_cmd_mobility_robots**](ExperimentApi.md#send_cmd_mobility_robots)

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


EXPERIMENT = ExperimentAlias(
    duration=10,
    name="test_client",
    nodes=[
        Alias(
            alias='1',
            nbnodes=1,
            properties=AliasProperties(
                archi="m3:at86rf231",
                site=SITE,
                mobile=False)
        )
    ],
    firmwareassociations=[
        FirmwareAliasAssociation(
            firmwarename='iotlab_m3_tutorial',
            nodes=['1']
        ),
    ])


def stop_experiment(exp):
    result = api.stop_experiment(exp.id)
    print('stop exp')
    expected = dict(id=exp.id,
                    status='Delete request registered')
    assert expected == result.to_dict()


def start_experiment(exp):
    data = experiments.submit_experiment(experiment=exp)

    while True:
        exp = api.get_experiment(data.id)
        print(exp.state)
        if exp.state == 'Running':
            return exp
        time.sleep(1)


@pytest.fixture(scope='module')
def running_experiment():
    running_experiments = experiments.get_running_experiments().items

    exp = None
    if len(running_experiments) > 0:
        for running in running_experiments:
            if running.name == 'test_client':
                exp = api.get_experiment(running.id)
                break

    if exp is None:
        exp = start_experiment(EXPERIMENT)

    yield exp
    stop_experiment(exp)


@pytest.fixture
def experiment_id(running_experiment):
    return running_experiment.id


@pytest.fixture
def experiment_nodes(running_experiment):
    return running_experiment.nodes


def assert_ok(result, nodes):
    assert result.to_dict() == {'_0': nodes, '_1': None}


def assert_nok(result, nodes):
    assert result.to_dict() == {'_1': nodes, '_0': None}


def test_flash_experiment_nodes_w_store(experiment_id, experiment_nodes):
    result = api.flash_experiment_nodes(
        experiment_id,
        nodes=experiment_nodes,
        name='iotlab_m3_tutorial'
    )

    assert_ok(result, experiment_nodes)


def test_flash_experiment_nodes_local(experiment_id, experiment_nodes):
    result = api.send_cmd_update_nodes(
        experiment_id,
        firmware=os.path.join(cur_dir, 'tutorial_m3.elf'),
        nodes=experiment_nodes
    )

    assert_ok(result, experiment_nodes)


@pytest.mark.parametrize('command', [
    'start',
    'stop',
    'reset',
    'update-idle',
    'profile-reset',
])
def test_commands(command, experiment_id, experiment_nodes):
    result = api.send_cmd_nodes(
        experiment_id,
        command,
        nodes=experiment_nodes
    )
    assert_ok(result, experiment_nodes)


def test_command_debug_start_stop(experiment_id, experiment_nodes):
    result = api.send_cmd_nodes(
        experiment_id,
        'debug-start',
        nodes=experiment_nodes
    )
    assert_ok(result, experiment_nodes)

    result = api.send_cmd_nodes(
        experiment_id,
        'debug-stop',
        nodes=experiment_nodes
    )
    assert_ok(result, experiment_nodes)


def test_get_token(experiment_id):
    result = api.get_experiment_token(experiment_id)
    assert result.token is not None
    try:
        UUID(result.token)
    except ValueError:
        fail('the experiment token is not an UUID')


def test_get_archive(experiment_id, experiment_nodes):
    archive = api.get_experiment_archive(experiment_id)

    files = tarfile.open(archive)
    members = {m.path: m for m in files.members}

    log_file = '{0}/{0}.log'.format(experiment_id)
    assert log_file in members

    experiment_log = members[log_file]

    extracted = files.extractfile(experiment_log)
    experiment_log_content = extracted.read().decode('utf-8')

    json_data = json.loads(experiment_log_content)
    assert json_data == {'0': experiment_nodes}


def test_get_deployment(experiment_id, experiment_nodes):
    deployment = api.get_experiment_deployment(experiment_id)

    assert deployment.to_dict() == {'_0': experiment_nodes, '_1': None}


def test_get_experiment_nodes(experiment_id, experiment_nodes):
    response = api.get_experiment_nodes(experiment_id).items

    assert [node.network_address for node in response] == experiment_nodes


def test_run_experiment_script(experiment_id):
    scriptname = 'aggregator_script'
    scriptconfigname = 'aggregator_script_config'

    status = api.status_experiment_scripts(experiment_id, sites=[SITE])

    result = api.run_experiment_scripts(
        experiment_id,
        script=os.path.join(cur_dir, scriptname),
        scriptconfig=os.path.join(cur_dir, scriptconfigname),
        scriptassociation=ScriptAssociations(
            script=[ScriptAssociationsScript(
                scriptname=scriptname,
                sites=[SITE]
            )],
            scriptconfig=[ScriptAssociationsScriptconfig(
                scriptconfigname=scriptconfigname,
                sites=[SITE]
            )]
        )
    )

    assert result.to_dict() == {'_0': [SITE_TLD], '_1': None}

    time.sleep(0.5)

    status = api.status_experiment_scripts(experiment_id, sites=[SITE])

    # assert status.to_dict() == {'_0': {SITE_TLD: 'Running'}}


def test_load_profile_nodes(experiment_id, experiment_nodes):
    profile = Profile(
        profilename='profile',
        nodearch='m3',
        power='dc',
        consumption=ProfileConsumption(
            power=True,
            current=False,
            voltage=False,
            period=2116,
            average=1
        ),
        radio=ProfileRadio(
            mode='rssi',
            num_per_channel=0,
            period=1000,
            channels=[11]

        )

    )
    result = api.send_load_profile_nodes(
        experiment_id,
        profile=profile,
        nodes=experiment_nodes
    )
    assert_ok(result, experiment_nodes)


def test_send_cmd_profile_nodes(experiment_id, experiment_nodes):
    result = api.send_cmd_profile_nodes(
        experiment_id,
        name='test_profile',
        nodes=experiment_nodes
    )
    assert_ok(result, experiment_nodes)

    try:
        result = api.send_cmd_profile_nodes(
            experiment_id,
            name='this profile doesn\'t exist in the store',
            nodes=experiment_nodes
        )
    except rest.ApiException as e:
        assert e.status == 400


def wait_until(callable, interval=0.1, timeout=1):
    start = time.time()
    while not callable() and time.time() - start < timeout:
        time.sleep(interval)


def test_stop_experiment():
    exp = start_experiment(EXPERIMENT)

    result = api.stop_experiment(exp.id)

    expected = dict(id=exp.id, status='Delete request registered')
    assert result.to_dict() == expected

    wait_until(lambda: api.get_experiment(exp.id).state == 'Stopped',
               interval=0.5, timeout=20)
