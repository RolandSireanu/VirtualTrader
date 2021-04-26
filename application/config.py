from datetime import timedelta
import os


class BaseConfig(object):
    SECRET_KEY="fwv32frw242ef39";
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:1234@"+os.environ.get('DATABASE_HOST')+":5432/trader";
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
    DEBUG = False
    TESTING = False
    SESSION_COOKIE_SECURE=False 
    RQ_REDIS_URL = 'redis://'+os.environ.get("REDIS_HOST")+":6379/0"
    REDIS_URL = 'redis://'+os.environ.get("REDIS_HOST")+":6379/1"
    RQ_SCHEDULER_INTERVAL = 10
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5);
    SESSION_REFRESH_EACH_REQUEST = True;
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USERNAME = os.environ.get("USER_EMAIL");
    MAIL_PASSWORD = os.environ.get("PASSWORD_EMAIL");
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    

class TestingEnv(BaseConfig):
    TESTING = True 

class DevelopmentEnv(BaseConfig):
    DEBUG = True
    
