import os
from pathlib import Path

from . import config


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

DJANGO_CONFIG = config['django']
DATABASE_CONFIG = config['database']
STATIC_CONFIG = config['static']
LOCALIZATION_CONFIG = config['localization']

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kernel.urls'

TEMPLATE_DIR = os.path.join(BASE_DIR, STATIC_CONFIG['TEMPLATE_DIR']) 

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kernel.wsgi.application'

# Default primary key type
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

#################
#    STATIC    #
################

STATIC_URL = STATIC_CONFIG['STATIC_URL']

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, STATIC_CONFIG['STATIC_DIR']),
)

STATIC_ROOT = os.path.join(BASE_DIR, STATIC_CONFIG['COLLECT_STATIC_DIR'])

MEDIA_URL = STATIC_CONFIG['MEDIA_URL']

MEDIA_ROOT = STATIC_CONFIG['MEDIA_UPLOAD_DIR']

FIXTURES_DIRS = STATIC_CONFIG['FIXTURE_TEST_DIRS']
