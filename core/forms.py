from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class MecanicoForm(ModelForm):

    class Meta:
        model = Mecanico
        fields = ['nombre_mecanico', 'apellido_mecanico', 'correo_mecanico', 'password_mecanico']

class TrabajoForm(ModelForm):

    class Meta:
        model = Trabajo
        fields = ['nombre_trabajo', 'diagnostico', 'mecanico', 'materiales', 'foto', 'servicio']

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