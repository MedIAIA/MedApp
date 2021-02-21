from flask import abort, request, Blueprint
from digiez_api.models import *


api_units = Blueprint('api_units', __name__, url_prefix='/api/units')


@api_units.route('', methods=['GET'])
def get_units():
    """
    Get all units
    ---
    tags:
            - units
    responses:
            200:
                    description: List of units
    """
    page = request.args.get('p')
    query = Unit.query
    if page:
        query = query.order_by(Unit.id).paginate(
            int(page), per_page=20, error_out=False)
        units = query.items
    else:
        units = query.all()
    units = units_schema.dump(units)
    return {'status': 'success', 'data': units}, 200


@api_units.route('', methods=['POST'])
def create_unit():
    """
    Create a unit
    ---
    tags:
            - units
    responses:
            201:
                    description: unit created
    """
    json_data = request.get_json(force=True)
    if not json_data:
        return {'message': 'No input data provided'}, 400
    # # Validate and deserialize input
    data = unit_schema.load(json_data)
    unit = Unit.query.filter_by(name=data['name']).first()
    if unit:
        return {'message': 'Unit already exists'}, 400
    unit = Account(**request.get_json())
    unit.save()
    result = account_schema.dump(unit)
    return {"status": 'success', 'data': result}, 201


@api_units.route('/<unit_id>', methods=['GET'])
def get_unit(unit_id):
    """
    Get a specific unit
    ---
    tags:
            - units
    parameters:
            -   in: path
                required: true
                name: unit_id
                type: integer
    responses:
            200:
                    description: Unit found for given id
            404:
                    description: No Unit found for given id
    """
    unit = Account.query.get(unit_id)
    if not unit:
        abort(404)
    result = account_schema.dump(unit)
    return {'status': 'success', 'data': result}, 200


@api_units.route('/<unit_id>', methods=['PUT'])
def edit_unit(unit_id):
    """
    Edit a unit
    ---
    tags:
            - unit
    parameters:
            -   in: path
                required: true
                name: unit_id
                type: integer
    responses:
            200:
                    description: unit edited
            404:
                    description: No unit found for given id
    """
    data = request.get_json()
    unit = Unit.query.get(unit_id)
    if not unit:
        abort(404)
    unit.update(data)
    unit.save()
    result = unit_schema.dump(unit)
    return {"status": 'success', 'data': result}, 200


@api_units.route('/<unit_id>', methods=['DELETE'])
def delete_unit(unit_id):
    """
    Delete an unit
    ---
    tags:
            - units
    parameters:
            -   in: path
                required: true
                name: unit_id
                type: integer
    responses:
            204:
                    description: Division deleted
            404:
                    description: No unit found for given id
    """
    deleted_count = Unit.delete(unit_id)
    if not deleted_count:
        abort(404)
    return '', 204
