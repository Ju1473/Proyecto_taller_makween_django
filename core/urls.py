from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('nosotros/', nosotros, name="nosotros"),
    path('contacto/', contacto, name="contacto"),
    path('mecanicos/', mecanicos, name="mecanicos"),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('logout/', logout_view, name="logout"),
    path('galeria/', galeria, name="galeria"),
    path('servicios/', servicios, name="servicios"),
    path('404/', not_found, name="404"),
    path('mecanicos/mecanicoadd/', mecanicoadd, name="mecanicoadd"),
    path('mecanicos/mecanicolistar/', mecanicos, name="mecanicolistar"),
    path('mecanicos/mecanicoupdate/<id>/', mecanicoupdate, name="mecanicoupdate"),
    path('mecanicos/mecanicodelete/<id>/', mecanicodelete, name="mecanicodelete"),
    path('mecanicos/trabajoadd/', trabajoadd, name="trabajoadd"),
    path('mecanicos/trabajolistar/', trabajos, name="trabajolistar"),
    path('mecanicos/trabajoupdate/<id>/', trabajoupdate, name="trabajoupdate"),
    path('mecanicos/listarconsultas/', listarconsultas, name="listarconsultas"),
    path('mecanicos/listarreservas/', listarreservas, name="listarreservas"),
    path('mecanicos/reservaupdate/<id>/', reservaupdate, name="reservaupdate"),
    path('trabajo/<id>/', trabajo, name="trabajo"),
    path('reserva/', reserva, name="reserva"),
    path('categoria_trabajo/<int:id>/', categoria_trabajo, name="categoria_trabajo"),
    path('mecanico_trabajo/<id>/', mecanico_trabajo, name="mecanico_trabajo"),
]
