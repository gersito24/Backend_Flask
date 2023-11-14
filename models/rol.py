from utils.db import db

class Rol(db.Model):
    __tablename__ = "rol"

    id_rol = db.Column(db.SmallInteger, primary_key=True)
    descripcion = db.Column(db.String(255))

    def __init__(self, id_rol, descripcion):
        self.id_rol = id_rol
        self.descripcion = descripcion

