# Introduccion a flask

## Creamos entorno virtual con python 

- Para crear el entorno virual se usa el comando: 
```bash
    python -m venv venv
```
- Para activar el entorno virtual se usa el comando ("bin" en MAC y "Scripts" en Windows):
```bash
    source venv/bin/activate
```
```bash
    source venv/Scripts/activate
```
- Para desactivar el entorno virtual se usa el comando:
```bash
    deactivate
```

## Instalamos flask
- Para instalar flask se usa el comando:
```bash
    pip install flask
```
- Para ver las librerias instaladas se usa el comando:
```bash
    pip freeze
```
```bash
    pip list
```

## Levantamos el servidor
- Para levantar el servidor se usa el comando:
```bash
    flask run
```
- Para levantar el servidor en modo debug se usa el comando:
```bash
    flask --debug run
```

# Crear una API con flask y sqlalchemy
- Primero tenemos que instalar las librerias:
```bash
    pip install flask-sqlalchemy
```

# Creamos un ecommerce con flask y marshmallow
- Instalamos las dependencias de nuestro requirements.txt:
```bash
    pip install -r requirements.txt
```
- O instalamos las librerias de forma manual:
```bash
    pip install flask
    pip install flask-sqlalchemy
    pip install flask-cors
    pip install flask-migrate
    pip install flask-marshmallow
    pip install marshmallow-sqlalchemy
```
- Luego de crear nuestros modelos vamos a migrar la base de datos (SOLO SE EJECUTA UNA SOLA VEZ):
```bash
    flask db init
```
- Luego de migrar la base de datos vamos a crear la base de datos:
```bash
    flask db migrate -m "Initial migration"
```
- Luego de crear la base de datos vamos a hacer el rollback:
```bash
    flask db upgrade
```

# Nuestras variables de entorno (Necesario para que funcione)
```text
FLASK_DEBUG=True
FLASK_RUN_PORT=5000
# FLASK_APP='main.py'
FLASK_RUN_HOST=127.0.0.1

DB_URI=mysql://root:root@localhost/flask_ecommerce
```