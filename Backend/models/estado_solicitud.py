# models/estado_solicitud.py
from utils.db import db

class EstadoSolicitud(db.Model):
    __tablename__ = "estado_solicitud"

    id_estado_solicitud = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255), nullable=False)
    ind_cotizacion = db.Column(db.String(1), nullable=False)

    def __init__(self, descripcion, ind_cotizacion):
        self.descripcion = descripcion
        self.ind_cotizacion = ind_cotizacion
