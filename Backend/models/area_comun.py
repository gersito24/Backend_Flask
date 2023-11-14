from utils.db import db

class AreaComun(db.Model):
    __tablename__ = "area_comun"

    id_area_comun = db.Column(db.SmallInteger, primary_key=True)
    descripcion = db.Column(db.String(255))

    def __init__(self, descripcion):
        self.descripcion = descripcion
