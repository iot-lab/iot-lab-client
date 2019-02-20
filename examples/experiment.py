from pprint import pprint

from iotlabclient.api import Api

api = Api().experiment

pprint(api.experiments_id_get(12283))
