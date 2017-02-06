# settings/local.py

from .base import *  # this is one of the only times splat imports are ok

DEBUG = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hivemind_powerball',
        'USER': 'overmind',
        'PASSWORD': '0b3y!',
        'HOST': 'localhost',
        'PORT': 5432,
        'TEST': {
            'NAME': 'test_hivemind_powerball',
        }
    }
}

INSTALLED_APPS += ('debug_toolbar',)

MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

INTERNAL_IPS = ['127.0.0.1',]
