from django.shortcuts import render
from .models import Oferente
from django.http import HttpResponse

def inicio(request):
    personas = Oferente.objects.all()
    contexto = {
        'personas': personas
    }
    return render(request, 'index.html', contexto)

def publicar(request):
    return HttpResponse("Crear Publicación")