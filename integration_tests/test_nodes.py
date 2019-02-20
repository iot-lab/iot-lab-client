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
from integration_tests import HOST, SITE_TLD, TLD
from iotlabclient.api import Api
from iotlabclient.utils import expand_short_nodes_list

API = Api(host=HOST)
api = API.nodes

sites = [item.site for item in API.sites.get_sites().items]


def test_get_nodes():
    nodes = api.get_nodes()

    assert nodes.items

    for node in nodes.items:
        assert node.site in sites


def test_get_nodes_id():
    global nodeid_site
    nodes = api.get_nodes()
    nodes_id = api.get_nodes_id()

    assert nodes_id.items

    assert len(nodes_id.items) == len(sites)

    nodes_map = {node.network_address: node for node in nodes.items}

    for nodeid_site in nodes_id.items:
        assert nodeid_site.site in sites
        site_tld = nodeid_site.site + TLD
        for archi_item in nodeid_site.archis:
            assert archi_item.archi
            short_archi = archi_item.archi.split(':')[0]
            for state_item in archi_item.states:
                ids = expand_short_nodes_list(state_item.ids)
                for id in ids:
                    network_address = '%s-%s.%s' % (short_archi, id, site_tld)

                    assert network_address in nodes_map

                    node = nodes_map[network_address]
                    assert node.state == state_item.state
