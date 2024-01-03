from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

"""
1.  Debemos agregar los imports de include, settings y static
2.  Además debemos agregar el código para realizar la conexión con la carpeta media
3.  Y como ultimo agregamos al path las url de nuestra app generada
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("apps.WebPage.urls")),
]
if  settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)