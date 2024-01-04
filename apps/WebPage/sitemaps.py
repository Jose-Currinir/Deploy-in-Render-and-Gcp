from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import *

class IndexSitemap(Sitemap):
    priority = 0.8
    changefreq = 'daily'

    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)
    
class ProyectoSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.5

    def items(self):
        return Proyecto.objects.all()

    def lastmod(self, obj):
        return obj.fecha_actualizacion  # Asumiendo que tienes un campo de fecha de actualización

    def location(self, obj):
        return reverse('detalle_proyecto', args=[obj.id])