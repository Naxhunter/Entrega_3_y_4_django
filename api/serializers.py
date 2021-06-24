from sitiosApp.models import solicitudtrabajo
from sitiosApp.models import CategoriaUtrabajador
from rest_framework import serializers

#indicar la clase que contendra el modelo a serializar con la lista de sus campos
class SolTrabSerializers(serializers.ModelSerializer):
    class Meta:
        model = solicitudtrabajo #modelo a serializar
        fields = ["correo","telefono","descripcion","imagen"] #campos

class TrabSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoriaUtrabajador
        field = ["email","nombre","especialidad"]