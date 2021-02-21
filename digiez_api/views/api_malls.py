from flask import abort, request, Blueprint
from digiez_api.models import *


api_malls = Blueprint('api_malls', __name__, url_prefix='/api/malls')


@api_malls.route('', methods=['GET'])
def get_malls():
    """
    Get all malls
    ---
    tags:
            - malls
    responses:
            200:
                    description: List of malls
    """
    page = request.args.get('p')
    query = Mall.query
    if page:
        query = query.order_by(Mall.id).paginate(
            int(page), per_page=20, error_out=False)
        malls = query.items
    else:
        malls = query.all()
    result = malls_schema.dump(malls)
    return {'status': 'success', 'data': result}, 200

@api_malls.route('', methods=['POST'])
def create_mall():
    """
    Create a mall
    ---
    tags:
            - malls
    responses:
            201:
                    description: mall created
    """
    json_data = request.get_json(force=True)
    if not json_data:
        return {'message': 'No input data provided'}, 400
    # # Validate and deserialize input
    data = request.get_json()
    mall = Mall.query.filter_by(name=data['name']).first()
    if mall:
        return {'message': 'Mall already exists'}, 400
    mall = Mall(**request.get_json())
    mall.save()
    result = mall_schema.dump(mall)
    return {"status": 'success', 'data': result}, 201


@api_malls.route('/<mall_id>', methods=['DELETE'])
def delete_mall(mall_id):
    """
    Delete a mall
    ---
    tags:
            - malls
    parameters:
            -   in: path
                required: true
                name: mall_id
                type: integer
    responses:
            204:
                    description: Division deleted
            404:
                    description: No mall found for given id
    """
    deleted_count = Mall.delete(mall_id)
    if not deleted_count:
        abort(404)
    return '', 204


@api_malls.route('/<mall_id>', methods=['PUT'])
def edit_mall(mall_id):
    """
    Edit a mall
    ---
    tags:
            - mall
    parameters:
            -   in: path
                required: true
                name: mall_id
                type: integer
    responses:
            200:
                    description: mall edited
            404:
                    description: No mall found for given id
    """
    data = request.get_json()
    mall = Mall.query.get(mall_id)
    if not mall:
        abort(404)
    mall.update(data)
    mall.save()
    result = mall_schema.dump(mall)
    return {"status": 'success', 'data': result}, 200


@api_malls.route('/<mall_id>', methods=['GET'])
def get_mall(mall_id):
    """
    Get a specific mall
    ---
    tags:
            - malls
    parameters:
            -   in: path
                required: true
                name: mall_id
                type: integer
    responses:
            200:
                    description: Mall found for given id
            404:
                    description: No Mall found for given id
    """
    mall = Mall.query.get(mall_id)
    if not mall:
        abort(404)
    result = account_schema.dump(mall)
    return {'status': 'success', 'data': result}, 200