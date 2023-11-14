from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.tipo_predio import TipoPredio
from schemas.tipo_predio_schema import tipoPredio_schema, tiposPredio_schema

tipo_predio_routes = Blueprint("tipo_predio_routes", __name__)

@tipo_predio_routes.route('/tipo_predio', methods=['POST'])
def create_TipoPredio():
    nombre_predio = request.json.get('nombre_predio')

    new_tipo_predio = TipoPredio(
        nombre_predio
    )

    db.session.add(new_tipo_predio)
    db.session.commit()

    result = tipoPredio_schema.dump(new_tipo_predio)

    data = {
        'message': 'Nuevo Tipo de Predio creado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@tipo_predio_routes.route('/tipo_predio', methods=['GET'])
def get_TiposPredio():
    all_tipos_predio = TipoPredio.query.all()
    result = tiposPredio_schema.dump(all_tipos_predio)

    data = {
        'message': 'Todos los Tipos de Predio',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@tipo_predio_routes.route('/tipo_predio/<int:id>', methods=['GET'])
def get_TipoPredio(id):
    tipo_predio = TipoPredio.query.get(id)

    if not tipo_predio:
        data = {
            'message': 'Tipo de Predio no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = tipoPredio_schema.dump(tipo_predio)

    data = {
        'message': 'Tipo de Predio encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@tipo_predio_routes.route('/tipo_predio/<int:id>', methods=['PUT'])
def update_TipoPredio(id):
    tipo_predio = TipoPredio.query.get(id)

    if not tipo_predio:
        data = {
            'message': 'Tipo de Predio no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    nombre_predio = request.json.get('nombre_predio')

    tipo_predio.nombre_predio = nombre_predio

    db.session.commit()

    result = tipoPredio_schema.dump(tipo_predio)

    data = {
        'message': 'Tipo de Predio actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@tipo_predio_routes.route('/tipo_predio/<int:id>', methods=['DELETE'])
def delete_TipoPredio(id):
    tipo_predio = TipoPredio.query.get(id)

    if not tipo_predio:
        data = {
            'message': 'Tipo de Predio no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(tipo_predio)
    db.session.commit()

    data = {
        'message': 'Tipo de Predio eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)
