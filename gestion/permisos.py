from rest_framework.permissions import BasePermission
from rest_framework.request import Request

class PermisoPersonalizado(BasePermission):
    # message > Sera el mensaje que se mostrara en el caso no se cumpla con las condiciones indicadas
    message = 'No hay permisos'

    def has_permission(self, request: Request, view):
        # middleware > es un intermediario entre la peticion del usuario (endpoint) y el controlador final (la vista que hemos definido) y si algo no cumple con lo esperado se terminara la consulta, caso contrario procedera a la ejecucion de la vista

        # aqui hare la logica de este permiso y si no cumple con lo esperado entonces retornare false

        # request > la instancia de la peticion que me realiza el cliente
        # request.user > nos devuelve la instancia del usuario encontrado en la base de datos. En el caso no se proveyese las credenciales de auth el objeto request.user sera un usuario anonimo (AnonymousUser) por lo que no podremos acceder a los atributos de la clase usuario
        print(request.user)
        # request.auth > Si no se le dan las credenciales de auth entonces sera None, si si le dan entonces nos imprimira la token que nos envia el usuario 
        print(request.auth)
        # Generalmente se suele utilizar la propiedad user ya que contiene mejor informacion que la propiedad auth

        # view > es la vista a la cual se desea acceder, no se utiliza para nada solamente se dara paso si es que cumple con las condiciones
        # print(view)
        # Solamente para los usuarios que no son administradores

        if request.auth is None : 
            return False

        print(request.user.rol)
        if request.user.rol == 'ADMINISTRADOR':
            return False
        else:
            return True


class EsAdministrador(BasePermission):
    message = 'El usuario no tiene los permisos necesarios'

    def has_permission(self, request: Request, view):
        print(request.data.get('rol'))
        # para que si el rol es 'USUARIO' no pida la token y si el rol es 'ADMINISTRADOR' tenga q pedir token
        if request.data.get('rol') == 'USUARIO':
            return True

        # validamos que en el auth tengamos una token
        if request.auth is None:
            return False

        # validamos que el usuario identificado sea administrador para poder crear
        if request.user.rol == 'ADMINISTRADOR':
            return True
        else:
            return False