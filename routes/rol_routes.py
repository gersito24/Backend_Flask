from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.rol import Rol
from schemas.rol_schema import rol_schema, roles_schema

rol_routes = Blueprint("rol_routes", __name__)

@rol_routes.route('/rol', methods=['POST'])
def create_Rol():
    nombre = request.json.get('nombre')

    new_rol = Rol(nombre)

    db.session.add(new_rol)
    db.session.commit()

    result = rol_schema.dump(new_rol)

    data = {
        'message': 'Nuevo Rol creado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@rol_routes.route('/rol', methods=['GET'])
def get_Roles():
    all_roles = Rol.query.all()
    result = roles_schema.dump(all_roles)

    data = {
        'message': 'Todos los Roles',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@rol_routes.route('/rol/<int:id>', methods=['GET'])
def get_Rol(id):
    rol = Rol.query.get(id)

    if not rol:
        data = {
            'message': 'Rol no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = rol_schema.dump(rol)

    data = {
        'message': 'Rol encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@rol_routes.route('/rol/<int:id>', methods=['PUT'])
def update_Rol(id):
    rol = Rol.query.get(id)

    if not rol:
        data = {
            'message': 'Rol no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    nombre = request.json.get('nombre')

    rol.nombre = nombre

    db.session.commit()

    result = rol_schema.dump(rol)

    data = {
        'message': 'Rol actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@rol_routes.route('/rol/<int:id>', methods=['DELETE'])
def delete_Rol(id):
    rol = Rol.query.get(id)

    if not rol:
        data = {
            'message': 'Rol no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(rol)
    db.session.commit()

    data = {
        'message': 'Rol eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)
