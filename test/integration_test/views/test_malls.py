import json
from flask import url_for



def test_api_get_all_malls_should_return_json_malls(client):
    # When
    res = client.get(url_for('api_malls.get_malls'))
    data = res.json
    # Then
    assert res.status_code == 200
    assert len(data['data']) == 2

def test_api_get_mall_should_return_404_if_mall_not_found(client):
    # When
    res = client.get(url_for('api_malls.get_mall', mall_id=3))

    # Then
    assert res.status_code == 404

def test_api_create_mall_should_return_json_mall(client):
    # Given
    mall = {'name': 'NewMall'}

    # When
    res = client.post(
        url_for('api_malls.get_mall'),
        data=json.dumps(mall)
    )
    data = res.json

    # Then
    assert res.status_code == 201
    assert data['data']['name'] == 'NewMall'
