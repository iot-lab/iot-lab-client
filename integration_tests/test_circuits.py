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
import uuid

import pytest

from integration_tests import API
from iotlabclient.client import Circuit, ResourceType
from iotlabclient.client.rest import ApiException

api = API.circuit_mobilities
sites = API.sites.get_sites()

site = next(item.site for item in sites.items if 'lille' in item.site)

"""
endpoints:

[**delete_user_mobility**](MobilitiesApi.md#delete_user_mobility)
[**get_mobilities**](MobilitiesApi.md#get_mobilities)
[**get_mobility**](MobilitiesApi.md#get_mobility)
[**modify_user_mobility**](MobilitiesApi.md#modify_user_mobility)
[**save_user_mobility**](MobilitiesApi.md#save_user_mobility)
"""


def test_all_circuits():
    data = api.get_mobilities()

    assert data.items

    assert len(data.items) > 0


def test_all_circuits_filtered():
    data = dict(
        all=api.get_mobilities(),
        all_site=api.get_mobilities(site=site),

        all1=api.get_mobilities(
            type=ResourceType.ALL),
        all1_site=api.get_mobilities(
            type=ResourceType.ALL, site=site),

        userdefined=api.get_mobilities(
            type=ResourceType.USERDEFINED),
        userdefined_site=api.get_mobilities(
            type=ResourceType.USERDEFINED, site=site),

        predefined=api.get_mobilities(
            type=ResourceType.PREDEFINED),
        predefined_site=api.get_mobilities(
            type=ResourceType.PREDEFINED, site=site),
    )

    for v in data.values():
        assert v.items

    # no difference with or without ALL
    assert data['all'] == data['all1']
    assert data['all_site'] == data['all1_site']


def test_square1():
    square1 = api.get_mobility('square1')

    assert square1 is not None

    assert square1.to_dict() == {
        'coordinates':
            {'A': {'x': 19.0, 'y': 2.0, 'theta': 1.57},
             'B': {'x': 19.0, 'y': 5.0, 'theta': 0.0},
             'C': {'x': 22.0, 'y': 5.0, 'theta': -1.57},
             'D': {'x': 22.0, 'y': 2.0, 'theta': 3.14}},
        'loop': True,
        'name': 'square1',
        'site': site,
        'type': 'predefined',
        'points': ['A', 'B', 'C', 'D']
    }


@pytest.fixture
def saved_circuit():
    circuit = Circuit(
        coordinates={
            "A": {
                "theta": 1.57,
                "x": 22,
                "y": 7
            },
            "B": {
                "theta": 0,
                "x": 24,
                "y": 7
            },
            "C": {
                "theta": -1.57,
                "x": 24,
                "y": 4
            },
            "D": {
                "theta": 3.14,
                "x": 22,
                "y": 4
            }
        },
        points=["A", "B", "C", "D"],
        loop=True,
        site=site,
        name='%032x' % uuid.uuid4().int  # unique circuit name
    )

    saved = api.save_user_mobility(circuit=circuit)

    circuit.type = ResourceType.USERDEFINED

    assert circuit.to_dict() == saved.to_dict()

    yield saved

    api.delete_user_mobility(name=saved.name)

    try:
        api.get_mobility(name=saved)
    except ApiException as e:
        assert e.status == 500


@pytest.mark.dependency()
def test_save(saved_circuit):
    # GET on the circuit should get us the same

    get = api.get_mobility(name=saved_circuit.name)
    assert saved_circuit.to_dict() == get.to_dict()

    # POST with the same circuit should fail
    try:
        api.save_user_mobility(circuit=saved_circuit)
    except ApiException as e:
        assert e.status == 500


@pytest.mark.dependency(depends=["test_save"])
def test_modify(saved_circuit):
    del saved_circuit.coordinates['B']
    saved_circuit.points.remove('B')

    # modify my_circuit
    api.modify_user_mobility(saved_circuit.name, circuit=saved_circuit)

    get = api.get_mobility(name=saved_circuit.name)
    assert saved_circuit.to_dict() == get.to_dict()


@pytest.mark.dependency(depends=["test_save"])
def test_rename(saved_circuit):

    # rename my_circuit
    old_circuit_name = saved_circuit.name
    saved_circuit.name = saved_circuit.name + '_modified'

    api.modify_user_mobility(name=old_circuit_name, circuit=saved_circuit)

    try:
        api.get_mobility(name=old_circuit_name)
    except ApiException as e:
        assert e.status == 500

    get = api.get_mobility(name=saved_circuit.name)
    assert saved_circuit.to_dict() == get.to_dict()

    predefined = api.get_mobilities(type=ResourceType.USERDEFINED).items
    circuits = [c.to_dict() for c in predefined]

    assert saved_circuit.to_dict() in circuits
