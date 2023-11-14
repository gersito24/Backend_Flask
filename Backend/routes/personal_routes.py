from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.personal import Personal
from schemas.personal_schema import personal_schema, personales_schema

personal_routes = Blueprint("personal_routes", __name__)

@personal_routes.route('/personal', methods=['POST'])
def create_Personal():
    nombres = request.json.get('nombres')
    apellido_paterno = request.json.get('apellido_paterno')
    apellido_materno = request.json.get('apellido_materno')
    cargo = request.json.get('cargo')

    new_personal = Personal(nombres, apellido_paterno, apellido_materno, cargo)

    db.session.add(new_personal)
    db.session.commit()

    result = personal_schema.dump(new_personal)

    data = {
        'message': 'Nuevo Personal creado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@personal_routes.route('/personal', methods=['GET'])
def get_Personals():
    all_personals = Personal.query.all()
    result = personales_schema.dump(all_personals)

    data = {
        'message': 'Todo el Personal',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@personal_routes.route('/personal/<int:id>', methods=['GET'])
def get_Personal(id):
    personal = Personal.query.get(id)

    if not personal:
        data = {
            'message': 'Personal no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = personal_schema.dump(personal)

    data = {
        'message': 'Personal encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@personal_routes.route('/personal/<int:id>', methods=['PUT'])
def update_Personal(id):
    personal = Personal.query.get(id)

    if not personal:
        data = {
            'message': 'Personal no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    nombres = request.json.get('nombres')
    apellido_paterno = request.json.get('apellido_paterno')
    apellido_materno = request.json.get('apellido_materno')
    cargo = request.json.get('cargo')

    personal.nombres = nombres
    personal.apellido_paterno = apellido_paterno
    personal.apellido_materno = apellido_materno
    personal.cargo = cargo

    db.session.commit()

    result = personal_schema.dump(personal)

    data = {
        'message': 'Personal actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@personal_routes.route('/personal/<int:id>', methods=['DELETE'])
def delete_Personal(id):
    personal = Personal.query.get(id)

    if not personal:
        data = {
            'message': 'Personal no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(personal)
    db.session.commit()

    data = {
        'message': 'Personal eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)
