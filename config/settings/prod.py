from .aws import *
import os
from decouple import config
import django_on_heroku
import dj_database_url
from pathlib import Path
from storages.backends.s3boto3 import S3Boto3Storage

BASE_DIR = Path(__file__).resolve().parent.parent.parent
TEMPLATES_DIR =  os.path.join(BASE_DIR, "templates")
SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['keithragsdale.com', 'agile-gorge-76642.herokuapp.com']

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'pages.apps.PagesConfig',
    'quotes.apps.QuotesConfig',
    'resume_pics.apps.ResumePicsConfig',
    'my_app.apps.AppConfig',
    'django.contrib.admindocs',
    'django_extensions',
    'storages',
    'blog',
    'django_bootstrap5',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "config.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"
    },
]

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

LANGUAGE_CODE = "en-us"
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Database setup
DATABASES = {}
DATABASES['default'] = dj_database_url.config(config('DATABASE_URL'))
django_on_heroku.settings(locals())

