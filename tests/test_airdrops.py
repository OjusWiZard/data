import json


def test_airdrops_metadata():
    airdrop_index = json.load(open('airdrops/index_v1.json'))
    airdrops = airdrop_index['airdrops']
    poap_airdrops = airdrop_index['poap_airdrops']

    for protocol_name, airdrop_data in airdrops.items():
        assert isinstance(protocol_name, str)
        for field in ('csv_url', 'asset_identifier', 'url', 'name', 'icon'):
            assert isinstance(airdrop_data[field], str)
        assert airdrop_data['csv_url'].endswith('.csv')

    for protocol_name, airdrop_data in poap_airdrops.items():
        assert isinstance(protocol_name, str)
        for i in range(3):
            assert isinstance(airdrop_data[i], str)
        assert airdrop_data[0].endswith('.json')
