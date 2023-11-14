from utils.ma import ma
from models.rol import Rol

class RolSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Rol
        fields = ('id_rol', 'descripcion')

rol_schema = RolSchema()
roles_schema = RolSchema(many=True)