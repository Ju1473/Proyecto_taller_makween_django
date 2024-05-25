from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class MecanicoForm(ModelForm):

    class Meta:
        model = Mecanico
        fields = ['nombre_mecanico', 'apellido_mecanico', 'correo_mecanico', 'password_mecanico', 'foto_mecanico']
        labels = {
            'nombre_mecanico': 'Nombre',
            'apellido_mecanico': 'Apellido',
            'correo_mecanico': 'Correo electrónico',
            'password_mecanico': 'Contraseña',
            'foto_mecanico' : 'Foto de Perfil'
        }

class TrabajoForm(ModelForm):

    class Meta:
        model = Trabajo
        fields = ['nombre_trabajo', 'diagnostico', 'mecanico', 'materiales', 'foto', 'servicio','cliente']
        labels = {
            'nombre_trabajo': 'Nombre del trabajo',
            'diagnostico': 'Diagnóstico del trabajo',
            'mecanico': 'Mecánico responsable',
            'materiales': 'Materiales usados',
            'servicio': 'Tipo de Servicio',
        }

class ClienteForm(ModelForm):
    
    class Meta:
        model = Cliente
        fields = ['nombre_cliente', 'apellido_cliente', 'correo_cliente']

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class CustomAuthentication(AuthenticationForm):

    class Meta:
        model = User
        fields = ['username', 'password1']

class ContactoForm(ModelForm):
    
    class Meta:
        model = Contacto
        fields = ['nombre_apellido','email_contacto','telefono','consulta','info_adicional']
        labels = {
            'nombre_apellido' : 'Nombre y Apellido',
            'email_contacto' : 'Email',
            'telefono' : 'Teléfono',
            'info_adicional': 'Información Adicional',
        }

class TrabajoAdminForm(ModelForm):

    class Meta:
        model = Trabajo
        fields = ['nombre_trabajo', 'diagnostico', 'mecanico', 'materiales', 'foto', 'servicio', 'estado_publicacion', 'comentario_admin', 'cliente']
        labels = {
            'nombre_trabajo': 'Nombre del trabajo',
            'diagnostico': 'Descripción del diagnóstico',
            'mecanico': 'Mecánico responsable',
            'materiales': 'Materiales usados',
            'servicio': 'Tipo de Servicio',
            'estado_publicacion' : 'Estado de publicación',
            'comentario_admin' : 'Comentario (motivo de rechazo)'
        }

class ReservaForm(ModelForm):

    class Meta:
        model = Reserva
        fields = ['nombre_apellido','email_reserva','telefono','tipo_servicio']
        labels = {
            'nombre_apellido' : 'Nombre y Apellido',
            'email_reserva' : 'Correo electrónico',
            'telefono' : 'Teléfono',
            'tipo_servicio' : 'Servicio'
        }

class ReservaAdminForm(ModelForm):

    class Meta:
        model = Reserva
        fields = ['estado_reserva', 'mecanico']
        labels = {
            'estado_reserva' : 'Petición',
            'mecanico' : 'Mecánico responsable'
        }

class TrabajoSearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100)