from .views import inicio, nosotros, menus, registro
from django.urls import path # type: ignore

urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('nosotros', nosotros, name = 'nosotros'),
    path('menus', menus, name = 'menus'),
    path('registro', registro , name = 'registro')
]