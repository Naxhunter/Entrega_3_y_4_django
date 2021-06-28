from django.shortcuts import render
from requests.sessions import Request
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as login_aut
from django.contrib.auth.decorators import login_required
#Gestion peticiones HTTP
import requests
def inicio(request):
    solicitud = solicitudtrabajo.objects.filter(publicar=True)
    contexto = {"trabajo":solicitud}
#Consumo de API api/trabuscar
    response = requests.get('http://127.0.0.1:8000/api/trabajador/')
    trabajapi = response.json()
    contexto["trabajapi"] = trabajapi
    #----------------------------
    return render(request, 'index.html', contexto)
def base(request):
    return render(request, 'base.html')
@login_required(login_url='/LOGIN')
def sol_ayu(request):
    solicitud = solicitudayuda.objects.all()
    contexto = {"ayuda":solicitud}
    response = requests.get('http://127.0.0.1:8000/api/solayuda/')
    solaapi = response.json()
    contexto["solaapi"] = solaapi
    return render(request, 'sol_ayu.html',contexto)
@login_required(login_url='/LOGIN')
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
@login_required(login_url='/LOGIN')
def salir(request):
    logout(request)
    solicitud = solicitudtrabajo.objects.filter(publicar=True)
    contexto = {"trabajo":solicitud}
    return render(request, 'index.html', contexto)
