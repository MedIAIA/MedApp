import json
from flask import url_for



def test_api_get_all_accounts_should_return_json_accounts(client):
    # When
    res = client.get(url_for('api_accounts.get_accounts'))
    data = res.json
    # Then
    assert res.status_code == 200
    assert len(data['data']) == 2

def test_api_get_account_should_return_404_if_account_not_found(client):
    # When
    res = client.get(url_for('api_accounts.get_account', account_id=3))

    # Then
    assert res.status_code == 404

def test_api_create_account_should_return_json_account(client):
    # Given
    account = {'name': 'Fiat'}

    # When
    res = client.post(
        url_for('api_accounts.create_account'),
        data=json.dumps(account)
    )
    data = res.json

    # Then
    assert res.status_code == 201
    assert data['data']['name'] == 'Fiat'
