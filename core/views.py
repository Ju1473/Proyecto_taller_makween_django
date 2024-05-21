from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
#from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def servicios(request):
    return render(request, 'core/servicios.html')

def contacto(request):
    aux = {
        'form' : ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = 'Enviado'
        else:
            aux['form'] = formulario
            aux['msj'] = 'No se pudo enviar'

    return render(request, 'core/contacto.html', aux)

def login(request):
    aux = {
        'form' : CustomAuthentication()
    }

    if request.method == 'POST':
        formulario = CustomAuthentication(request.POST)
        if formulario.is_valid():
            return redirect(to="index")
        else:
            aux['form'] = formulario
    
    return render(request, 'registration/login.html', aux)

def logout_view(request):
    logout(request)

def register(request):
    aux = {
        'form' : CustomUserCreationForm()
    }
    cliente = Cliente()

    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            group = Group.objects.get(name="Cliente")
            user.groups.add(group)
            cliente.nombre_cliente = user.first_name
            cliente.apellido_cliente = user.last_name
            cliente.correo_cliente = user.email
            cliente.save()
            #messages.success(request, 'Usuario creado correctamente!')
            return redirect(to="index")
        else:
            aux['form'] = formulario
            #messages.error(request, 'No se pudo almacenar')

    return render(request, 'registration/register.html', aux)

@login_required
def mecanicos(request):
    mecanicos = Mecanico.objects.all()
    for mec in mecanicos:
        mec.cant_mantenciones_mec = mec.calcular_cantidad_trabajos()
    aux = {
        'lista' : mecanicos
    }
    return render(request, 'core/mecanicos/crud_mecanico/listar.html', aux)

def galeria(request):
    trabajos = Trabajo.objects.all()
    aux = {
        'lista' : trabajos
    }
    return render(request, 'core/galeria.html',aux)

def not_found(request):
    return render(request, 'core/404.html')

@permission_required('core.add_mecanico')
def mecanicoadd(request):
    aux = {
        'form' : MecanicoForm()
    }

    if request.method == 'POST':
        formulario = MecanicoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = 'Mecánico almacenado correctamente!'
        else:
            aux['form'] = formulario
            aux['msj'] = 'No se pudo almacenar el mecánico!'


    return render(request, 'core/mecanicos/crud_mecanico/add.html', aux)

@permission_required('core.change_mecanico')
def mecanicoupdate(request, id):
    mecanico = Mecanico.objects.get(id=id)
    aux = {
        'form' : MecanicoForm(instance=mecanico)
    }

    if request.method == 'POST':
        formulario = MecanicoForm(data=request.POST, instance=mecanico)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            aux['msj'] = 'Mecánico modificado correctamente!'
        else:
            aux['form'] = formulario
            aux['msj'] = 'No se pudo modificar el mecánico!'

    return render(request, 'core/mecanicos/crud_mecanico/update.html', aux)

@permission_required('core.delete_mecanico')
def mecanicodelete(request, id):
    mecanico = Mecanico.objects.get(id=id)
    mecanico.delete()

    return redirect(to="mecanicos")

@permission_required('core.add_trabajo')
def trabajoadd(request):
    aux = {
        'form' : TrabajoForm()
    }

    if request.method == 'POST':
        formulario = TrabajoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = 'Proyecto almacenado correctamente!'
        else:
            aux['form'] = formulario
            aux['msj'] = 'No se pudo almacenar el proyecto!'

    return render(request, 'core/mecanicos/crud_proyecto/add.html', aux)

@permission_required('core.view_trabajo')
def trabajos(request):
    trabajos = Trabajo.objects.all()
    aux = {
        'lista' : trabajos
    }

    return render(request, 'core/mecanicos/crud_proyecto/listar.html', aux)

@permission_required('core.change_trabajo')
def trabajoupdate(request, id):
    trabajos = Trabajo.objects.get(id=id)
    aux = {
        'form' : TrabajoAdminForm(instance=trabajos)
    }

    if request.method == 'POST':
        formulario = TrabajoAdminForm(data=request.POST, instance=trabajos)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            aux['msj'] = 'Trabajo aplicado correctamente!'
        else:
            aux['form'] = formulario
            aux['msj'] = 'No se pudo aplicar el estado de trabajo!'

    return render(request, 'core/mecanicos/crud_proyecto/update.html', aux)

def trabajo(request, id):
    trabajo = Trabajo.objects.get(id=id,estado_publicacion='A')
    aux = {
        'lista' : trabajo
    }
    return render(request, 'core/trabajo.html', aux)

def listarconsultas(request):
    consultas = Contacto.objects.all()
    aux = {
        'lista' : consultas
    }

    return render(request, 'core/mecanicos/consultas.html', aux)