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
import pytest
import six
from pytest import fail

from integration_tests import API, SITE
from integration_tests.utils import wait_until

api = API.experiments


def test_get_experiments():
    experiments = api.get_experiments()

    assert experiments.items

    if SITE.startswith('dev'):
        exp_id = 14187
    else:
        exp_id = 164422
    one_exp = API.experiment.get_experiment(exp_id)
    one_exp_dict = list(six.iteritems(one_exp.to_dict()))

    for exp in experiments.items:
        if exp.id == exp_id:
            print(exp.to_dict())
            print(one_exp.to_dict())
            for item in six.iteritems(exp.to_dict()):
                assert item in one_exp_dict
            return

    fail('expected experiment not found')


@pytest.mark.skip
def test_get_experiments_total():
    # wait for running to be 0, otherwise race issue between the two next steps
    wait_until(lambda: api.get_experiments_total().running == 0,
               interval=0.5,
               timeout=30)
    experiments = api.get_experiments()
    experiments_total = api.get_experiments_total()

    translate = {
        'Stopped': 'terminated',
        'Terminated': 'terminated',
        'Error': 'terminated',
        'Running': 'running',
        'Finishing': 'running',
        'Launching': 'upcoming',
        'Waiting': 'upcoming',
    }

    expected = {v: 0 for v in translate.values()}
    for exp in experiments.items:
        state = translate[exp.state]
        expected.setdefault(state, 0)
        expected[state] += 1

    assert expected == experiments_total.to_dict()
