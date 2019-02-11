import pprint

from iotlabclient.api import Api
from iotlabclient.client import Circuit, Point

api = Api().mobilities

site = 'lille'

def delete_if_exists(circuit_name):
    try:
        pprint.pprint(api.mobilities.delete_user_mobility(circuit_name))
    except:
        print('OK, circuit already deleted')

# get all circuits

print('all circuits (no param):')
pprint.pprint(api.get_mobilities())

print('all circuits:')
pprint.pprint(api.get_mobilities(type='all'))

print('userdefined circuits:')
pprint.pprint(api.get_mobilities(type='userdefined'))

print('predefined circuits:')
pprint.pprint(api.get_mobilities(type='predefined'))

print('predefined circuits:')
pprint.pprint(api.get_mobilities(type='predefined', site=site))

print('predefined circuit square1:')
pprint.pprint(api.get_mobility('square1'))

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
    points=[ "A", "B", "C", "D" ],
    loop= True,
    site=site
)

pprint.pprint(api.save_user_mobility(circuit=circuit))

# POST with the same circuit should fail
try:
    result = api.save_user_mobility(circuit=circuit)
except Exception as e:
    assert e.status == 500

print('remove point B in my_circuit')

del circuit.coordinates['B']
circuit.points.remove('B')

print('userdefined circuit my_circuit on devlille:')
pprint.pprint(api.modify_user_mobility('mobilities/circuits/my_circuit', method='get'))

try:
    api.method('mobilities/circuits/my_circuit', method='put', json=circuit)
except Exception as e:
    print(e)

print('userdefined circuit my_circuit on devlille:')
pprint.pprint(api.get_mobility('my_circuit'))

# rename my_circuit
circuit.name = 'modified_my_circuit'

try:
    api.modify_user_mobility(circuit=circuit)
except Exception as e:
    print(e)

print('userdefined circuit modified_my_circuit:')
pprint.pprint(api.get_mobility('modified_my_circuit'))

print('userdefined circuits (only modified_my_circuit):')
pprint.pprint(api.get_mobilities(type='USERDEFINED'))


api = Api().robots

print('get map config:')
pprint.pprint(api.get_map_config(site))

print('get dock config:')
pprint.pprint(api.get_dock_config(site))

print('reachable:')
pprint.pprint(api.are_coordinates_reachable(site, request_body={'A': Point(x= 20, y=4)}))


print('original_coordinates:')
point = Point(x=20, y=4)
pprint.pprint(point)

print('to_map_coordinates:')
to_map_coordinates = api.get_map_coordinates(site, point=point)
pprint.pprint(to_map_coordinates)

print('back to_ros_coordinates:')
pprint.pprint(api.get_ros_coordinates(site, to_map_coordinates))
