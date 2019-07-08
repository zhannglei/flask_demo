from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging


app = Flask(__name__)
app.config.from_object('demo.default_settings')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

logging_format = "[%(asctime)s] %(process)d-%(levelname)s "
logging_format += "%(module)s::%(funcName)s():l%(lineno)d: "
logging_format += "%(message)s"

logging.basicConfig(
    format=logging_format,
    level=logging.DEBUG
)
log = logging.getLogger()


from demo.model import *

import demo.api

from demo.api.util import api_bp
app.register_blueprint(api_bp)