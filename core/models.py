from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from core.funciones import upload_to_mecanicos, upload_to_trabajos
# Create your models here.

class TipoServicio(models.Model):
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return self.descripcion

class Mecanico(models.Model):
    nombre_mecanico = models.CharField(max_length=50)
    apellido_mecanico = models.CharField(max_length=50)
    correo_mecanico = models.CharField(max_length=50)
    password_mecanico = models.CharField(max_length=50)
    foto_mecanico = models.ImageField(upload_to=upload_to_mecanicos)
    cant_mantenciones_mec = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre_mecanico + ' ' + self.apellido_mecanico
    
    def calcular_cantidad_trabajos(self):
        return Trabajo.objects.filter(mecanico=self,estado_publicacion="A").count()
    
class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=50)
    apellido_cliente = models.CharField(max_length=50)
    correo_cliente = models.CharField(max_length=50)
    cant_mantenciones_cli = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre_cliente + ' ' + self.apellido_cliente
    
    def calcular_cantidad_trabajos(self):
        return Trabajo.objects.filter(cliente=self,estado_publicacion="A").count()

class Trabajo(models.Model):
    nombre_trabajo = models.CharField(max_length=50)
    diagnostico = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE)
    materiales = models.CharField(max_length=50)
    foto = models.ImageField(upload_to=upload_to_trabajos)
    servicio = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)
    PENDIENTE= "P"
    RECHAZADO= "R"
    ACEPTADO= "A"
    estado_opciones = {
        PENDIENTE: "Pendiente",
        RECHAZADO: "Rechazado",
        ACEPTADO: "Aceptado",
    }
    estado_publicacion = models.CharField(max_length=1,choices=estado_opciones,default=PENDIENTE)
    comentario_admin = models.CharField(max_length=100, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    def clean(self):
        super().clean()
        if self.estado_publicacion == self.RECHAZADO and not self.comentario_admin:
            raise ValidationError({'comentario_admin': 'El comentario del administrador es requerido cuando el estado es "Rechazado".'})

    def __str__(self):
        return self.nombre_trabajo
    

class EstadoTrabajo(models.Model):
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE)
    estado = models.BooleanField(default=False)
    desc_rechazo = models.CharField(max_length=150)

    def __str__(self):
        return self.estado

class TipoConsulta(models.Model):
    descripcion = models.CharField(max_length=40)

    def __str__(self):
        return self.descripcion

class Contacto(models.Model):
    nombre_apellido = models.CharField(max_length=100)
    email_contacto = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9,validators=[RegexValidator(r'^\d{9}$', 'El número de teléfono debe tener 9 dígitos numéricos.')])
    consulta = models.ForeignKey(TipoConsulta, on_delete=models.CASCADE)
    info_adicional = models.TextField()

    def __str__(self):
        return self.nombre_apellido

class Reserva(models.Model):
    nombre_apellido = models.CharField(max_length=100)
    email_reserva = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9,validators=[RegexValidator(r'^\d{9}$', 'El número de teléfono debe tener 9 dígitos numéricos.')])
    tipo_servicio = models.ForeignKey(TipoServicio, on_delete=models.CASCADE)
    mecanico = models.ForeignKey(Mecanico, on_delete=models.CASCADE, null=True)
    PENDIENTE= "P"
    ACEPTADO= "A"
    estado_opciones = {
        PENDIENTE: "Pendiente",
        ACEPTADO: "Aceptado",
    }
    estado_reserva = models.CharField(max_length=1,choices=estado_opciones,default=PENDIENTE)

    def __str__(self):
        return self.nombre_apellido
    
    def clean(self):
        super().clean()
        if self.estado_reserva == self.ACEPTADO and not self.mecanico:
            raise ValidationError({'mecanico': 'Debe tener un mecánico que hará el trabajo!'})