import os

from iotlabclient.api import Api
from iotlabclient.client import Firmware, Model

api = Api()


model_dir = os.path.expanduser('~/iot-lab-dev/parts/robots/scripts/controlled')
firmware = os.path.expanduser('~/appli_controlled/bin/iotlab-m3/controlled.elf')

api.model_mobilities.modify_user_model_mobility('controlled',
                                                model=Model(name='controlled', script='controlled.py'),
                                                script=os.path.join(model_dir, 'controlled.py'))
print('ok updated model mobility')
api.firmwares.modify_firmware('controlled', firmware=firmware,
                              metadata=Firmware(name='controlled', filename="controlled.elf", archi='m3'))
print('ok updated firmware')

robots = [
    'm3-201.devlille.iot-lab.info',
]

exp = api.experiments.get_running_experiments().items[0]

print(api.experiment.flash_experiment_nodes(exp.id, 'controlled', nodes=robots))
print('ok sent firmware')
print(api.experiment.send_cmd_mobility_robots(exp.id, 'controlled', nodes=robots))
print('ok sent mobility')

