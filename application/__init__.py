from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from flask_mail import Mail
from itsdangerous.url_safe import URLSafeSerializer
import os
from datetime import timedelta

from flask_rq2 import RQ

app = Flask(__name__)
if (os.getenv("FLASK_ENV") == "Development"):
        app.config.from_object("application.config.DevelopmentEnv");
elif (os.getenv("FLASK_ENV") == "Testing"):
        app.config.from_object("application.config.TestingEnv");
else:
        app.config.from_object("application.config.DevelopmentEnv");


rq = RQ(app)
redis_client = FlaskRedis(app);
mail = Mail(app);

rq.init_app(app);





db = SQLAlchemy(app);

from .CryptoReader import CryptoReader
from .DataRangeReader import DataRangeReader

cryptoReader = CryptoReader();
dataRangeReader = DataRangeReader();
urlSerializer = URLSafeSerializer(secret_key=app.config["SECRET_KEY"]);

from . import filters
from . import Views
from . import Models
from . import errorHandler
from .RESTApi import RestApi
