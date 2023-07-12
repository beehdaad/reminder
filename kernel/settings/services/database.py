from kernel.settings.base import DATABASE_CONFIG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_CONFIG['DB_NAME'],
        'USER': DATABASE_CONFIG['DB_USER'],
        'PASSWORD': DATABASE_CONFIG['DB_PASSWORD'],
        'HOST': DATABASE_CONFIG['DB_HOST'],
        'PORT': DATABASE_CONFIG['DB_PORT'],
        'TEST': {
            'NAME': DATABASE_CONFIG['DB_TEST']
        }
    }
}
