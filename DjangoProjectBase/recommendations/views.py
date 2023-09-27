from django.shortcuts import render

from .models import Recommendations 

from . import utils

def recommendation_view(request):
    if request.method == 'POST':
        tipo_pelicula = request.POST.get('tipo_pelicula', '')
        if tipo_pelicula:
            # Llama a la función get_completion para obtener la respuesta
            texto, image_url  = utils.Generar_respuesta(tipo_pelicula)
            respuestas = {
                'texto': texto,
                'image_url': image_url,
            }
            # Renderiza tu plantilla HTML y pasa la respuesta como contexto
            return render(request, './recommendation.html', {'respuestas': respuestas})

    recomendaciones = Recommendations.objects.all()

    return render(request, './recommendation.html', {'recomendaciones': recomendaciones})