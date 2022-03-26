from .base import *

SECRET_KEY = 'abc'
DEBUG = True
ALLOWED_HOSTS = ['*']

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'checkstatic/static')]

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL =  '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
print('MEDIA_URL -> ', MEDIA_URL)
print('MEDIA_ROOT -> ', MEDIA_ROOT)

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