from os import environ

class EnvConfig:
    SECRET_KEY = environ.get("SITE_SECRET_KEY")
    DB_NAME = environ.get("SITE_DB_NAME")
    DB_USER = environ.get("SITE_DB_USER")
    DB_PASSWORD = environ.get("SITE_DB_PASSWORD")
    DB_HOST = environ.get("SITE_DB_HOST")
    DB_PORT = environ.get("SITE_DB_PORT")
    DJANGO_SETTINGS_MODULE = environ.get("DJANGO_SETTINGS_MODULE")
