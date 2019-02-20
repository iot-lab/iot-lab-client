import json
from pprint import pprint

from iotlabclient.api import Api, ExperimentApi

api = Api()

running_experiments = api.experiments.get_running_experiments()

print(running_experiments)
for running_experiment in running_experiments.items:
    experiment_api = ExperimentApi(running_experiment.id)
    all_nodes = experiment_api.get_experiment_nodes().items
    one_node_address = json.dumps([all_nodes[0].network_address])
    all_nodes_addresses = json.dumps([node.network_address for node in all_nodes])

    print('flash all the nodes (explicit list) with tutorial_m3.elf (local file)')
    pprint(experiment_api.send_cmd_update_nodes(
        firmware='tutorial_m3.elf',
        nodes=all_nodes_addresses))

    print('flash one of the nodes with tutorial_m3.elf (local file)')
    pprint(experiment_api.send_cmd_update_nodes(
        firmware='tutorial_m3.elf',
        nodes=one_node_address))

    print('flash all nodes (no list sent) with tutorial_m3.elf (local file)')
    pprint(experiment_api.send_cmd_update_nodes(
        firmware='tutorial_m3.elf'
    ))

    pprint(experiment_api.get_experiment())

    print('flash all nodes with default_m3 (firmware store)')
    pprint(experiment_api.flash_nodes(
        'default_m3',
        request_body=[]
    ))

    pprint(experiment_api.get_experiment_token())

    pprint(experiment_api.get_experiment_archive())

    pprint(experiment_api.get_experiment_deployment())

    pprint(experiment_api.get_experiment_nodes())

    pprint(experiment_api.get_experiment_nodes_id())

    print('stop nodes...')
    pprint(experiment_api.send_cmd_nodes('stop'))

    print('start nodes...')
    pprint(experiment_api.send_cmd_nodes('start'))
