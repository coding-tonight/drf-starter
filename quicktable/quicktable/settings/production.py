from base import *

ALLOWED_HOSTS = []

THIRD_PARTY_APPS = [
    'rest_framework'
]

INSTALLED_APPS = DEFAULT_APPS + DJANGO_APPS + THIRD_PARTY_APPS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
