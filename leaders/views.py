from django.shortcuts import render
from .models import *


# Create your views here.
def inicio(request):
    usuarios=Participante.objects.all().order_by('-puntaje')
    cont=0
    for usuario in usuarios:
        cont=cont+1
        if usuario.posicion!=cont:
            usuario.posicion_old=usuario.posicion
            usuario.posicion=cont

        usuario.diff=usuario.posicion_old-usuario.posicion
        usuario.save()

    return render(request, 'inicio.html', {'usuarios':usuarios})

#def configuator_admin(request):


#def
