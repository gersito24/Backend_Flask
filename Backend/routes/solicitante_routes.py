from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.solicitante import Solicitante
from schemas.solicitante_schema import solicitante_schema, solicitantes_schema

solicitante_routes = Blueprint("solicitante_routes", __name__)

@solicitante_routes.route('/solicitante', methods=['POST'])
def create_Solicitante():
    id_solicitante = request.json.get('id_solicitante')
    id_persona = request.json.get('id_persona')
    id_rol = request.json.get('id_rol')
    telefono = request.json.get('telefono')
    correo = request.json.get('correo')

    new_solicitante = Solicitante(id_solicitante, id_persona, id_rol, telefono, correo)

    db.session.add(new_solicitante)
    db.session.commit()

    result = solicitante_schema.dump(new_solicitante)

    data = {
        'message': 'Nuevo Solicitante creado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@solicitante_routes.route('/solicitante', methods=['GET'])
def get_Solicitantes():
    all_solicitantes = Solicitante.query.all()
    result = solicitantes_schema.dump(all_solicitantes)

    data = {
        'message': 'Todos los Solicitantes',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@solicitante_routes.route('/solicitante/<int:id>', methods=['GET'])
def get_Solicitante(id):
    solicitante = Solicitante.query.get(id)

    if not solicitante:
        data = {
            'message': 'Solicitante no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = solicitante_schema.dump(solicitante)

    data = {
        'message': 'Solicitante encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@solicitante_routes.route('/solicitante/<int:id>', methods=['PUT'])
def update_Solicitante(id):
    solicitante = Solicitante.query.get(id)

    if not solicitante:
        data = {
            'message': 'Solicitante no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    id_solicitante = request.json.get('id_solicitante')
    id_persona = request.json.get('id_persona')
    id_rol = request.json.get('id_rol')
    telefono = request.json.get('telefono')
    correo = request.json.get('correo')

    solicitante.id_solicitante = id_solicitante
    solicitante.id_persona = id_persona
    solicitante.id_rol = id_rol
    solicitante.telefono = telefono
    solicitante.correo = correo

    db.session.commit()

    result = solicitante_schema.dump(solicitante)

    data = {
        'message': 'Solicitante actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@solicitante_routes.route('/solicitante/<int:id>', methods=['DELETE'])
def delete_Solicitante(id):
    solicitante = Solicitante.query.get(id)

    if not solicitante:
        data = {
            'message': 'Solicitante no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(solicitante)
    db.session.commit()

    data = {
        'message': 'Solicitante eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)