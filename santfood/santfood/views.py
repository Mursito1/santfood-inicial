from django.shortcuts import render


def inicio(request):
    return render (request, 'paginas/inicio.html')

def nosotros(request):
    return render (request, 'paginas/nosotros.html')


def menus (request):
    return render (request, 'paginas/menus.html')


def registro (request):
    return render (request, 'paginas/registro.html')