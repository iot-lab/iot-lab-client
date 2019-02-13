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
