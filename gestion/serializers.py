from rest_framework import serializers
from .models import Importancia, Tarea, Etiqueta, TareaEtiqueta

class PruebaSerializer(serializers.Serializer):
    # ahora vamos a definir la informacion que va a llegar y/o salir
    # https://www.django-rest-framework.org/api-guide/fields/
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(required=True, trim_whitespace= True, max_length= 20)
    apellido = serializers.CharField(required=True, trim_whitespace= True, max_length= 15)
    password = serializers.CharField(write_only=True)

    def create(self, data_validada):
        print('Aca se deberia de guardar la info en la BD')
        print(data_validada)
        # aca se deberia de retorna esa informacion guardada en la bd
        return 


class ImportanciaSerializer(serializers.ModelSerializer):

    def save(self):
        # modifico el nombre de la data_validad y lo convierto a minusculas
        self.validated_data['nombre'] = self.validated_data.get('nombre').lower()

        nuevaImportancia = Importancia.objects.create(**self.validated_data)

        return nuevaImportancia
        
    class Meta:
        model = Importancia # para poder setear todos los fields de mi modelo en el serializador
        # fields > sirve para indicar que columnas del modelo vamos a utilizar en este serializar
        # fields = ['id', 'nombre'] # restingiendo que la columna 'deleted' ya no se va a utilizar 
        # tambien podemos definir el atributo 'exclude' en el cual se definira las columnas que no se quieran mostrar 
        exclude = ['deleted']
        # NOTA: no pueden ir declarados los atributos fields y exclude o es uno, o el otro


class ImportanciaSerializerRUD(serializers.ModelSerializer):
    class Meta:
        model = Importancia 
        fields = '__all__'

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'

class ImportanciaSinDeletedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Importancia
        exclude = ['deleted']

class TareaEtiquetaConEtiquetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = TareaEtiqueta
        exclude= ['tarea','id']
        depth = 1
        

class TareaConImportanciaSerializer(serializers.ModelSerializer):
    # anidamiento de serializadores (nested serializers)
    # si nosotros queremos utilizar un serializador personalizado con las columnas que queremos mostrar entonces en vez de utilizar el 'depth' podemos llamar al atribut que es la FK y asignarlo otro serializador, ademas, si queremos cambiar el nombre de ese atributo por otro , entonces en el serializador deberemos de colocar el parametro 'source' con el nombre del atributo (FK)
    importancia = ImportanciaSinDeletedSerializer()
    etiquetas = TareaEtiquetaConEtiquetasSerializer(many= True, source= 'tareaEtiqueta') # tareaetiqueta_set

    class Meta:
        model = Tarea
        fields = '__all__'
        # depth > es el nivel que nosotros queremos ingresar desde este modelo hacia los demas, esto solamente servira para las relaciones donde tengamos la FK < PK, osea solamente a las relaciones en la cual este modelo tenga FK (llaves foraneas)
        # depth = 1 

class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etiqueta
        fields = '__all__'


class TareaEtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TareaEtiqueta
        fields = '__all__'