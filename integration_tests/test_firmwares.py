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
import hashlib
import os
import uuid

import pytest

from integration_tests import API
from iotlabclient.client import ResourceType, Firmware
from iotlabclient.client.rest import ApiException

api = API.firmwares
cur_dir = os.path.dirname(__file__)


def test_get_firmwares():
    data = api.get_firmwares()

    assert data

    assert len(data) > 0


def test_get_filtered_firmwares():
    data = dict(
        all=api.get_firmwares(),

        all1=api.get_firmwares(
            type=ResourceType.ALL),

        userdefined=api.get_firmwares(
            type=ResourceType.USERDEFINED),

        predefined=api.get_firmwares(
            type=ResourceType.PREDEFINED),
    )

    for v in data.values():
        assert v


def test_get_firmware_():
    firmware = api.get_firmware('iotlab_m3_tutorial')

    assert firmware.to_dict() == dict(
        name='iotlab_m3_tutorial',
        description='Basic tutorial which provides read sensors, send radio packet and so on',  # noqa: E501
        filename='tutorial_m3.elf', archi='m3', type=None)


def files_match(f1, f2):
    with open(f1, 'rb') as file1, \
            open(f2, 'rb') as file2:
        hash1 = hashlib.md5(file1.read()).hexdigest()
        hash2 = hashlib.md5(file2.read()).hexdigest()
        assert hash1 == hash2


def test_get_firmware_file():
    firmware_path = api.get_firmware_file('iotlab_m3_tutorial')

    files_match(os.path.join(cur_dir, 'tutorial_m3.elf'), firmware_path)


@pytest.fixture
def saved_firmware():
    firmware = Firmware(
        name='%032x' % uuid.uuid4().int,  # unique name
        description='a super test firmware',
        filename='tutorial_m3.elf',
        archi='m3',
    )

    saved = api.save_firmware(
        firmware=os.path.join(cur_dir, 'tutorial_m3.elf'),
        metadata=firmware
    )

    firmware.type = 'userdefined'

    assert firmware.to_dict() == saved.to_dict()

    yield saved

    api.delete_firmware(name=saved.name)

    try:
        api.get_firmware(name=saved.name)
    except ApiException as e:
        assert e.status == 500


@pytest.mark.dependency()
def test_save(saved_firmware):
    # GET on the firmware should get us the same

    get = api.get_firmware(name=saved_firmware.name)
    assert saved_firmware.to_dict() == get.to_dict()

    # POST with the same firmware should fail
    try:
        api.save_firmware(
            metadata=saved_firmware,
            firmware=os.path.join(cur_dir, 'tutorial_m3.elf')
        )
    except ApiException as e:
        assert e.status == 500


def test_save_wrong_file():
    # POST with no firmware file should fail
    firmware = Firmware(
        name='%032x' % uuid.uuid4().int,  # unique name
        description='a super test firmware',
        filename='tutorial_m3.elf',
        archi='m3',
    )

    try:
        api.save_firmware(
            metadata=firmware
        )
    except ApiException as e:
        assert e.status == 500


def test_save_no_metadata():
    # POST with no firmware metadata should fail

    try:
        api.save_firmware(
            firmware=os.path.join(cur_dir, 'tutorial_m3.elf')
        )
    except ApiException as e:
        assert e.status == 500


@pytest.mark.dependency(depends=["test_save"])
def test_modify_metadata(saved_firmware):
    saved_firmware.description = 'a new description'
    saved_firmware.archi = 'firefly'

    # modify
    api.modify_firmware(
        name=saved_firmware.name,
        metadata=saved_firmware,
        firmware=os.path.join(cur_dir, 'tutorial_m3.elf')
    )

    get = api.get_firmware(name=saved_firmware.name)
    assert saved_firmware.to_dict() == get.to_dict()

    get = api.get_firmware_file(name=saved_firmware.name)
    files_match(os.path.join(cur_dir, 'tutorial_m3.elf'), get)


@pytest.mark.dependency(depends=["test_save"])
def test_rename(saved_firmware):

    # rename
    old_name = saved_firmware.name
    saved_firmware.name = saved_firmware.name + '_modified'

    api.modify_firmware(
        name=old_name,
        metadata=saved_firmware,
        firmware=os.path.join(cur_dir, 'tutorial_m3.elf')
    )

    try:
        api.get_firmware(name=old_name)
    except ApiException as e:
        assert e.status == 500

    get = api.get_firmware(name=saved_firmware.name)
    assert saved_firmware.to_dict() == get.to_dict()

    get = api.get_firmware_file(name=saved_firmware.name)
    files_match(os.path.join(cur_dir, 'tutorial_m3.elf'), get)
