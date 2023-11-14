from utils.db import db

class Servicio(db.Model):
    __tablename__ = "servicio"

    id_servicio = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(255))

    def __init__(self, descripcion):
        self.descripcion = descripcion

