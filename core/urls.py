from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('nosotros/', nosotros, name="nosotros"),
    path('contacto/', contacto, name="contacto"),
    path('mecanicos/', mecanicos, name="mecanicos"),
    path('galeria/', galeria, name="galeria"),
    path('404/', not_found, name="404"),
    path('mecanicos/add/', proyectoadd, name="proyectoadd")
]
