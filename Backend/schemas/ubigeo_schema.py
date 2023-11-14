from utils.ma import ma
from models.ubigeo import Ubigeo

class UbigeoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Ubigeo
        fields = ('idubigeo', 'departamento', 'provincia', 'distrito', 'superficie', 'altitud', 'latitud', 'longitud')

ubigeo_schema = UbigeoSchema()
ubigeos_schema = UbigeoSchema(many=True)