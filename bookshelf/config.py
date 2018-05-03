import os
import logging
from flask_compress import Compress
from flask_security import Security, SQLAlchemyUserDatastore
from bookshelf.data.models import db, Role, User


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    # sqlite :memory: identifier is the default if no filepath is present
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '1d94e52c-1c89-4515-b87a-f48cf3cb7f0b'
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'bookshelf.log'
    LOGGING_LEVEL = logging.DEBUG
    SECURITY_PASSWORD_SALT = '8312hjf123'
    CACHE_TYPE = 'simple'
    COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/xml',
                          'application/json', 'application/javascript']
    COMPRESS_LEVEL = 6
    COMPRESS_MIN_SIZE = 500
    SUPPORTED_LANGUAGES = {'bg': 'Bulgarian',
                           'en': 'English', 'fr': 'Francais'}
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    ENV = 'dev'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///bookshelf.db'
    SECRET_KEY = 'a9eec0e0-23b7-4788-9a92-318347b9a39f'


class StagingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    ENV = 'staging'
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SECRET_KEY = '792842bc-c4df-4de1-9177-d5207bd9faa6'


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    ENV = 'prod'
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SECRET_KEY = '8c0caeb1-6bb2-4d2d-b057-596b2dcab18e'


config = {
    "dev": "bookshelf.config.DevelopmentConfig",
    "staging": "bookshelf.config.StagingConfig",
    "prod": "bookshelf.config.ProductionConfig",
    "default": "bookshelf.config.DevelopmentConfig"
}


def configure_app(app):
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name])
    app.config.from_pyfile('config.cfg', silent=True)
    # Configure logging
    handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
    handler.setLevel(app.config['LOGGING_LEVEL'])
    formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    # Configure Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.security = Security(app, user_datastore)
    # Configure Compressing
    Compress(app)
