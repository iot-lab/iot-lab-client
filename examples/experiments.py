import json
from pprint import pprint

from iotlabclient.client import ExperimentAlias, Alias, AliasProperties, ExperimentPhysical, \
    ArchiString, FirmwareAssociation

from iotlabclient.api import Api
from iotlabclient.client.models import FirmwareAliasAssociation

api = Api()

print('all experiments:')
pprint(api.experiments.get_experiments())
print('experiments total:')
pprint(api.experiments.get_experiments_total())
print('running experiments:')
pprint(api.experiments.get_running_experiments())
all_nodes = api.nodes.get_nodes(archi=ArchiString.M3, state="Alive")

experiment = ExperimentAlias(
    duration=10,
    name="test_client",
    nodes=[
        Alias(
            alias='1',
            nbnodes=2,
            properties=AliasProperties(archi="m3:at86rf231", site='devgrenoble', mobile=False)
        )
    ],
    firmwareassociations=[
        FirmwareAliasAssociation(
            firmwarename='iotlab_m3_tutorial',
            nodes=['1']
        ),
    ])

print('alias exp:')
print(api.experiments.submit_experiment(experiment=experiment))

print('alias exp with firmware:')

experiment.firmwareassociations = [
        FirmwareAliasAssociation(
            firmwarename='tutorial_m3.elf',
            nodes=['1']
        ),
    ]
print(api.experiments.submit_experiment(experiment=experiment, files=['tutorial_m3.elf']))

exp_nodes = [node.network_address for node in all_nodes.items[:2]]

experiment = ExperimentPhysical(
    duration=10,
    name='test_phys',
    nodes=exp_nodes,
    firmwareassociations=[
        FirmwareAssociation(
            firmwarename='iotlab_m3_tutorial',
            nodes=exp_nodes
        )
    ]
)

print('physical exp:')
pprint(api.experiments.submit_experiment(experiment=experiment))
