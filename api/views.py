from django.shortcuts import render
from sitiosApp.models import solicitudtrabajo
from sitiosApp.models import CategoriaUtrabajador
from sitiosApp.models import solicitudayuda
from .serializers import SolTrabSerializers
from .serializers import TrabSerializers
from .serializers import AyudaSerializers
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
#API NUMERO 2 DESDE TRABAJOS ANTERIORES, INGRESO DE NUEVOS SERVICIOS
class SolTrabSearchViewSet(generics.ListAPIView):
    serializer_class = SolTrabSerializers
    def get_queryset(self):
        #kwargs = recuperar parametro ['']
        correo = self.kwargs['correo']
        #retorna la info solicitada
        #se puede cambiar el parametro en self.kwargs y el filtro para asi poder realizar otro...
        #...tipo de busqued
        return solicitudtrabajo.objects.filter(correo=correo)


#API NUMERO 1 DESDE INDEX
#Vista de datos de trabajadores
class TrabdorViewSet(generics.ListAPIView):
    queryset =CategoriaUtrabajador.objects.all()
    serializer_class = TrabSerializers

#API NUMERO 3 DESDE CUENTA DE USUARIO, INGRESO DE NUEVAS PETICIONES DE AYUDA
class SolTrabCreateViewSet(generics.ListCreateAPIView):
    queryset = solicitudtrabajo.objects.all()
    serializer_class = SolTrabSerializers




#Este no funciono como deseaba fui a por otro
#class TrabSearchViewSet(generics.ListAPIView):
#    serializer_class = TrabSerializers
#    def get_queryset(self):
#        nombre = self.kwargs['nombre']
#        return CategoriaUtrabajador.objects.filter(nombre=nombre) 