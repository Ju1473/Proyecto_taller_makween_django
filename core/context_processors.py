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