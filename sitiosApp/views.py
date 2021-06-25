from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as login_aut
from django.contrib.auth.decorators import login_required
def inicio(request):
    solicitud = solicitudtrabajo.objects.all()
    contexto = {"trabajo":solicitud}
    return render(request, 'index.html', contexto)
def base(request):
    return render(request, 'base.html')
def sol_ayu(request):
    solicitud = solicitudayuda.objects.all()
    contexto = {"ayuda":solicitud}
    return render(request, 'sol_ayu.html',contexto)
def mot_rec(request):
    return render(request, 'mot_rec.html')
def ayuda(request):
    if(request.POST):
        correo = request.POST.get("txtEmail")
        telefono = request.POST.get("txtTel")
        descripcion = request.POST.get("txtDesc")
        imagen = request.FILES.get("txtFile")
        solicitud = solicitudayuda(
            correo= correo,
            telefono= telefono,
            descripcion= descripcion,
            imagen=imagen
        )
        contexto={"mensaje":"Solictud recibida"}
        solicitud.save()
        return render(request,"ayuda.html", contexto)
    return render(request, 'ayuda.html')
def login(request):
    if request.POST:
        email = request.POST.get("txtEmail")
        contra = request.POST.get("txtPasslog")
        us = authenticate(request, username=email, password=contra)
        if us is not None and us.is_active:
            login_aut(request,us)
            return render(request, 'index.html')
        else:
            contexto= {"mensaje":"Email o Contraseña incorrecto"}
            return render(request, 'login.html', contexto)

    return render(request, 'login.html')
def salir(request):
    logout(request)
    solicitud = solicitudtrabajo.objects.all()
    contexto = {"trabajo":solicitud}
    return render(request, 'index.html', contexto)
def register(request):
    if(request.POST):
        nombre = request.POST.get('txtNombre')
        email = request.POST.get('txtEmail')
        passw = request.POST.get('txtPasslog')
        usuario = CategoriaUnormal(
            nombre= nombre,
            email= email,
            contrasena= passw
        )
        contexto ={"mensaje":"Registrado con exito"}
        usuario.save()
        nuevo_usuario = User()
        nuevo_usuario.username = email
        nuevo_usuario.set_password(passw)
        nuevo_usuario.first_name = nombre
        nuevo_usuario.save()
        return render(request, 'register.html', contexto)
    return render(request, 'register.html')

def anterior(request):
    solicitud = solicitudtrabajo.objects.all()
    categorias = categoria.objects.all()
    contexto = {"trabajo":solicitud,"categorias":categorias}
    return render(request, 'trabanterior.html',contexto)
def frabajo(request, id):
    contexto={"solicitud":""}
    soli = solicitudtrabajo.objects.get(correo=id)
    atencion = recepciontrabajo.objects.get(solicitudt=soli)
    #if(atencion.solicitudt==soli.correo):
     #   contexto = {"solicitud":soli,"ate":atencion}*/
    contexto = {"solicitud":soli,"ate":atencion}
    return render(request, 'ficha_trabajo.html', contexto)
def cuenta(request):
    return render(request, 'cuenta.html')

def register_work(request):
    if(request.POST):
        rut = request.POST.get('txtRut')
        nombre = request.POST.get('txtNombre')
        email = request.POST.get('txtEmail')
        passw = request.POST.get('txtPasslog')
        esp = request.POST.get('txtEsp')
        tel = request.POST.get('txtTel')
        usuario = CategoriaUtrabajador(
            rut = rut,
            nombre = nombre,
            email= email,
            contrasena= passw,
            especialidad=esp,
            telefono=tel
        )
        contexto ={"mensaje":"Registrado con exito"}
        usuario.save()
        return render(request, 'register_work.html', contexto)
    return render(request, 'register_work.html')
def sol_tra(request):
    solicitud = solicitudtrabajo.objects.all()
    contexto = {"trabajo":solicitud}
    return render(request, 'sol_tra.html', contexto)
def mot_rec_tr(request):
    return render(request, 'mot_rec_tr.html')
def sol_ser(request):
    if(request.POST):
        correo = request.POST.get("txtEmail")
        telefono = request.POST.get("txtTel")
        descripcion = request.POST.get("txtDesc")
        imagen = request.FILES.get("txtFile")
        solicitud = solicitudtrabajo(
            correo= correo,
            telefono= telefono,
            descripcion= descripcion,
            imagen=imagen
        )
        contexto={"mensaje":"Solictud recibida"}
        solicitud.save()
        return render(request,"sol_ser.html", contexto)
    return render(request, 'sol_ser.html')
def admini(request):
    return render(request, 'admin.html')
# Create your views here.
