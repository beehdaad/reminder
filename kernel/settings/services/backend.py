from kernel.settings.base import DJANGO_CONFIG

ALLOWED_HOSTS = [host.strip() for host in DJANGO_CONFIG['ALLOWED_HOSTS'].split(',')]
SECRET_KEY = DJANGO_CONFIG['SECRET_KEY']
