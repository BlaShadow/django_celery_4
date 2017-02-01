from django.shortcuts import render, HttpResponse
from tasks import enviar_mail

# Create your views here.
def index(request):
    
    enviar_mail.delay("Hola", "La gente dura manito", "nice@gmail.com")
    
    return HttpResponse("Hola")