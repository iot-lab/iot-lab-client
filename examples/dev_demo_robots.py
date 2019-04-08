import time

from iotlabclient.api import Api
from iotlabclient.auth import get_user_credentials
from iotlabclient.client import Configuration, ExperimentPhysical, FirmwareAssociation

devconfiguration = Configuration()
devconfiguration.username, devconfiguration.password = get_user_credentials()
devconfiguration.host = 'https://devwww.iot-lab.info/api'

devapi = Api(configuration=devconfiguration)

devapi.users.get_user()

devrobots = [
    # 'm3-201.devlille.iot-lab.info',
    'm3-202.devlille.iot-lab.info',
    # 'm3-203.devlille.iot-lab.info',
    # 'm3-204.devlille.iot-lab.info',
    # 'm3-205.devlille.iot-lab.info',
]

devmobilities = {}
for mobility in devapi.circuit_mobilities.get_mobilities().items:
    devmobilities.setdefault(mobility.site, [])
    devmobilities[mobility.site].append(mobility)

model_mobilities = {mob.name: mob for mob in devapi.model_mobilities.get_model_mobilities().items}

dev_exp = devapi.experiments.submit_experiment(experiment=ExperimentPhysical(
    duration=20,
    nodes=devrobots,
    firmwareassociations=[
        FirmwareAssociation(
            nodes=devrobots,
            firmwarename='iotlab_m3_tutorial'
        )
    ]
))

devapi.experiment.send_cmd_mobility_robots(dev_exp.id, 'triangle')
time.sleep(30)
devapi.experiment.send_cmd_mobility_robots(dev_exp.id, 'random')

pass
