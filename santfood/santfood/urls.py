from .views import inicio, nosotros, menus, registro
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('nosotros', nosotros, name = 'nosotros'),
    path('menus', menus, name = 'menus'),
    path('registro', registro , name = 'registro')
]