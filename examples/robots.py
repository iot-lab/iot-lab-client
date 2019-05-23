
from pprint import pprint

from iotlabclient.api import Api
from iotlabclient.client import Point

site = 'devlille'

api = Api().robots

print('get map config:')
pprint(api.get_map_config(site))

print('get map image:')
pprint(api.get_map_image(site))

print('get dock config:')
pprint(api.get_dock_config(site).items)

print('reachable:')
pprint(api.are_coordinates_reachable(site, request_body={'A': Point(x=20, y=4)}))

print('original_coordinates:')
point = Point(theta=1, x=20, y=4)
pprint(point)

print('to_map_coordinates:')
to_map_coordinates = api.get_map_coordinates(site, point=point)
pprint(to_map_coordinates)

print('back to_ros_coordinates:')
pprint(api.get_ros_coordinates(site, point=to_map_coordinates))
