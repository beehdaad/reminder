from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from todo_list.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    """"""

    list_display = (
        "subject",
        "priority",
        "status",
        "created",
        "modified"
    )

    list_filter = (
        "status",
        "created"
    )

    search_fields = (
        "subject",
    )

    readonly_fields = (
        "created",
        "modified"
    )

    fields = (
        "subject",
        "priority",
        "status"
    )
    
    save_on_top = True
