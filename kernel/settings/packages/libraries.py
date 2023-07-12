from kernel.settings.base import DEFAULT_APPS

BUSINESS_APPS = [
    'painless.apps.PainlessConfig'
]

INSTALLED_APPS =  DEFAULT_APPS + BUSINESS_APPS
