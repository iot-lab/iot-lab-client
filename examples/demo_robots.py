from iotlabclient.api import Api
from iotlabclient.auth import get_user_credentials
from iotlabclient.client import Configuration, ExperimentPhysical, FirmwareAssociation, MobilityAssociation

configuration = Configuration()
configuration.username, configuration.password = get_user_credentials()
configuration.host = 'https://www.iot-lab.info/api'

devconfiguration = Configuration()
devconfiguration.username, configuration.password = get_user_credentials()
devconfiguration.host = 'https://www.iot-lab.info/api'

api = Api(configuration=configuration)
devapi = Api(configuration=devconfiguration)

api.users.get_user()
devapi.users.get_user()

robots = [
    'm3-257.lille.iot-lab.info',
    'm3-258.lille.iot-lab.info',
    'm3-259.lille.iot-lab.info'
]

devrobots = [
    'm3-201.devlille.iot-lab.info',
    'm3-202.devlille.iot-lab.info',
    'm3-203.devlille.iot-lab.info',
    'm3-204.devlille.iot-lab.info',
    'm3-205.devlille.iot-lab.info',
]

mobilities = {}
for mobility in api.circuit_mobilities.get_mobilities().items:
    mobilities.setdefault(mobility.site, [])
    mobilities[mobility.site].append(mobility)

devmobilities = {}
for mobility in devapi.circuit_mobilities.get_mobilities().items:
    devmobilities.setdefault(mobility.site, [])
    devmobilities[mobility.site].append(mobility)

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


api.experiment.send_cmd_mobility_robots(id=exp_id, name='square1', request_body=[robots[0]])
api.experiment.send_cmd_mobility_robots(id=exp_id, name='square2', request_body=[robots[1]])
api.experiment.send_cmd_mobility_robots(id=exp_id, name='square3', request_body=[robots[2]])

dev_exp = devapi.experiments.submit_experiment(experiment=ExperimentPhysical(
    duration=20,
    nodes=robots,
    firmwareassociations=[
        FirmwareAssociation(
            nodes=robots,
            firmwarename='iotlab_m3_tutorial'
        )
    ],
    mobilities=devmobilities,
    mobilityassociations=[
        MobilityAssociation(mobilityname='square1', nodes=[robots[0]]),
        MobilityAssociation(mobilityname='square2', nodes=[robots[1]]),
        MobilityAssociation(mobilityname='square3', nodes=[robots[2]]),
    ]
))
