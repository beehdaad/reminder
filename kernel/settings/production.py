from .base import *
from .services import *
from .packages import *

DEBUG = False if DJANGO_CONFIG['DEBUG'] else True
