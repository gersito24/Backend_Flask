from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.ubigeo import Ubigeo
from schemas.ubigeo_schema import ubigeo_schema, ubigeos_schema

ubigeo_routes = Blueprint("ubigeo_routes", __name__)

@ubigeo_routes.route('/ubigeo', methods=['POST'])
def create_Ubigeo():
    departamento = request.json.get('departamento')
    provincia = request.json.get('provincia')
    distrito = request.json.get('distrito')
    superficie = request.json.get('superficie')
    altitud = request.json.get('altitud')
    latitud = request.json.get('latitud')
    longitud = request.json.get('longitud')

    new_ubigeo = Ubigeo(
        departamento,
        provincia,
        distrito,
        superficie,
        altitud,
        latitud,
        longitud
    )

    db.session.add(new_ubigeo)
    db.session.commit()

    result = ubigeo_schema.dump(new_ubigeo)

    data = {
        'message': 'Nuevo Ubigeo creado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@ubigeo_routes.route('/ubigeo', methods=['GET'])
def get_Ubigeos():
    all_ubigeos = Ubigeo.query.all()
    result = ubigeos_schema.dump(all_ubigeos)

    data = {
        'message': 'Todos los Ubigeos',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@ubigeo_routes.route('/ubigeo/<string:id>', methods=['GET'])
def get_Ubigeo(id):
    ubigeo = Ubigeo.query.get(id)

    if not ubigeo:
        data = {
            'message': 'Ubigeo no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = ubigeo_schema.dump(ubigeo)

    data = {
        'message': 'Ubigeo encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@ubigeo_routes.route('/ubigeo/<string:id>', methods=['PUT'])
def update_Ubigeo(id):
    ubigeo = Ubigeo.query.get(id)

    if not ubigeo:
        data = {
            'message': 'Ubigeo no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    departamento = request.json.get('departamento')
    provincia = request.json.get('provincia')
    distrito = request.json.get('distrito')
    superficie = request.json.get('superficie')
    altitud = request.json.get('altitud')
    latitud = request.json.get('latitud')
    longitud = request.json.get('longitud')

    ubigeo.departamento = departamento
    ubigeo.provincia = provincia
    ubigeo.distrito = distrito
    ubigeo.superficie = superficie
    ubigeo.altitud = altitud
    ubigeo.latitud = latitud
    ubigeo.longitud = longitud

    db.session.commit()

    result = ubigeo_schema.dump(ubigeo)

    data = {
        'message': 'Ubigeo actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@ubigeo_routes.route('/ubigeo/<string:id>', methods=['DELETE'])
def delete_Ubigeo(id):
    ubigeo = Ubigeo.query.get(id)

    if not ubigeo:
        data = {
            'message': 'Ubigeo no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(ubigeo)
    db.session.commit()

    data = {
        'message': 'Ubigeo eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)
