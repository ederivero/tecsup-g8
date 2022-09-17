# El tipado aun no es tan fuerte que nos va a arrojar un error si no cumplimos con determinado tipo de dato 
# lo va a permitir pero estariamos haciendo algo mal (sin errores)
def sumar(x: int , y: int ):
    # VSCode y Pycharm y sublime text le dan prioridad o importancia al tipado que nosotros manualmente le configuramos, tener cuidado porque si el tipado no es el correcto entonces podremos tener errores de incompatibilidad
    nombre: int = 'Eduardo'
    
    return x + y


print(sumar('A', 'C'))
print(sumar(1, 10))