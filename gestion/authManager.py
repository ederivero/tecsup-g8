from django.contrib.auth.models import BaseUserManager
# BaseUserManager > me permite modificar el comportamiento ENTERO de la creacion del usuario por la terminal
# UserManager > me permitir modificar el comportamiento de los campos nuevos que estoy agregando al modelo del usuario mas no a todos los campos

class AuthManager(BaseUserManager):
    def create_superuser(self, correo, password, nombre, apellido, rol):
        """Creacion de un super usuario por consola (python manage.py createsuperuser)"""
        # los parametros que definamos en el metodo tienen que ser iguales a los nombre de los atributos que hemos definido
        if not correo:
            raise ValueError('El super usuario no puede tener el correo vacio')
        # valido el correo y ademas lo normalizo (remueve los espacios al inicio, al final y al medio) y lo pone todo en minusculas
        correo_normalizado = self.normalize_email(correo)

        # inicializo el nuevo usuario con la informacion brindada por la terminal
        nuevoUsuario = self.model(correo=correo_normalizado, nombre=nombre, apellido=apellido, rol=rol, is_staff=True, is_superuser=True)

        # generara un hash de la contraseña para evitar guardar el valor de manera pura en la bd, NOTA: los hashes no pueden ser convertidos al valor original lo que lo hace mas seguro
        nuevoUsuario.set_password(password)

        # guardamos el usuario de manera permanente en la bd
        nuevoUsuario.save()

        return nuevoUsuario
