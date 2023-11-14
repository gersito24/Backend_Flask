from utils.db import db

class Solicitud(db.Model):
    __tablename__ = "solicitud"

    id_solicitud = db.Column(db.BigInteger, primary_key=True)
    id_predio = db.Column(db.Integer, db.ForeignKey("predio.id_predio"))
    id_solicitante = db.Column(db.Integer, db.ForeignKey("solicitante.id_solicitante"))
    id_servicio = db.Column(db.Integer, db.ForeignKey("servicio.id_servicio"))
    area_predio = db.Column(db.Numeric)
    num_casas = db.Column(db.Integer)
    cant_acomunes = db.Column(db.Integer)
    area_acomunes = db.Column(db.Float)
    cant_vigilantes = db.Column(db.Integer)
    cant_plimpieza = db.Column(db.Integer)
    cant_administracion = db.Column(db.Integer)
    cant_jardineria = db.Column(db.Integer)
    fecha_solicitud = db.Column(db.Date)
    nombre_solicitante = db.Column(db.String(255))

    def __init__(self, id_predio, id_solicitante, id_servicio, area_predio, num_casas, cant_acomunes, area_acomunes, cant_vigilantes, cant_plimpieza, cant_administracion, cant_jardineria, fecha_solicitud, nombre_solicitante):
        self.id_predio = id_predio
        self.id_solicitante = id_solicitante
        self.id_servicio = id_servicio
        self.area_predio = area_predio
        self.num_casas = num_casas
        self.cant_acomunes = cant_acomunes
        self.area_acomunes = area_acomunes
        self.cant_vigilantes = cant_vigilantes
        self.cant_plimpieza = cant_plimpieza
        self.cant_administracion = cant_administracion
        self.cant_jardineria = cant_jardineria
        self.fecha_solicitud = fecha_solicitud
        self.nombre_solicitante = nombre_solicitante
