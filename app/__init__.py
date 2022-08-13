from flask import Flask, request
from logging import basicConfig, DEBUG, FileHandler, StreamHandler
# INFO SUCCESS DEBUG ERROR

basicConfig(
    level=DEBUG,
    format='%(asctime)s [%(levelname)s] %(message)s',
    encoding='utf-8',
    handlers=[FileHandler('flask.log'), StreamHandler()]
)

app = Flask(__name__)

users = [
    {
        'id': 1,
        'name': 'Flavio',
        'last_name': 'Rios',
        'age': 26
    },
    {
        'id': 2,
        'name': 'Gerardo',
        'last_name': 'Garibay',
        'age': 22
    }
]

@app.route('/users', methods=['GET'])
def usersList():
    return users, 200

@app.route('/users/<id>', methods=['GET'])
def userGetById(id):
    for user in users:
        if user['id'] == int(id):
            return user, 200
        
    return {
        'message': 'El usuario no ha sido encontrado'
    }, 404

@app.route('/users', methods=['POST'])
def userCreate():
    user = request.get_json()
    users.append(user)
    return {
        "message": "Usuario creado con exito",
        "users": users
    }, 201

@app.route('/users/<id>', methods=['PUT'])
def userUpdate(id):
    for user in users:
        if user['id'] == int(id):
            body = request.get_json()
            user['name'] = body['name']
            user['last_name'] = body['last_name']
            user['age'] = body['age']
            return user, 200
        
    return {
        'message': 'El usuario no ha sido encontrado'
    }, 404
    
@app.route('/users/<id>', methods=['DELETE'])
def userDelete(id):
    for index, user in enumerate(users):
        if user['id'] == int(id):
            users.pop(index)
            return users, 200
        
    return {
        'message': 'El usuario no ha sido encontrado'
    }, 404
