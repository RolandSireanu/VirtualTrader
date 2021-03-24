from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import timedelta
from .RESTApi.RestApi import CryptoReader

app = Flask(__name__)

if (os.getenv("FLASK_ENV") == "Development"):
        app.config.from_object("application.config.DevelopmentEnv");
elif (os.getenv("FLASK_ENV") == "Testing"):
        app.config.from_object("application.config.TestingEnv");
else:
        app.config.from_object("application.config.DevelopmentEnv");


db = SQLAlchemy(app);
cryptoReader = CryptoReader();

from . import Views
from . import Models
from . import errorHandler
from .RESTApi import RestApiView