import time

from integration_tests.utils import wait_until
from iotlabclient.api import Api
from iotlabclient.auth import get_user_credentials
from iotlabclient.client import Configuration, ExperimentPhysical, FirmwareAssociation, MobilityAssociation, \
    MobilityAssociations

PLATFORM = 'dev'

configs = {
    'dev': {
        'host': 'https://devwww.iot-lab.info/api',
        'robots':  [
            'm3-201.devlille.iot-lab.info',
            'm3-203.devlille.iot-lab.info'
        ]
    },
    'prod': {
        'host': 'https://www.iot-lab.info/api',
        'robots': [
            'm3-257.lille.iot-lab.info',
            'm3-258.lille.iot-lab.info',
        ]
    }
}
cfg = configs[PLATFORM]

configuration = Configuration()
configuration.username, configuration.password = get_user_credentials()
configuration.host = cfg['host']

api = Api(configuration=configuration)

api.users.get_user()
exps = api.experiments.get_running_experiments().items

exp = None

for _exp in exps:
    if _exp.name == 'demo_robots':
        exp = _exp
        break

robots = cfg['robots']

if exp is None:

    mobilities = {}
    for mobility in api.circuit_mobilities.get_mobilities().items:
        mobilities.setdefault(mobility.site, [])
        mobilities[mobility.site].append(mobility)

    exp = api.experiments.submit_experiment(experiment=ExperimentPhysical(
        name='demo_robots',
        duration=20,
        nodes=robots,
        firmwareassociations=[
            FirmwareAssociation(
                nodes=robots,
                firmwarename='simple_robot.elf'
            )
        ],
        mobilities=mobilities,
        associations=MobilityAssociations(
            mobility=[
                MobilityAssociation(mobilityname='square1', nodes=[robots[0]]),
                MobilityAssociation(mobilityname='square2', nodes=[robots[1]]),
            ]
        )), files=['simple_robot.elf'])

exp_id = exp.id

wait_until(
        lambda: api.experiment.get_experiment(exp_id).state == 'Running',
        interval=1,
        timeout=30
    )

print(api.experiment.send_cmd_mobility_robots(id=exp_id, name='square1', nodes=[robots[0]]))
print(api.experiment.send_cmd_mobility_robots(id=exp_id, name='square2', nodes=[robots[1]]))

time.sleep(45)

print(api.experiment.send_cmd_mobility_robots(id=exp_id, name='random', nodes=robots))

time.sleep(60)

print(api.experiment.send_cmd_mobility_robots(id=exp_id, name='square1', nodes=[robots[0]]))
print(api.experiment.send_cmd_mobility_robots(id=exp_id, name='square2', nodes=[robots[1]]))

time.sleep(60)

api.experiment.stop_experiment(id=exp_id)
