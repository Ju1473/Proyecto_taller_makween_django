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
    path('404/', not_found, name="404"),
    path('mecanicos/mecanicoadd/', mecanicoadd, name="mecanicoadd"),
    path('mecanicos/mecanicolistar/', mecanicos, name="mecanicolistar"),
    path('mecanicos/mecanicoupdate/<id>/', mecanicoupdate, name="mecanicoupdate"),
    path('mecanicos/trabajoadd/', trabajoadd, name="trabajoadd"),
    path('mecanicos/trabajolistar/', trabajos, name="trabajolistar")
]
