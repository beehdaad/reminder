from kernel.settings.base import DEFAULT_APPS

BUSINESS_APPS = [
    'painless.apps.PainlessConfig',
    'todo_list.apps.TodoListConfig'
]

INSTALLED_APPS =  DEFAULT_APPS + BUSINESS_APPS
