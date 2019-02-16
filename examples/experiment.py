from pprint import pprint

from iotlabclient.api import Api

api = Api().experiment

pprint(api.experiments_id_get(12283))



api.get_experiment_archive
api.get_experiment_deployment
api.get_experiment_nodes
api.get_experiment_nodes_id
api.kill_experiment_scripts
api.reload_experiment
api.run_experiment_scripts
api.send_cmd_mobility_robots
api.send_cmd_nodes
api.send_cmd_profile_nodes
api.send_cmd_robots
api.send_cmd_update_nodes
api.send_load_profile_nodes
api.status_experiment_scripts
api.stop_experiment