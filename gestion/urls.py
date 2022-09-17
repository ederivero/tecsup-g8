from django.urls import path
from .views import RegistroUsuarioView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('registro', RegistroUsuarioView.as_view()),
    # tendremos un endpoint que servira para validar el usuario y si es, retornar la token de acceso y de refresco
    path('iniciar-sesion', TokenObtainPairView.as_view())
]