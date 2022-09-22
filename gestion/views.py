from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.request import Request
from .serializers import RegistrarUsuarioSerializer, RegistroSerializer, MostrarFigurasSerializer
from rest_framework.response import Response
from rest_framework import status
from .enviar_correos import enviar_correo_validacion
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permisos import PermisoPersonalizado, EsAdministrador
from .models import Registro

class RegistroUsuarioView(CreateAPIView):
    serializer_class = RegistrarUsuarioSerializer
    permission_classes = [EsAdministrador]

    def post(self, request: Request):
        data = self.serializer_class(data= request.data)
        data.is_valid(raise_exception=True)
        data.save()

        print(enviar_correo_validacion(data.data.get('correo')))

        return Response(data={
            'message': 'Usuario creado exitosamente',
            'content': ''
        }, status=status.HTTP_201_CREATED)


class RegistroFiguritasView(ListCreateAPIView):
    # es el atributo que me va a serviro para indicar en en esta vista que tipos de usuarios pueden ingresar
    # AllowAny > sirve para indicar que cualquiera puede acceder a estos metodos
    # IsAuthenticated > solamente verificara que nos este proveyendo una token
    # IsAdminUser > solamente los usuarios que son 'is_superuser' pueden tener acceso a estos controladores

    permission_classes= [PermisoPersonalizado]
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer

    def get(self, request):
        id_usuario = request.user.id

        registros = self.get_queryset().filter(usuario = id_usuario).all()
        print(registros)
        # utilizar el serializador para convertir los registros a informacion leible
        return Response(data={
            'message':'Tu coleccion es:',
            'content': MostrarFigurasSerializer(instance=registros, many=True).data
        })
    
    def post(self, request):
        id_usuario = request.user.id
        # agregando al body actual la llave del usuario proveniente del request del usuario
        # usamos el ** para hacer la destructuracion o sacar el contenido del diccionario y agregarlo a uno nuevo
        data = {**request.data, **{'usuario': id_usuario}}
        print(data)
        registroSerializado = self.serializer_class(data=data)

        registroSerializado.is_valid(raise_exception=True)
        nuevoRegistro = registroSerializado.save()

        return Response(data={
            'message':'Registro creado exitosamente',
            'content': self.serializer_class(instance=nuevoRegistro).data
        })