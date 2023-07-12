from django.db import models
from django.utils.translation import gettext_lazy as _

from todo_list.helper import TodoStatus
from painless.models.mixins import TimestampMixin


class Todo(TimestampMixin):
    """
    It is responsible for saving the tasks that need to be done
    The save method automatically prioritizes when it is called
    And when the delete method is called,
    it deletes the object and the priority of the slave is done again
    """

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
        max_length=11,
        default=TodoStatus.IN_PROGRESS,
        choices=TodoStatus.choices,
        help_text=_("Status item"),
    )

    class Meta:
        db_table_comment = "User todo list"
        verbose_name = _("Todo")
        verbose_name_plural = _("Todo list")

    def save(self, *args, **kwargs):

        if not self.pk:  # Only for new instances
            qs = Todo.objects.order_by('created').last()
            if qs:
                self.priority = qs.priority + 1
            else:
                self.priority = 1

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.status is not None:
            super().delete(*args, **kwargs)
            qs = Todo.objects.order_by('created')
            number = 1
            for item in qs:
                item.priority = number
                number += 1
                item.save()

    def __str__(self):
        return f"{self.subject}"

    def __repr__(self):
        return f"<Todo: {self.subject}>"
