from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.servicio import Servicio
from schemas.servicio_schema import servicio_schema, servicios_schema

servicio_routes = Blueprint("servicio_routes", __name__)

@servicio_routes.route('/servicio', methods=['POST'])
def create_Servicio():
    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')

    new_servicio = Servicio(nombre, descripcion)

    db.session.add(new_servicio)
    db.session.commit()

    result = servicio_schema.dump(new_servicio)

    data = {
        'message': 'Nuevo Servicio creado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@servicio_routes.route('/servicio', methods=['GET'])
def get_Servicios():
    all_servicios = Servicio.query.all()
    result = servicios_schema.dump(all_servicios)

    data = {
        'message': 'Todos los Servicios',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@servicio_routes.route('/servicio/<int:id>', methods=['GET'])
def get_Servicio(id):
    servicio = Servicio.query.get(id)

    if not servicio:
        data = {
            'message': 'Servicio no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = servicio_schema.dump(servicio)

    data = {
        'message': 'Servicio encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@servicio_routes.route('/servicio/<int:id>', methods=['PUT'])
def update_Servicio(id):
    servicio = Servicio.query.get(id)

    if not servicio:
        data = {
            'message': 'Servicio no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    nombre = request.json.get('nombre')
    descripcion = request.json.get('descripcion')

    servicio.nombre = nombre
    servicio.descripcion = descripcion

    db.session.commit()

    result = servicio_schema.dump(servicio)

    data = {
        'message': 'Servicio actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@servicio_routes.route('/servicio/<int:id>', methods=['DELETE'])
def delete_Servicio(id):
    servicio = Servicio.query.get(id)

    if not servicio:
        data = {
            'message': 'Servicio no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(servicio)
    db.session.commit()

    data = {
        'message': 'Servicio eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)
