from django.contrib import admin
from .models import CategoriaUnormal,CategoriaUtrabajador,solicitudtrabajo,solicitudayuda,recepciontrabajo

admin.site.register(CategoriaUtrabajador)
admin.site.register(CategoriaUnormal)
admin.site.register(solicitudtrabajo)
admin.site.register(solicitudayuda)
admin.site.register(recepciontrabajo)
# Register your models here.
