from rest_framework import serializers
from .models import Usuario

class RegistrarUsuarioSerializer(serializers.ModelSerializer):

    def save(self):
        # modificamos el metodo save para que ahora si se pueda generar el hash de la password
        nuevoUsuario = Usuario(**self.validated_data)
        nuevoUsuario.set_password(self.validated_data.get('password'))
        nuevoUsuario.save()
        return nuevoUsuario

    class Meta:
        model = Usuario
        # groups > es el related_name entre el auth_user y el auth_user_groups
        # user_permissions > es el related_name entre el auth_user y el auth_user_permission 
        # en este escenario no necesitamos acceder a estas propiedades por ende las excluiremos
        exclude = ['groups', 'user_permissions']