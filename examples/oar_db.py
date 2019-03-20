from datetime import datetime, timedelta, timezone
from pprint import pprint

from iotlabclient.api import Api

api = Api().scheduler


now = datetime.now(timezone.utc)
pprint(api.get_experiments_jobs(
    start=now-timedelta(hours=6),
    stop=now+timedelta(hours=6)
))

pprint(api.get_nodes_states(
    start=now-timedelta(hours=6),
    stop=now+timedelta(hours=6)
))
