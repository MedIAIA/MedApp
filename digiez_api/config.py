import os
from dotenv import load_dotenv

load_dotenv('./etc/.env_{}'.format('dev'))
# load_dotenv('./etc/.env_{}'.format(os.environ.get('CONFIG_ENV')))

class ConfigEnv(object):

    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SWAGGER_BASE_PATH = os.environ.get("SWAGGER_BASE_PATH")
    SESSION_COOKIE_SECURE = True
    DEBUG = os.environ.get('DEBUG')
    DEV = os.environ.get("DEV")
    if not DEV:
        # Load database postgres credentials
        pass