import json

from iotlabclient.client import ExperimentAlias, Alias, AliasProperties, FirmwareAliasAssociationsFirmwareassociations

from iotlabclient.api import Api

api = Api()

experiment = ExperimentAlias(
    type='alias',
    duration=5,
    name="test",
    nodes=[
        Alias(
            alias='1',
            nbnodes=2,
            properties=AliasProperties(archi="m3:at86rf231", site='grenoble', mobile=False)
        )
    ],
    firmwareassociations=[
        FirmwareAliasAssociationsFirmwareassociations(
            firmwarename='iotlab_m3_tutorial',
            nodes=['1']
        ),
    ])

experiment_json = json.dumps(experiment.to_dict())
print(api.experiments.submit_experiment(experiment=experiment_json))
