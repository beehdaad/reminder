from django.db import models
from django.utils.translation import gettext_lazy as _


class TodoStatus(models.TextChoices):
    IN_PROGRESS = ('in progress', _('In Progress'))
    COMPLETED = ('completed', _('Completed'))
    CANCEL = ('cancel', _('Cancel'))
