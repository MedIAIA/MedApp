from flask import Flask, abort, Blueprint, request
from flask_restful import Resource, Api
from digiez_api.models import *


api_accounts = Blueprint('api_accounts', __name__, url_prefix='/api/accounts')
api = Api(api_accounts)


class AccountList(Resource):
    def get(self):
        page = request.args.get('p')
        query = Account.query
        if page:
            query = query.order_by(Account.id).paginate(
                int(page), per_page=20, error_out=False)
            accounts = query.items
        else:
            accounts = query.all()
        accounts = accounts_schema.dump(accounts)
        return {'status': 'success', 'data': accounts}, 200

    def get(self, account_id):
        """
        Get a specific account
        ---
        tags:
                - accounts
        parameters:
                -   in: path
                    required: true
                    name: account_id
                    type: integer
        responses:
                200:
                        description: Account found for given id
                404:
                        description: No Account found for given id
        """
        account = Account.query.get(account_id)
        if not account:
            abort(404)
        result = account_schema.dump(account)
        return {'status': 'success', 'data': result}, 200

    def post(self):
        """
        Create a account
        ---
        tags:
                - accounts
        responses:
                201:
                        description: account created
        """
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # # Validate and deserialize input
        data = account_schema.load(json_data)
        account = Account.query.filter_by(name=data['name']).first()
        if account:
            return {'message': 'Account already exists'}, 400
        account = Account(**request.get_json())
        account.save()
        result = account_schema.dump(account)
        return {"status": 'success', 'data': result}, 201


    def put(self, account_id):
        """
        Edit an account
        ---
        tags:
                - account
        parameters:
                -   in: path
                    required: true
                    name: account_id
                    type: integer
        responses:
                200:
                        description: account edited
                404:
                        description: No account found for given id
        """
        data = request.get_json()
        account = Account.query.get(account_id)
        if not account:
            abort(404)
        account.update(data)
        account.save()
        result = account_schema.dump(account)
        return {"status": 'success', 'data': result}, 200

    def delete(self, account_id):
        """
        Delete an account
        ---
        tags:
                - accounts
        parameters:
                -   in: path
                    required: true
                    name: account_id
                    type: integer
        responses:
                204:
                        description: Division deleted
                404:
                        description: No account found for given id
        """
        deleted_count = Account.delete(account_id)
        if not deleted_count:
            abort(404)
        return '', 204

api.add_resource(AccountList, '/', '/<string:account_id>')
