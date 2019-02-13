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
from pprint import pprint
import re

from iotlabclient.client.rest import ApiException

from iotlabclient.api import Api
from iotlabclient.client import Circuit, Point, ResourceType

api = Api().mobilities

site = 'devlille'


def delete_if_exists(circuit_name):
    try:
        api.delete_user_mobility(circuit_name)
    except ApiException as e:
        print('OK, circuit already deleted')
        msg = json.loads(e.body)['message']
        if not re.match(r"The circuit .* doesn\'t exist", msg):
            raise


# get all circuits

print('all circuits (no param):')
pprint(api.get_mobilities())

print('all circuits:')
pprint(api.get_mobilities(type=ResourceType.ALL))

print('userdefined circuits:')
pprint(api.get_mobilities(type=ResourceType.USERDEFINED))

print('predefined circuits:')
pprint(api.get_mobilities(type=ResourceType.PREDEFINED))

print('predefined circuits:')
pprint(api.get_mobilities(type=ResourceType.PREDEFINED, site=site))

print('predefined circuit square1:')
pprint(api.get_mobility('square1'))

print('add my_circuit user defined circuit:')
delete_if_exists('my_circuit')
delete_if_exists('modified_my_circuit')

circuit = Circuit(
    name="my_circuit",
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
    site=site
)

pprint(api.save_user_mobility(circuit=circuit))

# POST with the same circuit should fail
try:
    result = api.save_user_mobility(circuit=circuit)
except ApiException as e:
    assert e.status == 500

print('userdefined circuit my_circuit on devlille:')
pprint(api.modify_user_mobility('my_circuit', circuit=circuit))


print('remove point B in my_circuit')

del circuit.coordinates['B']
circuit.points.remove('B')

# modify my_circuit
api.modify_user_mobility('my_circuit', circuit=circuit)

print('userdefined circuit my_circuit on devlille:')
pprint(api.get_mobility('my_circuit'))

# rename my_circuit
circuit.name = 'modified_my_circuit'

try:
    api.modify_user_mobility(name='my_circuit', circuit=circuit)
except ApiException as e:
    print(e)

print('userdefined circuit modified_my_circuit:')
pprint(api.get_mobility('modified_my_circuit'))

print('userdefined circuits (only modified_my_circuit):')
pprint(api.get_mobilities(type=ResourceType.USERDEFINED))
