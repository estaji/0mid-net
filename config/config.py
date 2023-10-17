from os import environ


class Config:
    SECRET_KEY = environ.get("SITE_SECRET_KEY")
    DB_NAME = environ.get("SITE_DB_NAME", "mydb")
    DB_USER = environ.get("SITE_DB_USER", "myuser")
    DB_PASSWORD = environ.get("SITE_DB_PASSWORD", "mypass")
    DB_HOST = environ.get("SITE_DB_HOST", "127.0.0.1")
    DB_PORT = environ.get("SITE_DB_PORT", "3306")
    # Edit paths in ./systemd/scan-daemon.service
