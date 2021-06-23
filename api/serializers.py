from sitiosApp.models import solicitudtrabajo
from rest_framework import serializers

class SolTrabSerializers(serializers.ModelSerializer):
    class Meta:
        model = solicitudtrabajo
        fields = ["correo","telefono","descripcion"]