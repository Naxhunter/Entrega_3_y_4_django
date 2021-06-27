from django.contrib import admin
from .models import CategoriaUnormal,CategoriaUtrabajador,solicitudtrabajo,solicitudayuda,recepciontrabajo,categoria,perfilusuario

admin.site.register(CategoriaUtrabajador)
admin.site.register(CategoriaUnormal)
admin.site.register(solicitudtrabajo)
admin.site.register(solicitudayuda)
admin.site.register(recepciontrabajo)
admin.site.register(categoria)
admin.site.register(perfilusuario)
# Register your models here.
