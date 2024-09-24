from os import environ


class Config:
    SECRET_KEY = environ.get("SITE_SECRET_KEY")
    DB_NAME = environ.get("SITE_DB_NAME", "mydb")
    DB_USER = environ.get("SITE_DB_USER", "myuser")
    DB_PASSWORD = environ.get("SITE_DB_PASSWORD", "mypass")
    DB_HOST = environ.get("SITE_DB_HOST", "127.0.0.1")
    DB_PORT = environ.get("SITE_DB_PORT", "3306")
    SITE_ENV = environ.get("SITE_ENV", "local")
    PROJECT_PATH = environ.get("SITE_PROJECT_PATH")
    VENV_PATH = environ.get("SITE_VENV_PATH")
    """
    also create /etc/systemd/system/.env including
    these variables and use as EnvironmentFile in
    systemd files for scan-daemon.service and gunicorn
    """
