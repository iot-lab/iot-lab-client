from integration_tests import API

api = API.sites


def test_get_sites():
    sites = api.get_sites()
    assert sites.items
    assert all([item.site for item in sites.items])


def test_get_sites_details():
    sites = api.get_sites()
    sites_details = api.get_sites_details()
    assert sites.items
    assert sites_details.items

    sites = set(item.site for item in sites.items)
    sites_details = set(item.site for item in sites_details.items)

    assert sites == sites_details
