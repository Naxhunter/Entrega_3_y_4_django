from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class CategoriaUnormal(models.Model):
    email= models.CharField(primary_key=True, max_length=30)
    nombre= models.CharField(max_length=30)
    contrasena= models.CharField(max_length=30)
    def __str__(self):
        return self.nombre
class CategoriaUtrabajador(models.Model):
    rut= models.CharField(primary_key=True,max_length=30)
    email= models.CharField(max_length=30)
    nombre= models.CharField(max_length=30)
    contrasena= models.CharField(max_length=30)
    especialidad= models.CharField(max_length=30)
    telefono= models.IntegerField()
    def __str__(self):
        return self.nombre
class solicitudtrabajo(models.Model):
    correo=models.CharField(primary_key=True, max_length=30)
    telefono=models.IntegerField()
    descripcion=models.TextField(max_length=350)
    imagen=models.ImageField(upload_to='solitudest', null=True)
    def __str__(self):
        return self.correo
class solicitudayuda(models.Model):
    correo=models.CharField(primary_key=True, max_length=30)
    telefono=models.IntegerField()
    descripcion=models.TextField(max_length=350)
    imagen=models.ImageField(upload_to='solitudesa', null=True)
    def __str__(self):
        return self.correo
class categoria(models.Model):
    num_unico=models.IntegerField(primary_key=True)
    trabajo_cate=models.CharField(max_length=150)
    def __str__(self):
        return self.trabajo_cate
class recepciontrabajo(models.Model):
    num_unico=models.IntegerField(primary_key=True)
    fecha=models.CharField(max_length=30)
    tipo_de_trabajo=models.CharField(max_length=100)
    comentarios = models.CharField(max_length=50)
    materiales = models.CharField(max_length=200)
    solicitudt = models.ForeignKey(solicitudtrabajo, on_delete=models.CASCADE)
    trabajador = models.ForeignKey(CategoriaUtrabajador, on_delete=models.CASCADE)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.fecha

