from django import views
from django.urls import path
from .views import *
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

"""
1.  Como este archivo es generado de manera manual, debemos realizar el siguiente procedimiento
2.  Nos dirigimos al archivo urls.py del proyecto general.

3.  Una vez ya tengamos trabajado el archivo urls.py del proyecto general, debemos hacer la lista de urls de esta app
4.  creamos las nuevas urls
5.  Ya finalizando esto debemos configurar el archivo settings
"""

urlpatterns = [
    #   Aquí comienzan las nuevas urls, es el único código que se modifica.
    path("", views.index, name="index"),
    path('detalle_proyecto/<int:proyecto_id>/', views.detalle_proyecto, name='detalle_proyecto'),
    #   Aquí finalizan las nuevas urls, es el único código que se modifica.
]

if  settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
