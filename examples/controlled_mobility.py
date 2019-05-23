from iotlabclient.client import ExperimentPhysical, FirmwareAssociation, MobilityAssociation, Associations, \
    MobilityAssociations

from iotlabclient.api import Api

api = Api()

robots = [
    'm3-201.devlille.iot-lab.info',
]

api.experiments.submit_experiment(experiment=ExperimentPhysical(
        duration=60,
        nodes=robots,
        firmwareassociations=[
            FirmwareAssociation(
                nodes=robots,
                firmwarename='controlled'
            )
        ],
        associations=MobilityAssociations(
            mobility=[
                MobilityAssociation(mobilityname='controlled', nodes=[robots[0]])
            ],
        )
    ))
