from app_mail.celery import app
from django.core.mail import send_mail

@app.task
def prueba_suma(x, y):
    return x + y
    
@app.task
def prueba_resta(x, y):
    return x - y
    
    
@app.task
def enviar_mail(asunto, contenido, destinatario):
    send_mail(asunto, contenido, 'noreply@mail.com', [destinatario], fail_silently=False)
