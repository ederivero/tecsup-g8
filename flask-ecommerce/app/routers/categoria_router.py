from app import app
from flask import request
from app.controllers.categoria_controller import CategoriaController


@app.route("/categorias/", methods=['GET', 'POST'])
def categorias():
    if request.method == 'GET':
        categorias = CategoriaController().getAll()
        return categorias
    else:
        json_input = request.get_json()
        result = CategoriaController().post(json_input)
        return result
