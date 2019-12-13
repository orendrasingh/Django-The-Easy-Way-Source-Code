# Use this file only in production. Rename it as "local_settings.py".

import os
from mysite.settings import BASE_DIR

SECRET_KEY = 'SECRET_KEY'
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'IP']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER': 'DATABASE_USERNAME',
        'PASSWORD': 'DATABASE_PASSWORD',
        'HOST': 'localhost',
        'PORT': '',
    }
}
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
