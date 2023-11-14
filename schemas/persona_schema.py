from utils.ma import ma
from models.persona import Persona

class PersonaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Persona
        fields = ('id_persona', 'apellido_paterno', 'apellido_materno', 'nombres', 'fecha_nacimiento', 'id_tipo_documento', 'ndocumento', 'direccion', 'idubigeo')

persona_schema = PersonaSchema()
personas_schema = PersonaSchema(many=True)