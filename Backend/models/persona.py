from utils.db import db

class Persona(db.Model):
    __tablename__ = "persona"

    id_persona = db.Column(db.Integer, primary_key=True)
    apellido_paterno = db.Column(db.String(255))
    apellido_materno = db.Column(db.String(255))
    nombres = db.Column(db.String(255))
    fecha_nacimiento = db.Column(db.Date)
    id_tipo_documento = db.Column(db.Integer, db.ForeignKey("tipo_documento.id_tipo_documento"))
    ndocumento = db.Column(db.String(255))
    direccion = db.Column(db.String(255))
    idubigeo = db.Column(db.String(255), db.ForeignKey("ubigeo.idubigeo"))

    def __init__ (self, apellido_paterno, apellido_materno, nombres, fecha_nacimiento, id_tipo_documento, ndocumento, direccion, idubigeo):
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.nombres = nombres
        self.fecha_nacimiento = fecha_nacimiento
        self.id_tipo_documento = id_tipo_documento
        self.ndocumento = ndocumento
        self.direccion = direccion
        self.idubigeo = idubigeo
