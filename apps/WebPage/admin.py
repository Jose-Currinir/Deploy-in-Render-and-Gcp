from django.contrib import admin
from .models import *

"""
1.  Debemos comenzar con importar los modelos en este archivo
2.  Después debemos registrar los modelos con la siguiente estructura.
    @admin.register(Modelo)
    classModeloAdmin(admin.ModelAdmin):
	    list_display = ['','']
	    search_fields = ['','']
    	list_filter = ['','']
        ordering = ['']
        list_per_page = n
3.  En caso de que el modelo que quiero registrar en el administrador no posee más de un atributo se debe 
    registrar de la siguiente manera.
    admin.site.register(Modelo)
4.  Ya teniendo el archivo admin.py listo nos debemos ir al archivo views.py
"""

@admin.register(InformacionPersonal)
class InformacionPersonalAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ocupacion', 'email', 'telefono']
    search_fields = ['nombre', 'email']
    list_filter = ['ocupacion']

@admin.register(Habilidad)
class HabilidadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'porcentaje']
    search_fields = ['nombre']

@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'categoria', 'cliente', 'fecha']
    search_fields = ['nombre', 'cliente']
    list_filter = ['categoria', 'fecha']

@admin.register(Testimonio)
class TestimonioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cargo', 'proyecto']
    search_fields = ['nombre', 'proyecto__nombre']
    list_filter = ['proyecto']

admin.site.register(Mensaje)