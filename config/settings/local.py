from .base import *

DEBUG = True

DATA_UPLOAD_MAX_NUMBER_FIELDS = 20000

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CSRF_TRUSTED_ORIGINS = ['chrome-extension://eejfoncpjfgmeleakejdcanedmefagga']
