from sitiosApp.models import solicitudtrabajo
from sitiosApp.models import CategoriaUtrabajador
from sitiosApp.models import solicitudayuda
from rest_framework import serializers

#indicar la clase que contendra el modelo a serializar con la lista de sus campos
#Solicitud servicio
class SolTrabSerializers(serializers.ModelSerializer):
    class Meta:
        model = solicitudtrabajo #modelo a serializar
        fields = ["correo","telefono","descripcion","imagen"] #campos
#Trabajadores
class TrabSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoriaUtrabajador
        fields = ["email","nombre","especialidad","telefono"]

#Solicitud de ayuda
class AyudaSerializers(serializers.ModelSerializer):
    class Meta:
        model = solicitudayuda
        fields = ["correo","telefono","descripcion","imagen"]