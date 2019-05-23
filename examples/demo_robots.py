from integration_tests.utils import wait_until
from iotlabclient.api import Api
from iotlabclient.auth import get_user_credentials
from iotlabclient.client import Configuration, ExperimentPhysical, FirmwareAssociation, MobilityAssociation

configuration = Configuration()
configuration.username, configuration.password = get_user_credentials()
configuration.host = 'https://www.iot-lab.info/api'

api = Api(configuration=configuration)

api.users.get_user()

robots = [
    'm3-257.lille.iot-lab.info',
    'm3-258.lille.iot-lab.info',
    'm3-259.lille.iot-lab.info'
]

mobilities = {}
for mobility in api.circuit_mobilities.get_mobilities().items:
    mobilities.setdefault(mobility.site, [])
    mobilities[mobility.site].append(mobility)


exp = api.experiments.submit_experiment(experiment=ExperimentPhysical(
    duration=20,
    nodes=robots,
    firmwareassociations=[
        FirmwareAssociation(
            nodes=robots,
            firmwarename='iotlab_m3_tutorial'
        )
    ],
    mobilities=mobilities,
    mobilityassociations=[
        MobilityAssociation(mobilityname='square1', nodes=[robots[0]]),
        MobilityAssociation(mobilityname='square2', nodes=[robots[1]]),
        MobilityAssociation(mobilityname='square3', nodes=[robots[2]]),
    ]
))
exp_id = exp.id

wait_until(
        lambda: api.experiment.get_experiment(exp_id).state == 'Running',
        interval=1,
        timeout=30
    )

api.experiment.send_cmd_mobility_robots(id=exp_id, name='square1', request_body=[robots[0]])
api.experiment.send_cmd_mobility_robots(id=exp_id, name='square2', request_body=[robots[1]])
api.experiment.send_cmd_mobility_robots(id=exp_id, name='square3', request_body=[robots[2]])

