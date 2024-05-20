from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class MecanicoForm(ModelForm):

    class Meta:
        model = Mecanico
        fields = ['nombre_mecanico', 'apellido_mecanico', 'correo_mecanico', 'password_mecanico']
        labels = {
            'nombre_mecanico': 'Nombre',
            'apellido_mecanico': 'Apellido',
            'correo_mecanico': 'Correo electrónico',
            'password_mecanico': 'Contraseña',
        }

class TrabajoForm(ModelForm):

    class Meta:
        model = Trabajo
        fields = ['nombre_trabajo', 'diagnostico', 'mecanico', 'materiales', 'foto', 'servicio']
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
        fields = ['nombre_cliente', 'apellido_cliente', 'correo_cliente', 'password_cliente']

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
            'info_adicional': 'Informacion Adicional',
        }

class TrabajoAdminForm(ModelForm):

    class Meta:
        model = Trabajo
        fields = ['nombre_trabajo', 'diagnostico', 'mecanico', 'materiales', 'foto', 'servicio', 'estado_publicacion', 'comentario_admin']
        labels = {
            'nombre_trabajo': 'Nombre del trabajo',
            'diagnostico': 'Descripción del diagnóstico',
            'mecanico': 'Mecánico responsable',
            'materiales': 'Materiales usados',
            'servicio': 'Tipo de Servicio',
            'estado_publicacion' : 'Estado de publicación',
            'comentario_admin' : 'Comentario'
        }