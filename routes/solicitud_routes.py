from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.solicitud import Solicitud
from schemas.solicitud_schema import solicitud_schema, solicitudes_schema

solicitud_routes = Blueprint("solicitud_routes", __name__)


@solicitud_routes.route("/solicitud", methods=["POST"])
def create_Solicitud():
    id_predio = request.json.get("id_predio")
    id_solicitante = request.json.get("id_solicitante")
    id_servicio = request.json.get("id_servicio")
    area_predio = request.json.get("area_predio")
    num_casas = request.json.get("num_casas")
    cant_acomunes = request.json.get("cant_acomunes")
    area_acomunes = request.json.get("area_acomunes")
    cant_vigilantes = request.json.get("cant_vigilantes")
    cant_plimpieza = request.json.get("cant_plimpieza")
    cant_administracion = request.json.get("cant_administracion")
    cant_jardineria = request.json.get("cant_jardineria")
    fecha_solicitud = request.json.get("fecha_solicitud")
    nombre_solicitante = request.json.get("nombre_solicitante")

    new_solicitud = Solicitud(
        id_predio,
        id_solicitante,
        id_servicio,
        area_predio,
        num_casas,
        cant_acomunes,
        area_acomunes,
        cant_vigilantes,
        cant_plimpieza,
        cant_administracion,
        cant_jardineria,
        fecha_solicitud,
        nombre_solicitante,
    )

    db.session.add(new_solicitud)
    db.session.commit()

    result = solicitud_schema.dump(new_solicitud)

    data = {"message": "Nueva Solicitud creada!", "status": 201, "data": result}

    return make_response(jsonify(data), 201)


@solicitud_routes.route("/solicitud", methods=["GET"])
def get_Solicitudes():
    all_solicitudes = Solicitud.query.all()
    result = solicitudes_schema.dump(all_solicitudes)

    data = {"message": "Todas las Solicitudes", "status": 200, "data": result}

    return make_response(jsonify(data), 200)


@solicitud_routes.route("/solicitud/<int:id>", methods=["GET"])
def get_Solicitud(id):
    solicitud = Solicitud.query.get(id)

    if not solicitud:
        data = {"message": "Solicitud no encontrada", "status": 404}
        return make_response(jsonify(data), 404)

    result = solicitud_schema.dump(solicitud)

    data = {"message": "Solicitud encontrada", "status": 200, "data": result}

    return make_response(jsonify(data), 200)


@solicitud_routes.route("/solicitud/<int:id>", methods=["PUT"])
def update_Solicitud(id):
    solicitud = Solicitud.query.get(id)

    if not solicitud:
        data = {"message": "Solicitud no encontrada", "status": 404}
        return make_response(jsonify(data), 404)

    id_predio = request.json.get("id_predio")
    id_solicitante = request.json.get("id_solicitante")
    id_servicio = request.json.get("id_servicio")
    area_predio = request.json.get("area_predio")
    num_casas = request.json.get("num_casas")
    cant_acomunes = request.json.get("cant_acomunes")
    area_acomunes = request.json.get("area_acomunes")
    cant_vigilantes = request.json.get("cant_vigilantes")
    cant_plimpieza = request.json.get("cant_plimpieza")
    cant_administracion = request.json.get("cant_administracion")
    cant_jardineria = request.json.get("cant_jardineria")
    fecha_solicitud = request.json.get("fecha_solicitud")
    nombre_solicitante = request.json.get("nombre_solicitante")

    solicitud.id_predio = id_predio
    solicitud.id_solicitante = id_solicitante
    solicitud.id_servicio = id_servicio
    solicitud.area_predio = area_predio
    solicitud.num_casas = num_casas
    solicitud.cant_acomunes = cant_acomunes
    solicitud.area_acomunes = area_acomunes
    solicitud.cant_vigilantes = cant_vigilantes
    solicitud.cant_plimpieza = cant_plimpieza
    solicitud.cant_administracion = cant_administracion
    solicitud.cant_jardineria = cant_jardineria
    solicitud.fecha_solicitud = fecha_solicitud
    solicitud.nombre_solicitante = nombre_solicitante

    db.session.commit()

    result = solicitud_schema.dump(solicitud)

    data = {"message": "Solicitud actualizada", "status": 200, "data": result}

    return make_response(jsonify(data), 200)


@solicitud_routes.route("/solicitud/<int:id>", methods=["DELETE"])
def delete_Solicitud(id):
    solicitud = Solicitud.query.get(id)

    if not solicitud:
        data = {"message": "Solicitud no encontrada", "status": 404}
        return make_response(jsonify(data), 404)

    db.session.delete(solicitud)
    db.session.commit()

    data = {"message": "Solicitud eliminada", "status": 200}

    return make_response(jsonify(data), 200)
