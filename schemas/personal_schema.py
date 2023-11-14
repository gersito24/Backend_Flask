from utils.ma import ma
from models.personal import Personal

class PersonalSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Personal
        fields = ('id_personal', 'id_persona', 'id_rol', 'fecha_contrato', 'fecha_cese')

personal_schema = PersonalSchema()
personales_schema = PersonalSchema(many=True)