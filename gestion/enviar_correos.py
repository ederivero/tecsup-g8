from django.core.mail import send_mail
from os import environ

def enviar_correo_validacion(usuario_email):
    return send_mail(
        subject='Por favor verifica tu correo', 
        message='Hola, Bienvenido a la aplicacion de intercambio de figuritas. Por favor valida tu correo haciendo click en el siguiente enlace ...', 
        from_email=environ.get('EMAIL_USERNAME'), 
        recipient_list= [usuario_email], 
        fail_silently=False
        )
    

