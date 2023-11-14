from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.tipo_documento import TipoDocumento
from schemas.tipo_documento_schema import tipoDocumento_schema, tiposDocumento_schema

tipo_documento_routes = Blueprint("tipo_documento_routes", __name__)

@tipo_documento_routes.route('/tipo_documento', methods=['POST'])
def create_TipoDocumento():
    descripcion = request.json.get('descripcion')

    new_tipo_documento = TipoDocumento(
        descripcion
    )

    db.session.add(new_tipo_documento)
    db.session.commit()

    result = tipoDocumento_schema.dump(new_tipo_documento)

    data = {
        'message': 'Nuevo Tipo de Documento creado!',
        'status': 201,
        'data': result
    }

    return make_response(jsonify(data), 201)

@tipo_documento_routes.route('/tipo_documento', methods=['GET'])
def get_TiposDocumento():
    all_tipos_documento = TipoDocumento.query.all()
    result = tiposDocumento_schema.dump(all_tipos_documento)

    data = {
        'message': 'Todos los Tipos de Documento',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@tipo_documento_routes.route('/tipo_documento/<int:id>', methods=['GET'])
def get_TipoDocumento(id):
    tipo_documento = TipoDocumento.query.get(id)

    if not tipo_documento:
        data = {
            'message': 'Tipo de Documento no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    result = tipoDocumento_schema.dump(tipo_documento)

    data = {
        'message': 'Tipo de Documento encontrado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@tipo_documento_routes.route('/tipo_documento/<int:id>', methods=['PUT'])
def update_TipoDocumento(id):
    tipo_documento = TipoDocumento.query.get(id)

    if not tipo_documento:
        data = {
            'message': 'Tipo de Documento no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    descripcion = request.json.get('descripcion')

    tipo_documento.descripcion = descripcion

    db.session.commit()

    result = tipoDocumento_schema.dump(tipo_documento)

    data = {
        'message': 'Tipo de Documento actualizado',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)

@tipo_documento_routes.route('/tipo_documento/<int:id>', methods=['DELETE'])
def delete_TipoDocumento(id):
    tipo_documento = TipoDocumento.query.get(id)

    if not tipo_documento:
        data = {
            'message': 'Tipo de Documento no encontrado',
            'status': 404
        }
        return make_response(jsonify(data), 404)

    db.session.delete(tipo_documento)
    db.session.commit()

    data = {
        'message': 'Tipo de Documento eliminado',
        'status': 200
    }

    return make_response(jsonify(data), 200)
