from django.shortcuts import render
from sitiosApp.models import solicitudtrabajo
from .serializers import SolTrabSerializers
from rest_framework import generics
# Create your views here.
class SolTrabViewSet(generics.ListAPIView):
    queryset =solicitudtrabajo.objects.all()
    serializer_class = SolTrabSerializers