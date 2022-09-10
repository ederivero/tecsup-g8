from django.db import models

class Importancia(models.Model):
    # va a ser un entero y ademas sera autoincrementable
    # NOTA: solamente puede haber una columna autoincrementable por tabla
    # Field types: https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-types
    # Field options (las opciones que le podemos pasar a todos los tipos de datos): https://docs.djangoproject.com/en/4.1/ref/models/fields/#field-options
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=45, unique=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        # se usa para cuando trabajamos con herencia para poder pasar metadatos (informacion a la clase padre)
        # https://docs.djangoproject.com/en/4.1/ref/models/options/
        # sirve para cambiar el nombre de la tabla con relacion al modelo
        db_table='importancias'



class Tarea(models.Model):
    # si no indico la columna id Django automaticamente me la creara, se suele colocar cuando queremos llamarla de otra manera
    class CategoriaOpciones(models.TextChoices):
        # el primer valor sera para cuando nosotros usemos formularios y el segundo valor es el valor que se almacera en la base de datos
        LISTADO = ('LISTADO', 'LISTADO') 
        POR_HACER = ('POR_HACER', 'POR_HACER')
        HACIENDO = ('HACIENDO', 'HACIENDO')
        FINALIZADO = ('FINALIZADO', 'FINALIZADO')
        CANCELADO = ('CANCELADO', 'CANCELADO')

    categoria = models.CharField(choices=CategoriaOpciones.choices, max_length=15, default='LISTADO')
    nombre = models.CharField(max_length=250, null=False)
    descripcion = models.TextField(null=True)
    fechaCaducidad = models.DateTimeField(db_column='fecha_caducidad')
    
    # Relaciones
    # on_delete > significa que va a suceder cuando se intente eliminar una importancia que tiene tareas
    # CASCADE > primero eliminara la Importancia y luego eliminara todas las Tareas de esa importancia
    # PROTECT > evitara la eliminacion de la Importancia mientras que tenga Tareas ProtectError
    # RESTRICT > evitara la eliminacion pero emitira un error de tipo RestrictedError
    # SET_NULL > eliminara la Importancia pero todas las tareas de esa importancia las seteara en 'null'
    # SET_DEFAULT > eliminara la Importancia pero tendremos que indicar un valor por defecto para que sea reemplazado
    # DO_NOTHING > No toma ninguna accion, elimina la Importancia pero aun conservara ese ID eliminado (es el mas peligroso de todos porque puede generar mala incongruencia de datos)
    # https://docs.djangoproject.com/en/4.1/topics/db/examples/many_to_one/
    importancia = models.ForeignKey(to=Importancia, db_column='importancia_id', on_delete=models.PROTECT, null=False)
    class Meta:
        db_table = 'tareas'


class Etiqueta(models.Model):
    # definir los atributos de la tabla etiqueta con sus propiedades
    nombre = models.CharField(max_length=45, null=False, unique=True)

    class Meta:
        db_table= 'etiquetas'



class TareaEtiqueta(models.Model):
    # el parametro related_name sirve para poder referenciar desde la clase donde estamos creando la relacion hacia todos sus 'hijos' osea creara un atributo virtual en la clase Tarea para poder acceder a todas sus tareasEtiquetas, si no define su valor predeterminado sera el nombre del modelo con '_set' osea en este caso sera 'tareaetiqueta_set'
    tarea = models.ForeignKey(to=Tarea, db_column='tarea_id', on_delete=models.CASCADE, related_name='tareaEtiqueta')
    etiqueta = models.ForeignKey(to=Etiqueta, db_column='etiqueta_id', on_delete=models.CASCADE, related_name='etiquetaTarea')

    class Meta:
        db_table='tareas_etiquetas'