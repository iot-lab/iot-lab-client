""" example usage of the Python API"""

from iotlabclient.api import Api

api = Api().sites

# list of sites
print(api.get_sites().items)

# sites details (
print(api.get_sites_details().items)
