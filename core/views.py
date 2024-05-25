from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def index(request):
    trabajos = Trabajo.objects.filter(estado_publicacion="A").order_by('-id')[:3]
    user = request.user
    if user.is_authenticated:
        if user.groups.filter(name='Mecánico').exists():  # Verifica si el usuario es un mecánico
            try:
                mecanico = Mecanico.objects.get(correo_mecanico=user.email)
            except Mecanico.DoesNotExist:
                mecanico = None
            aux = {
                'lista' : trabajos,
                'mecanico' : mecanico
            }
        elif user.groups.filter(name='Cliente').exists():  # Verifica si el usuario es un cliente
            try:
                cliente = Cliente.objects.get(correo_cliente=user.email)
            except Cliente.DoesNotExist:
                cliente = None
            aux = {
                'lista' : trabajos,
                'cliente' : cliente
            }
    else:
        aux = {
            'lista' : trabajos
        }
    return render(request, 'core/index.html', aux)

def nosotros(request):
    mecanicos = Mecanico.objects.all()
    aux = {
        'lista' : mecanicos
    }

    return render(request, 'core/nosotros.html', aux)

def servicios(request):
    tiposervicios = TipoServicio.objects.all()
    aux = {
        'lista' : tiposervicios
    }

    return render(request, 'core/servicios.html', aux)

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
            messages.success(request, "Bienvenido")
            return redirect(to="index")
        else:
            aux['form'] = formulario
            messages.error(request, "No se pudo iniciar sesión")
    
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
            messages.success(request, 'Usuario creado correctamente!')
            return redirect(to="index")
        else:
            aux['form'] = formulario
            messages.error(request, 'No se pudo registrar')

    return render(request, 'registration/register.html', aux)

@login_required
def mecanicos(request):
    mecanicos = Mecanico.objects.all()
    for mec in mecanicos:
        mec.cant_mantenciones_mec = mec.calcular_cantidad_trabajos()
        mec.save()
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
        formulario = MecanicoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mecánico almacenado correctamente!")
        else:
            aux['form'] = formulario
            messages.error(request, "No se pudo almacenar el mecánico!")

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
            messages.success(request, "Mecánico modificado correctamente!")
        else:
            aux['form'] = formulario
            messages.error(request, "No se pudo modificar el mecánico!")

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
            messages.success(request, "Proyecto almacenado correctamente!")
        else:
            aux['form'] = formulario
            messages.error(request, "No se pudo almacenar el proyecto!")

    return render(request, 'core/mecanicos/crud_proyecto/add.html', aux)

@permission_required('core.view_trabajo')
def trabajos(request):
    trabajos = Trabajo.objects.all().order_by('-id')
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
            messages.success(request, "Trabajo aplicado correctamente!")
        else:
            aux['form'] = formulario
            messages.error(request, "No se pudo aplicar el estado de trabajo!")

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

def listarreservas(request):
    reservas = Reserva.objects.all().order_by('-id')
    aux = {
        'lista' : reservas
    }

    return render(request, 'core/mecanicos/reservas.html', aux)

@login_required
def reserva(request):
    aux = {
        'form' : ReservaForm
    }

    if request.method == 'POST':
        formulario = ReservaForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = 'Reservado'
        else:
            aux['form'] = formulario
            
            aux['msj'] = 'No se pudo reservar'

    return render(request, 'core/reserva.html', aux)

def reservaupdate(request, id):
    reservas = Reserva.objects.get(id=id)
    aux = {
        'form' : ReservaAdminForm(instance=reservas)
    }

    if request.method == 'POST':
        formulario = ReservaAdminForm(data=request.POST, instance=reservas)
        if formulario.is_valid():
            formulario.save()
            aux['form'] = formulario
            messages.success(request, "Reserva aplicado correctamente!")
        else:
            aux['form'] = formulario
            messages.error(request, "No se pudo aplicar la reserva!")

    return render(request, 'core/mecanicos/reservaupdate.html', aux)

def categoria_trabajo(request, id):
    tipo_servicio = get_object_or_404(TipoServicio, id=id)
    trabajos = Trabajo.objects.filter(servicio=tipo_servicio, estado_publicacion='A').order_by('-id')
    
    context = {
        'tipo_servicio': tipo_servicio,
        'trabajos': trabajos
    }
    
    return render(request, 'core/cat_trabajo.html', context)

def mecanico_trabajo(request, id):
    mecanico = get_object_or_404(Mecanico, id=id)
    trabajos = Trabajo.objects.filter(mecanico=mecanico, estado_publicacion='A').order_by('-id')

    context = {
        'mecanico' : mecanico,
        'trabajos' : trabajos
    }

    return render(request, 'core/mec_trabajo.html', context)


def buscador(request):
    form = TrabajoSearchForm()
    trabajos = []

    if 'query' in request.GET:
        form = TrabajoSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            trabajos = Trabajo.objects.filter(
                Q(nombre_trabajo__icontains=query) |
                Q(diagnostico__icontains=query) |
                Q(mecanico__nombre_mecanico__icontains=query) |
                Q(fecha__icontains=query) |
                Q(materiales__icontains=query) |
                Q(servicio__descripcion__icontains=query)
            )

    return render(request, 'core/buscador.html', {'form': form, 'trabajos': trabajos})

def pagina_404(request, exception=None):
    return render(request, 'core/404.html', status=404)


def clientes(request):
    clientes = Cliente.objects.all()
    for cli in clientes:
        cli.cant_mantenciones_cli = cli.calcular_cantidad_trabajos()
        cli.save()
    aux = {
        'lista' : clientes
    }
    return render(request, 'core/mecanicos/crud_clientes/listar.html', aux)