def register(request):
    if(request.POST):
        nombre = request.POST.get('txtNombre')
        email = request.POST.get('txtEmail')
        passw = request.POST.get('txtPasslog')
        desc = request.POST.get('txtDesc')
        usuario = CategoriaUnormal(
            nombre= nombre,
            email= email,
            contrasena= passw,
            descripcion = desc
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
    solicitud = solicitudtrabajo.objects.filter(publicar=True)
    categorias = categoria.objects.all()
    cantidad_s = solicitudtrabajo.objects.filter(publicar=True).count()
    cantidad_c = categoria.objects.all().count()
    contexto = {"trabajo":solicitud,"categorias":categorias,"cants":cantidad_s,"cantc":cantidad_c}
    response = requests.get('http://127.0.0.1:8000/api/categorias/')
    catapi = response.json()
    contexto["catapi"]= catapi
    return render(request, 'trabanterior.html',contexto)
def filtrar_nombre(request):
    categorias = categoria.objects.all()
    trabajadores = CategoriaUtrabajador.objects.all()
    recepciones = recepciontrabajo.objects.all()
    if request.POST:
        trabajador = request.POST.get("txtNombre")
        obj_trabajador = CategoriaUtrabajador.objects.get(nombre=trabajador)
        recepciones = recepciontrabajo.objects.filter(trabajador=obj_trabajador)
    contexto = {"trabajadores":trabajadores,"recepciones":recepciones, "categorias":categorias}
    return render(request, 'trabanterior.html', contexto)
def filtrar_cate(request):
    solicitud = solicitudtrabajo.objects.all()
    categorias = categoria.objects.all()
    recepciones = recepciontrabajo.objects.all()
    if request.POST:
        cate = request.POST.get("cboCategoria")
        obj_categoria = categoria.objects.get(num_unico=cate)
        recepciones = recepciontrabajo.objects.filter(categoria=obj_categoria)
    contexto = {"categorias":categorias, "recepcion":recepciones}
    return render(request, 'trabanterior.html',contexto)
def frabajo(request, id):
    contexto={"solicitud":""}
    soli = solicitudtrabajo.objects.get(correo=id)
    atencion = recepciontrabajo.objects.get(solicitudt=soli)
    contexto = {"solicitud":soli,"ate":atencion}
    return render(request, 'ficha_trabajo.html', contexto)
@login_required(login_url='/LOGIN')
def cuenta(request):
    user = User.objects.get(username=request.user.username)
    #rut = User.objects.get(last_name=request.user.last_name)
    #nombre = User.objects.get(first_name=request.user.first_name)
    mantenciones = recepciontrabajo.objects.filter(trabajador=request.user.last_name).count()
    especialidad = CategoriaUtrabajador.objects.filter(email=request.user.username)
    serv_sol = solicitudtrabajo.objects.filter(correo=request.user.username).count()
    imagen_poner = perfilusuario.objects.filter(nombre_perf=user)
    descripcion = CategoriaUnormal.objects.filter(email=request.user.username)
    contexto = {"imagenp":imagen_poner, "mantencion":mantenciones,"servicios":serv_sol, "especial":especialidad, "descri":descripcion}
    #contexto = {"imagenp":imagen_poner}
    if request.POST:
        imagen = request.FILES.get("txtFile")
        perfil_u = perfilusuario(
        nombre_perf = user,
        imagen = imagen
        )
        imagen_poner = perfilusuario.objects.filter(nombre_perf=user)
        contexto = {"mensaje":"imagen subida con éxito","imagenp":imagen_poner,"mantencion":mantenciones,"servicios":serv_sol, "especialidad":especialidad, "descri":descripcion}
        #contexto = {"mensaje":"imagen subida con éxito","imagenp":imagen_poner}
        perfil_u.save()

    return render(request, 'cuenta.html', contexto)
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
        nuevo_usuario = User()
        nuevo_usuario.username = email
        nuevo_usuario.set_password(passw)
        nuevo_usuario.first_name = nombre
        nuevo_usuario.last_name = rut
        nuevo_usuario.save()
        contexto ={"mensaje":"Registrado con exito"}
        usuario.save()
        return render(request, 'register_work.html', contexto)
    return render(request, 'register_work.html')
@login_required(login_url='/LOGIN')
def sol_tra(request):
    solicitud = solicitudtrabajo.objects.all()
    contexto = {"trabajo":solicitud}
    response = requests.get('http://127.0.0.1:8000/api/solitrab/')
    soltapi = response.json()
    contexto["soltapi"] = soltapi
    return render(request, 'sol_tra.html', contexto)
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
@login_required(login_url='/LOGIN')
def admini(request):
    return render(request, 'admin.html')
# Create your views here.
@login_required(login_url='/LOGIN')
def eliminar(request, id):
    try:
        borrar = solicitudtrabajo.objects.get(correo=id)
        borrar.delete()
        mensaje = "Solicitud eliminada."
        solicitud = solicitudtrabajo.objects.all()
        contexto = {"trabajo":solicitud,"elimino":mensaje}
        response = requests.get('http://127.0.0.1:8000/api/solitrab/')
        soltapi = response.json()
        contexto["soltapi"] = soltapi
    except:
        mensaje = "No elimino."
        solicitud = solicitudtrabajo.objects.all()
        contexto = {"trabajo":solicitud,"elimino":mensaje}
        response = requests.get('http://127.0.0.1:8000/api/solitrab/')
        soltapi = response.json()
        contexto["soltapi"] = soltapi
    return render(request, 'sol_tra.html', contexto)
@login_required(login_url='/LOGIN')
def publica(request, id):
    actualizar = solicitudtrabajo.objects.get(correo=id)
    actualizar.publicar=True
    actualizar.save()
    solicitud = solicitudtrabajo.objects.all()
    mensaje = "publicado"
    contexto = {"trabajo":solicitud,"hecho":mensaje}
    response = requests.get('http://127.0.0.1:8000/api/solitrab/')
    soltapi = response.json()
    contexto["soltapi"] = soltapi
    return render(request, 'sol_tra.html',contexto)

@login_required(login_url='/LOGIN')
def modificar(request, id):
    try:
        modific = solicitudtrabajo.objects.get(correo=id) 
        contexto = {"modifi":modific}
        return render(request, 'modificar.html', contexto)
    except:
        mensaje = "No encontro solicitud."
        solicitud = solicitudtrabajo.objects.all()
        contexto = {"trabajo":solicitud,"modific":mensaje}
        response = requests.get('http://127.0.0.1:8000/api/solitrab/')
        soltapi = response.json()
        contexto["soltapi"] = soltapi
    
    return render(request, 'sol_tra.html', contexto)
@login_required(login_url='/LOGIN')
def modif_sol(request):
    mensaje = ""
    if(request.POST):
        correo = request.POST.get("txtEmail")
        telefono = request.POST.get("txtTel")
        descripcion = request.POST.get("txtDesc")
        imagen = request.FILES.get("txtFile")
        try:
            actualizar = solicitudtrabajo.objects.get(correo=correo)
            actualizar.telefono=telefono
            actualizar.descripcion=descripcion
            if imagen is not None:
                actualizar.imagen=imagen
            actualizar.comentario="--"
            actualizar.save()
            mensaje = "Modifico"
        except:
            mensaje = "No modifico"
        contexto={"mensaje":"Solictud recibida","modifico":mensaje}
        return render(request,"modificar.html", contexto)

    contexto={"mensaje":"Solictud recibida","modifico":mensaje}
    return render(request, 'sol_tra.html')   

@login_required(login_url='/LOGIN')
def mot_rec_tr(request, id):#, id):
    modific = solicitudtrabajo.objects.get(correo=id) 
    contexto = {"modifi":modific}
    return render(request, 'mot_rec_tr.html', contexto)

@login_required(login_url='/LOGIN')
def comrec(request):
    mensaje = ""
    if(request.POST):
        email = request.POST.get("txtEmail")
        comentarios = request.POST.get("txtCom")
        try:
            actualizar = solicitudtrabajo.objects.get(correo=email)
            actualizar.comentario=comentarios
            actualizar.save()
            mensaje = "Rechazado"
        except:
            mensaje = "No rechazado"
        contexto={"rechazado":mensaje}
        return render(request,"mot_rec_tr.html", contexto)

    contexto={"rechazo":mensaje}
    return render(request, 'sol_tra.html')

#def cuentamecanico(request, id):
#    soli = User.objects.get(first_name=id)
#    mantenciones = recepciontrabajo.objects.filter(trabajador=soli.user.last_name).count()
#    especialidad = CategoriaUtrabajador.objects.filter(email=soli.user.username)
#    serv_sol = solicitudtrabajo.objects.filter(correo=soli.user.username).count()
#    imagen_poner = perfilusuario.objects.filter(nombre_perf=soli)
#    descripcion = CategoriaUnormal.objects.filter(email=soli.user.username)
#    contexto = {"imagenp":imagen_poner, "mantencion":mantenciones,"servicios":serv_sol, "especial":especialidad, "descri":descripcion}
    
#    return render(request,f"cuenta_busc.html")
