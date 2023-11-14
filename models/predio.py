from utils.db import db

class Predio(db.Model):
    __tablename__ = "predio"

    id_predio = db.Column(db.Integer, primary_key=True)
    id_tipo_predio = db.Column(db.Integer, db.ForeignKey("tipo_predio.id_tipo_predio"))
    descripcion = db.Column(db.String(255))
    ruc = db.Column(db.String(255))
    telefono = db.Column(db.String(255))
    correo = db.Column(db.String(255))
    direccion = db.Column(db.String(255))
    idubigeo = db.Column(db.String(255), db.ForeignKey("ubigeo.idubigeo"))
    id_persona = db.Column(db.Integer, db.ForeignKey("persona.id_persona"))

    def __init__(self, id_tipo_predio, descripcion, ruc, telefono, correo, direccion, idubigeo, id_persona):
        self.id_tipo_predio = id_tipo_predio
        self.descripcion = descripcion
        self.ruc = ruc
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.idubigeo = idubigeo
        self.id_persona = id_persona
