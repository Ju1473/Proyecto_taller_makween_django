from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'core/index.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def contacto(request):
    return render(request, 'core/contacto.html')

def mecanicos(request):
    return render(request, 'core/mecanicos/index.html')

def galeria(request):
    return render(request, 'core/galeria.html')

def not_found(request):
    return render(request, 'core/404.html')

def proyectoadd(request):
    return render(request, 'core/mecanicos/crud/add.html')