from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Auth/', include('usuarios.urls')),
    path('Comentarios/', include('comentarios.urls')),
    path('', include('main.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

handler404 = "main.views.PageNotFound"
