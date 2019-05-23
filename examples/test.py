import os

from integration_tests import API, ROBOT_SITE
from iotlabclient.client import Circuit, Model, Firmware, Profile, ProfileConsumption

circuit = Circuit(
    name="my_circuit",
    coordinates={
        "A": {
            "theta": 1.57,
            "x": 22,
            "y": 7
        },
        "B": {
            "theta": 0,
            "x": 24,
            "y": 7
        },
        "C": {
            "theta": -1.57,
            "x": 24,
            "y": 4
        },
        "D": {
            "theta": 3.14,
            "x": 22,
            "y": 4
        }
    },
    points=["A", "B", "C", "D"],
    loop=True,
    site=ROBOT_SITE
)

model = Model(
    name='my_model',
    script='script.py',

)

firmware = Firmware(name='my_firmware', filename='tutorial_m3.elf')

profile = Profile(profilename='test_profile', power='dc', nodearch='m3', consumption=ProfileConsumption(current=True, power=True, voltage=True, period=4156, average=1))


API.monitoring.save_profile(profile=profile)

# API.circuit_mobilities.save_user_mobility(circuit=circuit)

# API.model_mobilities.save_user_model_mobility(model=model, script='/home/matthieu/iot-lab-dev/parts/iot-lab-client/integration_tests/models/script.py')



#API.firmwares.save_firmware(metadata=firmware, firmware='/home/matthieu/iot-lab-dev/parts/iot-lab-client/integration_tests/tutorial_m3.elf')

pass
