from django.shortcuts import render
from .models import Oferente


def inicio(request):
    personas = Oferente.objects.all()
    contexto = {
        'personas': personas
    }
    return render(request, 'index.html', contexto)
