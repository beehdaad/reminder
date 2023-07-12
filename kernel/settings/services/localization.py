import os

from kernel.settings.base import (
    BASE_DIR,
    LOCALIZATION_CONFIG
)

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, LOCALIZATION_CONFIG['TRANSLATION_DIR']),
)
