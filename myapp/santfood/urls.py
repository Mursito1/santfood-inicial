from .views import inicio, nosotros, menus, registro
from django.urls import path # type: ignore
from django.conf.urls.static import static # type: ignore
from django.conf import settings # type: ignore

urlpatterns = [
    path('', inicio, name = 'inicio'),
    path('nosotros', nosotros, name = 'nosotros'),
    path('menus', menus, name = 'menus'),
    path('registro', registro , name = 'registro')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)