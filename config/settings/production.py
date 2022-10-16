from .base import *

DEBUG = False

ALLOWED_HOSTS = ['domain.com', 'www.domain.com']

LOGGING = {
    "version": 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '%(name)-12s %(levelname)-8s %(message)s'
        },
        'file': {
            "format": (
                u"%(asctime)s [%(levelname)-8s] "
                "(%(name)s) %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'console'
        },
        'file': {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "django.log",
            "formatter": "file",
        }
    },
    "loggers": {
        '': {
            'level': 'INFO',
            'handlers': ['console', 'file']
        }
    }
}
