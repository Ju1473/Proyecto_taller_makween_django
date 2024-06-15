from .models import *

def user_info(request):
    user_info = {}
    if request.user.is_authenticated:
        user = request.user
        user_info['user'] = user
        if user.groups.filter(name='Mecánico').exists():
            try:
                mecanico = Mecanico.objects.get(correo_mecanico=user.email)
                user_info['mecanico'] = mecanico
            except Mecanico.DoesNotExist:
                pass
        elif user.groups.filter(name='Cliente').exists():
            try:
                cliente = Cliente.objects.get(correo_cliente=user.email)
                user_info['cliente'] = cliente
            except Cliente.DoesNotExist:
                pass
    return user_info

def carrito_de_compras(request):
    user = request.user

    user_info = {'user': user}

    try:
        carrito = Carrito.objects.get(usuario=user_info['user'])
    except Carrito.DoesNotExist:
        carrito = None

    context = {
        'carrito': carrito,
        'total_car': carrito.total_carrito if carrito else 0,
    }

    return context