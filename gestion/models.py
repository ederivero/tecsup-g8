from django.db import models
from .authManager import AuthManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# AbstractBaseUser > usar la plantilla del usuario que django nos brinda
# PermissionsMixin > modificar los permisos del usuario a nivel del panel administrativo
class Usuario(AbstractBaseUser, PermissionsMixin):
    
    id = models.AutoField(primary_key=True, unique=True)
    correo = models.EmailField(unique=True, null=False)
    password = models.TextField(null=False)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    # en el primer valor sera el que se almacena en la bd | en el que se usa para formularios
    rol = models.CharField(max_length=50, choices=(['ADMINISTRADOR', 'ADMINISTRADOR'], ['USUARIO', 'USUARIO']))
    validado = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    
    # fecha de creacion del usuario
    createdAt = models.DateTimeField(auto_now_add=True, db_column='creado')
    # fecha en la que se actualizo cualquier campo
    updatedAt = models.DateTimeField(auto_now=True, db_column='actualizado')

    # =========================================
    # TODO LO SIGUIENTE ES NETAMENTE SI AUN QUEREMOS UTILIZAR EL PANEL ADMINISTRATIVO 

    # agregar las siguientes columnas para que el panel administrativo siga funcionando a pesar de haber modificado el auth_user
    # is_staff > sirve para indicar si el usuario creado pertenece al equipo de trabajo 
    is_staff = models.BooleanField(default=False)
    # is_active > puede realizar operaciones dentro del panel administrativo, pero si el usuario no esta activo podra logearse pero no realizar ninguna accion dentro del panel administrativo
    is_active = models.BooleanField(default=True)

    # dar el comportamiento que tendra el modelo cuando se realice el comando python manage.py createsuperuser
    objects = AuthManager()

    # se usara para el panel administrativo al momento de hacer el login
    USERNAME_FIELD = 'correo'

    # seran los valores pedidos al momento de hacer la creacion del superusuario por la terminal. NOTA: NO va el atributo declarado en el USERNAME_FIELD ni tampoco el password porque esos ya son de caracter OBLIGATORIO y si los ponemos emitira un error al realizar la creacion
    REQUIRED_FIELDS = ['nombre', 'apellido', 'rol']

    class Meta:
        db_table = 'usuarios'


class Categoria(models.Model):
    nombre = models.CharField(max_length=45, null=False)

    class Meta:
        db_table = 'categorias'

class Figura(models.Model):
    codigo = models.CharField(max_length=10, null=False, unique=True)
    nombre = models.CharField(max_length=45, null=False)
    # RELACIONES
    categoria = models.ForeignKey(to=Categoria, on_delete=models.PROTECT, related_name='figuras')

    class Meta:
        db_table = 'figuras'

class Registro(models.Model):
    numeroVeces = models.IntegerField(db_column='num_veces', null=False)
    tipo = models.CharField(max_length=40, choices=(['NORMAL','NORMAL'],['ESPECIAL', 'ESPECIAL'], ['ESCUDO', 'ESCUDO']))
    # RELACIONES
    figura = models.ForeignKey(to=Figura, on_delete=models.PROTECT, related_name='figura_registros')
    usuario = models.ForeignKey(to=Usuario, on_delete=models.PROTECT, related_name='usuario_registros')

    class Meta:
        db_table = 'registros'