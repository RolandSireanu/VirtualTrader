from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from datetime import timedelta
from .RestApi import CryptoReader

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.getcwd(), 'application/resources/app.db')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
app.permanent_session_lifetime = timedelta(minutes=5);

print('sqlite:///' + os.path.join(os.getcwd(), 'resources/app.db'))
db = SQLAlchemy(app);
cryptoReader = CryptoReader();

from . import Views
from . import Models