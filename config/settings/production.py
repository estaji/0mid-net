from .base import *

DEBUG = False

ALLOWED_HOSTS = ["0mid.net", "www.0mid.net", "127.0.0.1"]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "console": {"format": "%(name)-12s %(levelname)-8s %(message)s"},
        "file": {
            "format": ("%(asctime)s [%(levelname)-8s] " "(%(name)s) %(message)s"),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "handlers": {
        "console": {"class": "logging.StreamHandler", "formatter": "console"},
        #"file": {
        #    "level": "INFO",
        #    "class": "logging.FileHandler",
        #    "filename": "django.log",
        #    "formatter": "file",
        #},
    },
    #"loggers": {"": {"level": "INFO", "handlers": ["console", "file"]}},
    "loggers": {"": {"level": "INFO", "handlers": ["console"]}},
}
