import pprint

from iotlabclient.api import Api
from iotlabclient.client import Point

site = 'devlille'

api = Api().robots

print('get map config:')
pprint.pprint(api.get_map_config(site))

print('get dock config:')
pprint.pprint(api.get_dock_config(site).items)

print('reachable:')
pprint.pprint(api.are_coordinates_reachable(site, request_body={'A': Point(x=20, y=4)}))

print('original_coordinates:')
point = Point(theta=1, x=20, y=4)
pprint.pprint(point)

print('to_map_coordinates:')
to_map_coordinates = api.get_map_coordinates(site, point=point)
pprint.pprint(to_map_coordinates)

print('back to_ros_coordinates:')
pprint.pprint(api.get_ros_coordinates(site, point=to_map_coordinates))
