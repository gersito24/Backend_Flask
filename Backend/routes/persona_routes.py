from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.persona import Persona
from schemas.persona_schema import persona_schema, personas_schema

persona_routes = Blueprint("persona_routes", __name__)

@persona_routes.route('/persona', methods=['POST'])
def create_Persona():
    apellido_paterno = request.json.get('apellido_paterno')
    apellido_materno = request.json.get('apellido_materno')
    nombres = request.json.get('nombres')
    fecha_nacimiento = request.json.get('fecha_nacimiento')
    id_tipo_documento = request.json.get('id_tipo_documento')
    ndocumento = request.json.get('ndocumento')
    direccion = request.json.get('direccion')
    idubigeo = request.json.get('idubigeo')

    new_persona = Persona(apellido_paterno, apellido_materno, nombres, fecha_nacimiento, id_tipo_documento, ndocumento, direccion, idubigeo)

    db.session.add(new_persona)
    db.session.commit()

    result = persona_schema.dump(new_persona)

    data = {
        'message': 'Nueva Persona creada!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@persona_routes.route('/persona', methods=['GET'])
def get_Personas():
    all_personas = Persona.query.all()
    result = personas_schema.dump(all_personas)

    data = {
        'message': 'Todas las Personas',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@persona_routes.route('/persona/<int:id>', methods=['GET'])
def get_Persona(id):
    persona = Persona.query.get(id)

    if not persona:
        data = {
            'message': 'Persona no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = persona_schema.dump(persona)

    data = {
        'message': 'Persona encontrada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@persona_routes.route('/persona/<int:id>', methods=['PUT'])
def update_Persona(id):
    persona = Persona.query.get(id)

    if not persona:
        data = {
            'message': 'Persona no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    apellido_paterno = request.json.get('apellido_paterno')
    apellido_materno = request.json.get('apellido_materno')
    nombres = request.json.get('nombres')
    fecha_nacimiento = request.json.get('fecha_nacimiento')
    id_tipo_documento = request.json.get('id_tipo_documento')
    ndocumento = request.json.get('ndocumento')
    direccion = request.json.get('direccion')
    idubigeo = request.json.get('idubigeo')

    persona.apellido_paterno = apellido_paterno
    persona.apellido_materno = apellido_materno
    persona.nombres = nombres
    persona.fecha_nacimiento = fecha_nacimiento
    persona.id_tipo_documento = id_tipo_documento
    persona.ndocumento = ndocumento
    persona.direccion = direccion
    persona.idubigeo = idubigeo

    db.session.commit()

    result = persona_schema.dump(persona)

    data = {
        'message': 'Persona actualizada',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@persona_routes.route('/persona/<int:id>', methods=['DELETE'])
def delete_Persona(id):
    persona = Persona.query.get(id)

    if not persona:
        data = {
            'message': 'Persona no encontrada',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(persona)
    db.session.commit()

    data = {
        'message': 'Persona eliminada',
        'status': 200
    }

    return make_response(jsonify(data), 200)