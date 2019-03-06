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

from paramiko import SSHClient

from integration_tests import API, WSN430_SITE
from integration_tests.utils import wait_until
from iotlabclient.client import (ExperimentAlias, AliasProperties,
                                 Alias, ArchiRadioString)
from iotlabclient.client import FirmwareAliasAssociation

cur_dir = os.path.dirname(__file__)


def test_wsn430():
    """
    runs
    https://www.iot-lab.info/tutorials/submit-experiment-wsn430-web/
    """
    experiment = ExperimentAlias(
        duration=10,
        name="test_client_tutorial_wsn430",
        nodes=[
            Alias(
                alias='1',
                nbnodes=2,
                properties=AliasProperties(
                    archi=ArchiRadioString.WSN430_CC1101,
                    site=WSN430_SITE,
                    mobile=False)
            )
        ],
        firmwareassociations=[
            FirmwareAliasAssociation(
                firmwarename='tutorial_cc1101.hex',
                nodes=['1']
            ),
        ])

    submitted = API.experiments.submit_experiment(
        experiment=experiment,
        files=[os.path.join(cur_dir, 'tutorial_cc1101.hex')])

    exp_id = submitted.id

    wait_until(lambda: API.experiment.get_experiment(exp_id).state == 'Running', interval=1, timeout=30)

    deployment = API.experiment.get_experiment_deployment(exp_id)

    assert deployment._1 is None

    assert submitted

    user = API.users.get_user()

    experiment = API.experiment.get_experiment(exp_id)

    node0 = experiment.nodes[0]

    client, stdin, stdout, stderr = node_connect(user, WSN430_SITE, node0)

    lines = []
    while True:
        line = stdout.readline().rstrip()
        print('> ' + line)
        lines.append(line)
        if 'Type Enter to stop printing this help' in line:
            break

    client.close()

    expected = """IoT-LAB Simple Demo program
Type command
\th:	print this help
\tt:	temperature measure
\tl:	luminosity measure
\ts:	send a radio packet

 Type Enter to stop printing this help"""

    assert expected in '\n'.join(lines)


def node_connect(user, site, node):
    site_tld = '%s.iot-lab.info' % site
    client = SSHClient()
    client.load_system_host_keys()
    client.connect(site_tld, username=user.login)

    stdin, stdout, stderr = client.exec_command('nc %s 20000' % node)
    return client, stdin, stdout, stderr
