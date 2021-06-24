from django.shortcuts import render
from core.models import Evento

# Create your views here.


def lista_evento(request):
    evento = Evento.objects.all()
    context = {'eventos': evento}
    return render(request, 'agenda.html', context=context)

