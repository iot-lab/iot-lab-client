
from iotlabclient.utils import read_custom_api_url

from iotlabadminclient.client import UserRequest, UsersApi, ApiClient, Configuration
from iotlabclient.auth import get_user_credentials

configuration = Configuration()
configuration.username, configuration.password = get_user_credentials()
configuration.host = read_custom_api_url() or 'https://www.iot-lab.info/api/'
client = ApiClient(configuration, pool_threads=None)
api = UsersApi(client)

"""
{"sshkeys":[""],"firstName":"tester","lastName":"tester",
"email":"matthieu@mmea.fr","category":"Student","organization":"inria","city":"lille","country":"France","motivations":"motivated","groups":[],"status":"active"}
"""

user = UserRequest(
    first_name='tester',
    last_name='tester',
    email='matthieu@mmea.fr',
    country='Westeros',
    city='King\'s Landing',
    organization='INRIA',
    motivations='FIT IoT-LAB',
    category='Student',
    groups=['tutorial'],
    sshkeys=['']
)
api.create_user_s(
    user_request=user,
    nbusers=6
)
