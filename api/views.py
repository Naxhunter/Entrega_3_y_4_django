from django.shortcuts import render
from sitiosApp.models import solicitudtrabajo
from sitiosApp.models import CategoriaUtrabajador
from sitiosApp.models import solicitudayuda
from sitiosApp.models import categoria
from .serializers import SolTrabSerializers
from .serializers import TrabSerializers
from .serializers import AyudaSerializers
from .serializers import cateSerializers
from rest_framework import generics
# Crear las vistas a presentar en la API


#API NUMERO 1 DESDE INDEX
#Vista de datos de trabajadores
class TrabdorViewSet(generics.ListAPIView):
    queryset =CategoriaUtrabajador.objects.all()
    serializer_class = TrabSerializers


class ayudaViewSet(generics.ListAPIView):
    queryset= solicitudayuda.objects.all()
    serializer_class = AyudaSerializers

class CateViewSet(generics.ListAPIView):
    queryset= categoria.objects.all()
    serializer_class = cateSerializers


#Vista datos de las solicitudes de servicio
class SolTrabViewSet(generics.ListAPIView):
    queryset =solicitudtrabajo.objects.all() #Registros a presentar
    serializer_class = SolTrabSerializers #Campos a presentar