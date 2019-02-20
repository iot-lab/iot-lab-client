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
import random

import pytest
from PIL import Image

from integration_tests import ROBOT_SITE, API
from iotlabclient.client import Point

api = API.robots


@pytest.fixture
def map_image():
    image_path = api.get_map_image(ROBOT_SITE)
    return Image.open(image_path)


@pytest.fixture
def map_config():
    return api.get_map_config(ROBOT_SITE)


def test_get_map_config(map_config):
    assert map_config.origin
    assert map_config.resolution
    assert map_config.image
    assert ROBOT_SITE in map_config.image


def test_get_map_image(map_image, map_config):
    # should be a png
    assert map_image.format == 'PNG'


def test_get_dock_config(map_config):
    dock_configs = api.get_dock_config(ROBOT_SITE).items

    assert dock_configs

    for dock_config in dock_configs:
        assert dock_config.robot
        assert dock_config.site == ROBOT_SITE
        assert dock_config.config
        assert dock_config.config.frame_id
        assert dock_config.config.theta
        assert dock_config.config.x
        assert dock_config.config.y

    nodes = API.nodes.get_nodes().items
    assert nodes

    # dock config should match the declared mobile nodes

    robots = [n for n in nodes
              if n.mobile == 1 and
              n.site == ROBOT_SITE and
              n.mobility_type == 'turtlebot2']
    assert len(dock_configs) == len(robots)

    dock_config_map = {config.robot: config for config in dock_configs}
    for robot in robots:
        short = robot.network_address.split('.')[0]
        expected = 'turtlebot2_' + '_'.join(short.split('-'))

        assert expected in dock_config_map


def test_reachable(map_image):
    datas = map_image.getdata()
    w, h = map_image.size

    white_pixels = []
    for y in range(h):
        for x in range(w):
            c = map_image.getpixel((x, y))
            if c >= 254:
                white_pixels.append((x, y))

    some = random.sample(white_pixels, 5)

    points = {str((x, y)): api.get_ros_coordinates(
        ROBOT_SITE,
        point=Point(x=x, y=y, theta=0)) for x, y in some}

    reachable = api.are_coordinates_reachable(ROBOT_SITE, points=points)

    assert reachable.items

    reachable = reachable.items

    assert all(item.reachable for item in reachable)

    assert {item.point_name for item in reachable} == set(points.keys())


def assert_eqeps(v1, v2):
    assert abs(v1 - v2) / max(v1, v2) < 1e-5


def test_roundtrip_map_coordinates():
    point = Point(theta=1, x=20, y=4)

    roundtrip1 = api.get_ros_coordinates(
        ROBOT_SITE,
        point=api.get_map_coordinates(ROBOT_SITE, point=point))

    assert_eqeps(roundtrip1.x, point.x)
    assert_eqeps(roundtrip1.y, point.y)
    assert_eqeps(roundtrip1.theta, point.theta)

    roundtrip2 = api.get_map_coordinates(
        ROBOT_SITE,
        point=api.get_ros_coordinates(ROBOT_SITE, point=point))

    assert_eqeps(roundtrip2.x, point.x)
    assert_eqeps(roundtrip2.y, point.y)
    assert_eqeps(roundtrip2.theta, point.theta)


def test_values_to_map_coordinates(map_config, map_image):
    width, height = map_image.size
    point = Point(theta=1, x=20, y=4)

    value = api.get_map_coordinates(ROBOT_SITE, point=point)

    origin = map_config.origin
    resolution = map_config.resolution

    expected_x = (point.x - origin[0]) / resolution
    expected_y = height - (point.y - origin[1]) / resolution
    expected_theta = point.theta

    assert_eqeps(expected_x, value.x)
    assert_eqeps(expected_y, value.y)
    assert_eqeps(expected_theta, value.theta)


def test_values_to_ros_coordinates(map_config, map_image):
    width, height = map_image.size
    point = Point(theta=1, x=20, y=20)

    value = api.get_ros_coordinates(ROBOT_SITE, point=point)

    origin = map_config.origin
    resolution = map_config.resolution

    expected_x = origin[0] + point.x * resolution
    expected_y = origin[1] + (height - point.y) * resolution
    expected_theta = point.theta

    assert_eqeps(expected_x, value.x)
    assert_eqeps(expected_y, value.y)
    assert_eqeps(expected_theta, value.theta)
