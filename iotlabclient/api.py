# -*- coding:utf-8 -*-

# This file is a part of IoT-LAB client
# Copyright (C) 2019 INRIA (Contact: admin@iot-lab.info)
# Contributor(s) : see AUTHORS file
#
# This software is governed by the CeCILL license under French law
# and abiding by the rules of distribution of free software.  You can  use,
# modify and/ or redistribute the software under the terms of the CeCILL
# license as circulated by CEA, CNRS and INRIA at the following URL
# http://www.cecill.info.
#
# As a counterpart to the access to the source code and  rights to copy,
# modify and redistribute granted by the license, users are provided only
# with a limited warranty  and the software's author,  the holder of the
# economic rights,  and the successive licensors  have only  limited
# liability.
#
# The fact that you are presently reading this means that you have had
# knowledge of the CeCILL license and that you accept its terms.
from iotlabclient.auth import get_user_credentials
from iotlabclient.client import ExperimentApi as clientExperimentApi, \
    ExperimentsApi, ApiClient, \
    Configuration, FirmwaresApi, \
    MonitoringApi, NodesApi, RobotsApi, \
    SitesApi, UsersApi, CircuitMobilitiesApi, ModelMobilitiesApi
from iotlabclient.utils import read_custom_api_url


class Api(object):

    def __init__(self, host=None, configuration=None):
        if configuration is None:
            configuration = Configuration()
            username, password = get_user_credentials()
            url = host or read_custom_api_url() or 'https://www.iot-lab.info/api/'
            configuration.username = username
            configuration.password = password
            configuration.host = url

        self.client = ApiClient(configuration, pool_threads=None)

        self.experiment = clientExperimentApi(self.client)
        self.experiments = ExperimentsApi(self.client)
        self.firmwares = FirmwaresApi(self.client)
        self.circuit_mobilities = CircuitMobilitiesApi(self.client)
        self.model_mobilities = ModelMobilitiesApi(self.client)
        self.monitoring = MonitoringApi(self.client)
        self.nodes = NodesApi(self.client)
        self.robots = RobotsApi(self.client)
        self.sites = SitesApi(self.client)
        self.users = UsersApi(self.client)


class ExperimentApi(object):
    """api methods for a given experiment_id"""

    def __init__(self, experiment_id, host=None, configuration=None):
        self.api = Api(host, configuration)
        self.experiment_id = experiment_id

    def __getattr__(self, item):
        if hasattr(self.api.experiment, item):
            method = getattr(self.api.experiment, item)
            return lambda *a, **kw: method(self.experiment_id, *a, **kw)
        raise AttributeError
