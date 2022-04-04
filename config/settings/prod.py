from .base import *
from decouple import config
import django_on_heroku
import dj_database_url
import django_heroku
from pathlib import Path


DEBUG = config('DEBUG')

ALLOWED_HOSTS = ['keithragsdale.com', 'www.keithragsdale.com', 'agile-gorge-76642.herokuapp.com']

# Heroku Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'MYAPP': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}

# Database setup
DATABASES = {}
DATABASES['default'] = dj_database_url.config(config('DATABASE_URL'))
django_on_heroku.settings(locals())

# Amazon S3 Settings
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')

AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3Boto3.S3Boto3Storage'

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_LOCATION = 'static'
AWS_QUERYSTRING_AUTH = False
AWS_HEADERS = {'Access-Control-Allow-Origin': '*',}
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3ManifestStaticStorage'

# Do this after we get this working without S3.
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'



django_heroku.settings(locals())

# Static application files.
STATIC_URL = '/static/'
MEDIA_URL = '/images/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_ROOT = BASE_DIR / 'static/images'
STATIC_ROOT = BASE_DIR / 'staticfiles'