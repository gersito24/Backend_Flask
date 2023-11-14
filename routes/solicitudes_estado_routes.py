from flask import Blueprint, request, jsonify, make_response
from utils.db import db
from models.predio import Predio
from models.solicitud import Solicitud
from models.solicitud_estado_solicitud import SolicitudEstadoSolicitud
from models.estado_solicitud import EstadoSolicitud
from models.ubigeo import Ubigeo
from sqlalchemy import text

# Crea una nueva instancia de Blueprint
solicitudes_estado_routes = Blueprint("solicitudes_estado_routes", __name__)

@solicitudes_estado_routes.route("/solicitudes_estado", methods=["GET"])
def obtener_informacion_predio():
    if request.method == "GET":
        try:
            response = []
                
                           
            # Ejecutar la consulta utilizando SQLAlchemy
            data = (db.session.query(
                Solicitud.nombre_solicitante,
                Predio.descripcion.label("descripcion_predio"),
                Ubigeo.departamento,
                Ubigeo.provincia,
                Ubigeo.distrito,
                EstadoSolicitud.descripcion.label("descripcion_estado"),
                SolicitudEstadoSolicitud.fecha,
                Solicitud.id_solicitud
            ).join(
                Predio,
                Solicitud.id_predio == Predio.id_predio
            ).join(
                SolicitudEstadoSolicitud,
                Solicitud.id_solicitud == SolicitudEstadoSolicitud.id_solicitud
            ).join(
                EstadoSolicitud,
                SolicitudEstadoSolicitud.id_estado_solicitud == EstadoSolicitud.id_estado_solicitud
            ).join(
                Ubigeo,
                Predio.idubigeo == Ubigeo.idubigeo
            ).all()
            )
            # Procesar los resultados de la consulta
            for row in data:
                response.append({
                    "nombre_solicitante": row[0],
                    "descripcion_predio": row[1],
                    "departamento": row[2],
                    "provincia": row[3],
                    "distrito": row[4],
                    "descripcion_estado": row[5],
                    "fecha": row[6],
                    "id_solicitud": row[7]
                })
            
            # Devolver los resultados en formato JSON
            return jsonify(response)
        except Exception as e:
            # Manejo de errores: Registra el error o devuelve una respuesta de error adecuada
            return jsonify({"error": str(e)})
    else:
        # Manejo de métodos HTTP no admitidos
        return jsonify({"message": "Método HTTP no admitido"})