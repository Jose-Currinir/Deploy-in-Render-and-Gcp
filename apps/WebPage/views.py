from django.shortcuts import get_object_or_404, render
from .models import *
from django.views.decorators.cache import cache_page

"""
1.  Comenzamos con importar los models
2.  Creamos la view, con el siguiente formato
    @cache_page(60 * 15)  # Ajusta el tiempo de caché según tus necesidades
    def mi_vista_personalizada(request):
        template_name = 'ruta/a/mi_template.html'
        titulo_pagina = 'Título de la Página'
        descripcion_pagina = 'Descripción breve de la página (30 a 40 palabras)'
        # Listas de categorización
        CATEGORIA_1 = ['Opción1', 'Opción2', 'Opción3']
        CATEGORIA_2 = ['OpciónA', 'OpciónB', 'OpciónC']
        # Consultas a la base de datos basadas en categorías
        resultados_categoria_1 = TuModelo.objects.filter(campo__in=CATEGORIA_1).order_by('campo_orden')
        resultados_categoria_2 = TuModelo.objects.filter(campo__in=CATEGORIA_2).order_by('campo_orden')
        # Contexto para el template
        contexto = {
            'titulo_pagina': titulo_pagina,
            'descripcion_pagina': descripcion_pagina,
            'resultados_categoria_1': resultados_categoria_1,
            'resultados_categoria_2': resultados_categoria_2,
        }
        # Renderización del template
        return render(request, template_name, contexto)
"""

@cache_page(60 * 2)
def index(request):
    template    = 'WebPage/index.html'
    #
    informacion =   InformacionPersonal.objects.all()
    habilidades =   Habilidad.objects.all()[:5]
    proyectos   =   Proyecto.objects.all()
    testimonios =   Testimonio.objects.all()
    contexto    =   {
        'informacion':  informacion,
        'habilidades':  habilidades,
        'proyectos':    proyectos,
        'testimonios':  testimonios
        }
    return render(request, template, contexto)

@cache_page(60 * 2)
def detalle_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, pk=proyecto_id)
    template    = 'WebPage/detalle_proyecto.html'
    #
    return render(request, template, {'proyecto':proyecto})
