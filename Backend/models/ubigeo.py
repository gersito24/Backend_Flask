from utils.db import db

class Ubigeo(db.Model):
    __tablename__ = "ubigeo"

    idubigeo = db.Column(db.String(255), primary_key=True)
    departamento = db.Column(db.String(255))
    provincia = db.Column(db.String(255))
    distrito = db.Column(db.String(255))
    superficie = db.Column(db.Numeric(10, 4))
    altitud = db.Column(db.Numeric(10, 4))
    latitud = db.Column(db.Numeric(10, 4))
    longitud = db.Column(db.Numeric(10, 4))

    def __init__(self, departamento, provincia, distrito, superficie, altitud, latitud, longitud):
        self.departamento = departamento
        self.provincia = provincia
        self.distrito = distrito
        self.superficie = superficie
        self.altitud = altitud
        self.latitud = latitud
        self.longitud = longitud
