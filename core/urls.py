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
    path('mecanicos/mecanicolistar/mecanicodelete/<id>/', mecanicodelete, name="mecanicodelete"),
    path('mecanicos/trabajoadd/', trabajoadd, name="trabajoadd"),
    path('mecanicos/trabajolistar/', trabajos, name="trabajolistar"),
    path('mecanicos/trabajoupdate/<id>/', trabajoupdate, name="trabajoupdate"),
    path('mecanicos/listarconsultas/', listarconsultas, name="listarconsultas"),
    path('trabajo/<id>/', trabajo, name="trabajo"),
]
