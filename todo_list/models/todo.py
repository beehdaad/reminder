from django.db import models
from django.utils.translation import gettext_lazy as _

from todo_list.helper import TodoStatus
from painless.models.mixins import TimestampMixin


class Todo(TimestampMixin):
    """"""

    subject = models.CharField(
        _("Subject"),
        max_length=255,
        help_text=_("The subject of the todo"),
    )

    priority = models.IntegerField(
        _("Priority"),
        help_text=_("item prioritization"),
    )

    status = models.CharField(
        _("Status"),
        max_length=10,
        default=TodoStatus.IN_PROGRESS,
        choices=TodoStatus.choices,
        help_text=_("Status item"),
    )

    class Meta:
            db_table_comment = "User todo list"
            verbose_name = _("Todo")
            verbose_name_plural = _("Todo list")

    def __str__(self):
        return f"{self.subject}"

    def __repr__(self):
        return f"<Todo: {self.subject}>"
