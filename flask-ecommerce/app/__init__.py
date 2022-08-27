from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_migrate import Migrate
from logging import (
    basicConfig,
    DEBUG,
    FileHandler,
    StreamHandler
)
import os
from flask_jwt_extended import JWTManager

basicConfig(
    level=DEBUG,
    encoding='utf-8',
    handlers=[FileHandler('flask.log'), StreamHandler()]
)

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["JWT_SECRET_KEY"] = "super-secret"

cors = CORS(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
jwt = JWTManager(app)

@app.route("/")
def index():
    return "El servidor funciona 🤠"

from app import routers