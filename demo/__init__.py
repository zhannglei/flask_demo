from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object('demo.default_settings')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from demo.model import *

import demo.api

from demo.api.util import api_bp
app.register_blueprint(api_bp)