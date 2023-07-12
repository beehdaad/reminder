from django import forms
from django.utils.translation import gettext_lazy as _

from todo_list.models import Todo


class TodoListModelForm(forms.ModelForm):
    """
    Form for input subject todo list
    """

    class Meta:
        model = Todo
        exclude = (
            "created",
            "modified",
            "priority",
            "status"
        )
        widgets = {
            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "id": "form_subject"
                }
            ),
        }

        labels = {
            "subject": _("Enter a task here"),
            "class": "form-label",
            "for": "form1"
        }

        error_messages = {
            "subject": {
                "required": _("Please enter your subject"),
                "max_length": _("The subject cannot be more than 255 characters")
            },
        }

        max_lengths = {
            "subject": 255,
        }
