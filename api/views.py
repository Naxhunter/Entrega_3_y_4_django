from django.shortcuts import render
from sitiosApp.models import solicitudtrabajo
from sitiosApp.models import CategoriaUtrabajador
from .serializers import SolTrabSerializers
from .serializers import TrabSerializers
from rest_framework import generics
# Crear las vistas a presentar en la API

#Vista datos de las solicitudes de servicio
class SolTrabViewSet(generics.ListAPIView):
    queryset =solicitudtrabajo.objects.all() #Registros a presentar
    serializer_class = SolTrabSerializers #Campos a presentar
#Creacion de solicitudes de servicio + visualizacion de estos Listar + Crear
class SolTrabCreateViewSet(generics.ListCreateAPIView):
    queryset = solicitudtrabajo.objects.all()
    serializer_class = SolTrabSerializers

#Presentar pagina donde se puede buscar una solicitud especifica mediante el correo del usuario
class SolTrabSearchViewSet(generics.ListAPIView):
    serializer_class = SolTrabSerializers
    def get_queryset(self):
        #kwargs = recuperar parametro ['']
        correo = self.kwargs['correo']
        #retorna la info solicitada
        #se puede cambiar el parametro en self.kwargs y el filtro para asi poder realizar otro...
        #...tipo de busqued
        return solicitudtrabajo.objects.filter(correo=correo)


class TrabSearchViewSet(generics.ListAPIView):
    serializer_class = TrabSerializers
    def get_queryset(self):
        email = self.kwargs['email']
        return CategoriaUtrabajador.objects.filter(email=email)