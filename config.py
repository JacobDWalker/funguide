import os


class Config(object):
    DEBUG = False
    TESTING = False

    SECRET_KEY = os.urandom(12)
    UPLOADS = 'static/img'

    SESSION_COOKIE_SECURE = True

    ALLOWED_EXTENSIONS = {'png', "jpg", "jpeg"}
    IMAGE_UPLOADS = r'static/img/uploads'


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False
    ENV = 'development'


class TestingConfig(Config):
    TESTING = True
    SESSION_COOKIE_SECURE = False
