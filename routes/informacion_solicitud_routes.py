from flask import Blueprint, request, jsonify, make_response
from utils.db import db

from models.solicitud import Solicitud
from models.solicitante import Solicitante
from models.persona import Persona
from models.predio import Predio
from models.predio_area_comun import PredioAreaComun
from models.servicio import Servicio
from models.area_comun import AreaComun


from sqlalchemy import text, func
import traceback

from schemas.informacion_solicitud_schema import InformacionSolicitudSchema

informacion_solicitud_routes = Blueprint("informacion_solicitud_routes", __name__)
informacion_solicitud_schema = InformacionSolicitudSchema()

@informacion_solicitud_routes.route("/informacion_solicitud", methods=["POST"])
def create_InformacionSolicitud():
    try:
        data = request.json
        # Lógica para obtener la información de las tablas y construir un objeto InformacionSolicitante

        # Supongamos que el objeto informacion_solicitante se ha construido correctamente
        new_informacion_solicitud = InformacionSolicitud(**data)

        db.session.add(new_informacion_solicitud)
        db.session.commit()

        result = informacion_solicitud_schema.dump(new_informacion_solicitud)

        data = {
            "message": "Nueva Informacion de Solicitante creada!",
            "status": 201,
            "data": result,
        }

        return make_response(jsonify(data), 201)

    except Exception as e:
        traceback.print_exc()
        data = {"message": "Error en la creación de la Informacion de Solicitante", "status": 500}
        return make_response(jsonify(data), 500)

@informacion_solicitud_routes.route("/informacion_solicitud", methods=["GET"])
def get_InformacionSolicitud():
    if request.method == "GET":
        response = []
        data = (
            db.session.query(
                Solicitud.id_solicitud.label("id_solicitud"), 
                Solicitud.num_casas.label("numero_solicitud"),
                Solicitante.id_solicitante,
                Persona.id_persona,
                func.concat(Persona.apellido_paterno, ' ', Persona.apellido_materno, ' ', Persona.nombres).label("nombre_solicitante"),
                Solicitud.id_predio,
                Solicitud.fecha_solicitud,
                Predio.descripcion.label("predio"),
                Solicitud.area_predio.label("area_predio"),
                Solicitud.num_casas.label("numero_casas"),
                Servicio.descripcion.label("servicio_solicitado"),
                func.count(PredioAreaComun.id_area_comun).label("cantidad_areas_comunes"),
                PredioAreaComun.id_area_comun.label("id_area_comun"),
                PredioAreaComun.id_predio.label("id_predio_area_comun"),
            )
            .join(Solicitante, Solicitud.id_solicitante == Solicitante.id_solicitante)
            .join(Persona, Solicitante.id_persona == Persona.id_persona)
            .join(Predio, Solicitud.id_predio == Predio.id_predio)
            .join(PredioAreaComun, Predio.id_predio == PredioAreaComun.id_predio)
            .join(AreaComun, PredioAreaComun.id_area_comun == AreaComun.id_area_comun)
            .join(Servicio, Solicitud.id_servicio == Servicio.id_servicio)
            .group_by(
                Solicitud.id_solicitud,
                Solicitud.num_casas,
                Solicitante.id_solicitante,
                Persona.id_persona,
                func.concat(Persona.apellido_paterno, ' ', Persona.apellido_materno, ' ', Persona.nombres),
                Solicitud.id_predio,
                Solicitud.fecha_solicitud,
                Predio.descripcion,
                Solicitud.area_predio,
                Solicitud.num_casas,
                Servicio.descripcion,
                PredioAreaComun.id_area_comun,
                PredioAreaComun.id_predio,
            )
            .order_by(Solicitud.num_casas)
            .all()
        )
        for row in data:
            response.append({
                "numero_solicitud": row.numero_solicitud,
                "id_solicitante": row.id_solicitante,
                "id_persona": row.id_persona,
                "id_predio": row.id_predio,
                "id_solicitud": row.id_solicitud,
                "fecha_solicitud": row.fecha_solicitud,
                "predio": row.predio,
                "area_predio": row.area_predio,
                "numero_casas": row.numero_casas,
                "Nombre": row.nombre_solicitante,
                "servicio_solicitado": row.servicio_solicitado,
                "cantidad_areas_comunes": row.cantidad_areas_comunes,
                "id_area_comun": row.id_area_comun,
                "id_predio_area_comun": row.id_predio_area_comun,
            })
        return jsonify(response)
    else:
        return make_response(jsonify({"message": "Error en la solicitud", "status": 500}), 500)

@informacion_solicitud_routes.route("/informacion_solicitud/<int:id>", methods=["PUT"])
def update_InformacionSolicitud(id):
    try:
        informacion_solicitud = InformacionSolicitud.query.get(id)

        if not informacion_solicitud:
            data = {"message": "Informacion de Solicitante no encontrada", "status": 404}
            return make_response(jsonify(data), 404)

        data = request.json
        for key, value in data.items():
            setattr(informacion_solicitud, key, value)

        db.session.commit()

        result = informacion_solicitud_schema.dump(informacion_solicitud)

        data = {"message": "Informacion de Solicitante actualizada", "status": 200, "data": result}

        return make_response(jsonify(data), 200)

    except Exception as e:
        traceback.print_exc()
        data = {"message": "Error al actualizar la Informacion de Solicitante", "status": 500}
        return make_response(jsonify(data), 500)

@informacion_solicitud_routes.route("/informacion_solicitud/<int:id>", methods=["DELETE"])
def delete_InformacionSolicitud(id):
    try:
        informacion_solicitud = InformacionSolicitud.query.get(id)

        if not informacion_solicitud:
            data = {"message": "Informacion de Solicitante no encontrada", "status": 404}
            return make_response(jsonify(data), 404)

        db.session.delete(informacion_solicitud)
        db.session.commit()

        data = {"message": "Informacion de Solicitud eliminada", "status": 200}

        return make_response(jsonify(data), 200)

    except Exception as e:
        traceback.print_exc()
        data = {"message": "Error al eliminar la Informacion de Solicitud", "status": 500}
        return make_response(jsonify(data), 500)
