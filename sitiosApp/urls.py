from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',inicio, name='IND'),
    path('BASE', base, name='BASE'),
    path('SOLAYU', sol_ayu, name='SOLAYU'),
    path('MOTREC', mot_rec, name="MOTREC"),
    path('AYUDA',ayuda, name="AYUDA"),
    path('LOGIN',login, name="LOGIN"),
    path('REGISTER',register, name="REGISTER"),
    path('ANTERIORES',anterior, name='ANTERIORES'),
    path('FICHATRABAJO/<id>/',frabajo, name='FICHATRABAJO'),
    path('CUENTA', cuenta, name='CUENTA'),
    path('REGWORK',register_work, name='REGWORK'),
    path('SOLTRA',sol_tra, name='SOLTRA'),
    path('MTTR',mot_rec_tr, name='MTTR'),
    path('SOLSER',sol_ser,name="SOLSER"),
    path('ADM',admini,name="ADM"),
    path('SALIR', salir, name="SALIR"),
    path('FILTRAR', filtrar_cate, name="FILTRAR"),
]