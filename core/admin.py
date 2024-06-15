from django.contrib import admin
from .models import *
from admin_confirm import AdminConfirmMixin
from django.contrib.admin import ModelAdmin

class TipoServicioModelAdmin(AdminConfirmMixin, ModelAdmin):
        confirm_change = True
        confirmation_fields = ['descripcion']

class TrabajoModelAdmin(AdminConfirmMixin, ModelAdmin):
        confirm_change = True
        confirmation_fields = ['nombre_trabajo', 'diagnostico', 'fecha', 'mecanico', 'materiales', 'foto', 'servicio', 'estado_publicacion', 'comentario_admin', 'cliente']

class ClienteModelAdmin(AdminConfirmMixin, ModelAdmin):
        confirm_change = True
        confirmation_fields = ['nombre_cliente', 'apellido_mecanico', 'correo_mecanico', 'password_mecanico', 'foto_mecanico']

class MecanicoModelAdmin(AdminConfirmMixin, ModelAdmin):
        confirm_change = True
        confirmation_fields = ['nombre_mecanico', 'apellido_mecanico', 'correo_mecanico', 'password_mecanico', 'foto_mecanico']

class MecanicoModelAdmin(AdminConfirmMixin, ModelAdmin):
        confirm_change = True
        confirmation_fields = ['nombre_mecanico', 'apellido_mecanico', 'correo_mecanico', 'password_mecanico', 'foto_mecanico']

class MecanicoModelAdmin(AdminConfirmMixin, ModelAdmin):
        confirm_change = True
        confirmation_fields = ['nombre_mecanico', 'apellido_mecanico', 'correo_mecanico', 'password_mecanico', 'foto_mecanico']

class MecanicoModelAdmin(AdminConfirmMixin, ModelAdmin):
        confirm_change = True
        confirmation_fields = ['nombre_mecanico', 'apellido_mecanico', 'correo_mecanico', 'password_mecanico', 'foto_mecanico']


# Register your models here.
admin.site.register(TipoServicio, TipoServicioModelAdmin)
admin.site.register(Trabajo, TrabajoModelAdmin)
admin.site.register(Cliente)
admin.site.register(TipoConsulta)
admin.site.register(Contacto)
admin.site.register(Mecanico, MecanicoModelAdmin)
admin.site.register(Reserva)
admin.site.register(Carrito)