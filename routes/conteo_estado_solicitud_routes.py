from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.estado_solicitud import EstadoSolicitud
from models.solicitud_estado_solicitud import SolicitudEstadoSolicitud
from schemas.estado_solicitud_schema import EstadoSolicitudSchema

# from models.conteo_estado_solicitud import ConteoEstadoSolicitud
from schemas.conteo_estado_solicitud_schema import ConteoEstadoSolicitudSchema
from sqlalchemy import text, func
import traceback


conteo_estado_solicitud_routes = Blueprint("conteo_estado_solicitud_routes", __name__)
conteo_estado_solicitud_schema = ConteoEstadoSolicitudSchema()
conteo_estado_solicitud_schemas = ConteoEstadoSolicitudSchema(many=True)


@conteo_estado_solicitud_routes.route("/conteo_estado_solicitud", methods=["POST"])
def create_ConteoEstadoSolicitud():
    data = request.json
    new_conteo_estado_solicitud = ConteoEstadoSolicitud(**data)

    db.session.add(new_conteo_estado_solicitud)
    db.session.commit()

    result = conteo_estado_solicitud_schema.dump(new_conteo_estado_solicitud)

    data = {
        "message": "Nuevo Estado de Solicitud creado!",
        "status": 201,
        "data": result,
    }

    return make_response(jsonify(data), 201)


"""
@estado_solicitud_routes.route('/conteo_estado_solicitud', methods=['GET'])
def get_EstadoSolicitudes():
    all_conteo_estado_solicitudes = ConteoEstadoSolicitud.query.all()
    result = conteo_estado_solicitud_schemas.dump(all_conteo_estado_solicitudes)

    data = {
        'message': 'Todos los Estados de Solicitud',
        'status': 200,
        'data': result
    }

    return make_response(jsonify(data), 200)
"""


@conteo_estado_solicitud_routes.route("/conteo_estado_solicitud", methods=["GET"])
def interseccion_tablas():
    if request.method == "GET":
        response = []
        data = (
            db.session.query(
                EstadoSolicitud.descripcion,
                func.count(
                    SolicitudEstadoSolicitud.id_solicitud_estado_solicitud
                ).label("cantidad"),
            )
            .join(
                SolicitudEstadoSolicitud,
                EstadoSolicitud.id_estado_solicitud
                == SolicitudEstadoSolicitud.id_estado_solicitud,
            )
            .group_by(EstadoSolicitud.descripcion)
            .all()
        )
        for row in data:
            response.append({"descripcion": row.descripcion, "cantidad": row.cantidad})
        return jsonify(response)
    else:
        return jsonify({"message": "No se encontraron datos"})


@conteo_estado_solicitud_routes.route(
    "/conteo_estado_solicitud/<int:id>", methods=["PUT"]
)
def update_EstadoSolicitud(id):
    conteo_estado_solicitud = ConteoEstadoSolicitud.query.get(id)

    if not conteo_estado_solicitud:
        data = {"message": "Estado de Solicitud no encontrado", "status": 404}
        return make_response(jsonify(data), 404)

    data = request.json
    for key, value in data.items():
        setattr(conteo_estado_solicitud, key, value)

    db.session.commit()

    result = conteo_estado_solicitud_schema.dump(conteo_estado_solicitud)

    data = {"message": "Estado de Solicitud actualizado", "status": 200, "data": result}

    return make_response(jsonify(data), 200)


@conteo_estado_solicitud_routes.route(
    "/conteo_estado_solicitud/<int:id>", methods=["DELETE"]
)
def delete_EstadoSolicitud(id):
    conteo_estado_solicitud = ConteoEstadoSolicitud.query.get(id)

    if not conteo_estado_solicitud:
        data = {"message": "Estado de Solicitud no encontrado", "status": 404}
        return make_response(jsonify(data), 404)

    db.session.delete(conteo_estado_solicitud)
    db.session.commit()

    data = {"message": "Estado de Solicitud eliminado", "status": 200}

    return make_response(jsonify(data), 200)
