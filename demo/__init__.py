from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object('demo.default_settings')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

api_bp = Blueprint('api', __name__)
api = Api(api_bp)


from demo.model import *

import demo.api

app.register_blueprint(api_bp)