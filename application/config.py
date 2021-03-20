from datetime import timedelta
import os


class BaseConfig(object):
    SECRET_KEY="fwv32fr42ef39";
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.getcwd(), 'application/resources/app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE=False 
    #PERMANENT_SESSION_LIFETIME = timedelta(minutes=5);
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestingEnv(BaseConfig):
    TESTING = True 

class DevelopmentEnv(BaseConfig):
    DEBUG = True
    
