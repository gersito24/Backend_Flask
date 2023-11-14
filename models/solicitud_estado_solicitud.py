from utils.db import db

class SolicitudEstadoSolicitud(db.Model):
    __tablename__ = "solicitud_estado_solicitud"

    id_solicitud_estado_solicitud = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    id_solicitud = db.Column(db.Integer)
    id_estado_solicitud = db.Column(db.Integer, db.ForeignKey('estado_solicitud.id_estado_solicitud'))
    ind_ultimo = db.Column(db.String(255))
    
    def __init__(self, id_solicitud_estado_solicitud, fecha,id_solicitud,ind_ultimo):
        self.id_solicitud_estado_solicitud = id_solicitud_estado_solicitud
        self.fecha = fecha
        self.id_solicitud = id_solicitud
        self.ind_ultimo = ind_ultimo