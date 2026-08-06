from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('bebidas/', include('bebidas.urls')),
    path('vapes/', include('vapes.urls')),
    path('nosotros/', include('nosotros.urls')),
    path('contacto/', include('contacto.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)