# routes/estado_solicitud_routes.py
from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.estado_solicitud import EstadoSolicitud
from schemas.estado_solicitud_schema import EstadoSolicitudSchema

estado_solicitud_routes = Blueprint("estado_solicitud_routes", __name__)
estado_solicitud_schema = EstadoSolicitudSchema()
estado_solicitudes_schema = EstadoSolicitudSchema(many=True)

@estado_solicitud_routes.route('/estado_solicitud', methods=['POST'])
def create_EstadoSolicitud():
    data = request.json
    new_estado_solicitud = EstadoSolicitud(**data)

    db.session.add(new_estado_solicitud)
    db.session.commit()

    result = estado_solicitud_schema.dump(new_estado_solicitud)

    data = {
        'message': 'Nuevo Estado de Solicitud creado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@estado_solicitud_routes.route('/estado_solicitud', methods=['GET'])
def get_EstadoSolicitudes():
    all_estado_solicitudes = EstadoSolicitud.query.all()
    result = estado_solicitudes_schema.dump(all_estado_solicitudes)

    data = {
        'message': 'Todos los Estados de Solicitud',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@estado_solicitud_routes.route('/estado_solicitud/<int:id>', methods=['GET'])
def get_EstadoSolicitud(id):
    estado_solicitud = EstadoSolicitud.query.get(id)

    if not estado_solicitud:
        data = {
            'message': 'Estado de Solicitud no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = estado_solicitud_schema.dump(estado_solicitud)

    data = {
        'message': 'Estado de Solicitud encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@estado_solicitud_routes.route('/estado_solicitud/<int:id>', methods=['PUT'])
def update_EstadoSolicitud(id):
    estado_solicitud = EstadoSolicitud.query.get(id)

    if not estado_solicitud:
        data = {
            'message': 'Estado de Solicitud no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    data = request.json
    for key, value in data.items():
        setattr(estado_solicitud, key, value)

    db.session.commit()

    result = estado_solicitud_schema.dump(estado_solicitud)

    data = {
        'message': 'Estado de Solicitud actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@estado_solicitud_routes.route('/estado_solicitud/<int:id>', methods=['DELETE'])
def delete_EstadoSolicitud(id):
    estado_solicitud = EstadoSolicitud.query.get(id)

    if not estado_solicitud:
        data = {
            'message': 'Estado de Solicitud no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(estado_solicitud)
    db.session.commit()

    data = {
        'message': 'Estado de Solicitud eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)
