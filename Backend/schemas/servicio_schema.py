from utils.ma import ma
from models.servicio import Servicio

class ServicioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Servicio
        fields = ('id_servicio', 'descripcion')

servicio_schema = ServicioSchema()
servicios_schema = ServicioSchema(many=True)