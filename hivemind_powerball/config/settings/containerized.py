# settings/containerized.py

from .base import *  # this is one of the only times splat imports are ok

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
        'TEST': {
            'NAME': 'test_hivemind_powerball',
        }
    }
}

ALLOWED_HOSTS = ['0.0.0.0',
                 '127.0.0.1',]
