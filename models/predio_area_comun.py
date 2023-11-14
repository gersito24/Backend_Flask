from utils.db import db

class PredioAreaComun(db.Model):
    __tablename__ = "predio_area_comun"

    id_predio = db.Column(db.SmallInteger, primary_key=True)
    id_area_comun = db.Column(db.SmallInteger, db.ForeignKey("area_comun.id_area_comun"), primary_key=True)
    codigo = db.Column(db.Integer)
    area = db.Column(db.Float)

    def __init__(self, id_predio, id_area_comun, codigo, area):
        self.id_predio = id_predio
        self.id_area_comun = id_area_comun
        self.codigo = codigo
        self.area = area
