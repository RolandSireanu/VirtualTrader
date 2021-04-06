from datetime import timedelta
import os


class BaseConfig(object):
    SECRET_KEY="fwv32frw242ef39";
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL');
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE=False 
    RQ_REDIS_URL = 'redis://localhost:6379/0'
    RQ_SCHEDULER_INTERVAL = 10
    #PERMANENT_SESSION_LIFETIME = timedelta(minutes=5);

class TestingEnv(BaseConfig):
    TESTING = True 

class DevelopmentEnv(BaseConfig):
    DEBUG = True
    
