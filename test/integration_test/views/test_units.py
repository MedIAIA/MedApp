import json
from flask import url_for



def test_api_get_all_units_should_return_json_units(client):
    # When
    res = client.get(url_for('api_units.get_units'))
    data = res.json
    # Then
    assert res.status_code == 200
    assert len(data['data']) == 2


def test_api_get_unit_should_return_404_if_mall_not_found(client):
    # When
    res = client.get(url_for('api_units.get_units', unit_id=3))

    # Then
    assert res.status_code == 404


def test_api_create_unit_should_return_json_unit(client):
    # Given
    unit = {'name': 'NewUnit'}

    # When
    res = client.post(
        url_for('api_units.get_units'),
        data=json.dumps(unit)
    )
    data = res.json

    # Then
    assert res.status_code == 201
    assert data['data']['name'] == 'NewUnit'
