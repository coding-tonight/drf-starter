from .base import *

ALLOWED_HOSTS = ['0.0.0.0']


THIRD_PARTY_APPS = [
    'rest_framework'
]

INSTALLED_APPS = DEFAULT_APPS + DJANGO_APPS + THIRD_PARTY_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'pgdb',
        'PASSWORD': 'postgres',
        'PORT': '5432',
    }
}
