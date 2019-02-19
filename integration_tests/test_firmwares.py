from iotlabclient.api import Api

api = Api().firmwares


def test_get_firmwares():
    data = api.get_firmwares()

    assert data

    assert len(data) > 0
