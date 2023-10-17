from .base import *

DEBUG = True

DATA_UPLOAD_MAX_NUMBER_FIELDS = 20000

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CSRF_TRUSTED_ORIGINS = ["chrome-extension://eejfoncpjfgmeleakejdcanedmefagga"]

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
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "django.log",
            "formatter": "file",
        },
    },
    "loggers": {"": {"level": "DEBUG", "handlers": ["console", "file"]}},
}
