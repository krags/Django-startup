from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# Development only
DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': 'postgres',
       'USER': 'postgres',
       'PASSWORD': 'qazwsxedcr',
       'HOST': 'localhost',
       'PORT': '5432',
   }
}

STATICFILES_DIRS = [
	BASE_DIR / "static", 
    BASE_DIR / "media",

]
# Static application files.
STATIC_URL = "/static/"

#Collectstatic collects static files here.
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

#File uploads location.
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'