# use the droplet ip:
ALLOWED_HOSTS = ['159.89.45.216', 'localhost']
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER': 'sammy',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
STATIC_ROOT = '/home/sammy/static/'
MEDIA_ROOT = '/home/sammy/media/'
