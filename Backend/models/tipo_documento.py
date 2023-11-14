from utils.db import db

class TipoDocumento(db.Model):
    __tablename__ = "tipo_documento"

    id_tipo_documento = db.Column(db.SmallInteger, primary_key=True)
    descripcion = db.Column(db.String(255))

    def __init__(self, descripcion):
        self.descripcion = descripcion
