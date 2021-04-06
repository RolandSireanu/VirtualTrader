from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import timedelta

from flask_rq2 import RQ


app = Flask(__name__)
rq = RQ(app)

rq.init_app(app);

if (os.getenv("FLASK_ENV") == "Development"):
        app.config.from_object("application.config.DevelopmentEnv");
elif (os.getenv("FLASK_ENV") == "Testing"):
        app.config.from_object("application.config.TestingEnv");
else:
        app.config.from_object("application.config.DevelopmentEnv");


db = SQLAlchemy(app);

from .CryptoReader import CryptoReader
cryptoReader = CryptoReader();

from . import Views
from . import Models
from . import errorHandler
from .RESTApi import RestApi