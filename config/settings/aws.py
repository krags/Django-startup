import os
from decouple import config
from storages.backends.s3boto3 import S3Boto3Storage

# Amazon S3 Settings
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
print('key= ', AWS_ACCESS_KEY_ID)
print('secret= ', AWS_SECRET_ACCESS_KEY)
print('storage= ', AWS_STORAGE_BUCKET_NAME)
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
DEFAULT_FILE_STORAGE = 'storages.backends.s3Boto3.S3Boto3Storage'

AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
AWS_LOCATION = 'static'
AWS_QUERYSTRING_AUTH = False
AWS_HEADERS = {'Access-Control-Allow-Origin': '*',}
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3ManifestStaticStorage'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'

# Aws operations information
# storages and boto3 are required.
# Change config to config()
