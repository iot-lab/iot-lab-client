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
import os
import uuid

import pytest
import urllib3

from integration_tests import API
from integration_tests.utils import files_match
from iotlabclient.client import ResourceType, Model
from iotlabclient.client.rest import ApiException

urllib3.add_stderr_logger()

api = API.model_mobilities
cur_dir = os.path.dirname(__file__)
models_dir = os.path.join(cur_dir, 'models')

"""
endpoints:

[**delete_user_model_mobility**](ModelMobilitiesApi.md#delete_user_model_mobility)
[**get_model_mobilities**](ModelMobilitiesApi.md#get_model_mobilities)
[**get_model_mobility**](ModelMobilitiesApi.md#get_model_mobility)
[**get_model_mobility_script**](ModelMobilitiesApi.md#get_model_mobility_script)
[**modify_user_model_mobility**](ModelMobilitiesApi.md#modify_user_model_mobility)
[**save_user_model_mobility**](ModelMobilitiesApi.md#save_user_model_mobility)
"""


def test_all_models():
    data = api.get_model_mobilities()

    assert data.items

    assert len(data.items) > 0


def test_all_models_filtered():
    data = dict(
        all=api.get_model_mobilities(),

        all1=api.get_model_mobilities(
            type=ResourceType.ALL),

        userdefined=api.get_model_mobilities(
            type=ResourceType.USERDEFINED),

        predefined=api.get_model_mobilities(
            type=ResourceType.PREDEFINED),
    )

    for v in data.values():
        assert v.items

    # no difference with or without ALL
    assert data['all'] == data['all1']


def test_random():
    random = api.get_model_mobility('random')

    assert random is not None

    assert random.to_dict() == {
        'name': 'random',
        'script': 'random_move.py',
        'type': 'predefined'
    }


@pytest.fixture
def saved_model():
    model = Model(
        name='%032x' % uuid.uuid4().int,  # unique name
        script='script.py'
    )

    saved = api.save_user_model_mobility(
        model=model,
        script=os.path.join(models_dir, 'script.py')
    )

    model.type = 'userdefined'

    assert model.to_dict() == saved.to_dict()

    yield saved

    api.delete_user_model_mobility(name=saved.name)

    try:
        api.get_model_mobility(name=saved)
    except ApiException as e:
        assert e.status == 500


@pytest.mark.dependency()
def test_save(saved_model):
    # GET on should get us the same

    get = api.get_model_mobility(name=saved_model.name)
    assert saved_model.to_dict() == get.to_dict()

    # POST with the same should fail
    try:
        api.save_user_model_mobility(
            model=saved_model,
            script=os.path.join(models_dir, 'script.py')
        )
    except ApiException as e:
        assert e.status == 500


@pytest.mark.dependency(depends=["test_save"])
def test_modify_script_different_name(saved_model):
    saved_model.script = 'new_script.py'

    new_script = os.path.join(cur_dir, 'models', 'new_script.py')

    api.modify_user_model_mobility(
        name=saved_model.name,
        model=saved_model,
        script=new_script
    )

    modified_model = api.get_model_mobility(name=saved_model.name)
    assert modified_model.to_dict() == saved_model.to_dict()

    modified_script = api.get_model_mobility_script(name=saved_model.name)

    files_match(new_script, modified_script)


@pytest.mark.dependency(depends=["test_save"])
def test_modify_script_same_name(saved_model):
    new_script = os.path.join(cur_dir, 'models', 'change', 'script.py')

    api.modify_user_model_mobility(
        name=saved_model.name,
        model=saved_model,
        script=new_script
    )

    modified_model = api.get_model_mobility(name=saved_model.name)
    assert modified_model.to_dict() == saved_model.to_dict()

    modified_script = api.get_model_mobility_script(name=saved_model.name)

    files_match(new_script, modified_script)


@pytest.mark.dependency(depends=["test_save"])
def test_rename(saved_model):

    # rename
    old_name = saved_model.name
    saved_model.name = saved_model.name + '_modified'

    api.modify_user_model_mobility(
        name=old_name,
        model=saved_model,
        script=os.path.join(models_dir, 'script.py')
    )

    try:
        api.get_model_mobility(name=old_name)
    except ApiException as e:
        assert e.status == 500

    get = api.get_model_mobility(name=saved_model.name)
    assert saved_model.to_dict() == get.to_dict()
