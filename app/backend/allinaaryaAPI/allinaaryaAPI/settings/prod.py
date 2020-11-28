from .base import *

"""Defines prod environment specific settings. Base config. settings can be overridden"""

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'allinaarya_planner',
        'USER': 'prod-user',
        'PASSWORD': 'prod-password',
        'HOST': 'prod-host',
        'PORT': 'prod-port',
    }
}
