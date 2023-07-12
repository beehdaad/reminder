from django.db import models
from django.utils.translation import gettext_lazy as _


class IconOpMixin(models.Model):
    """"""

    icon_height_field = models.PositiveSmallIntegerField(
        _("Icon height field"),
        null=True,
        editable=False,
        help_text=_("Height of the icon")
    )

    icon_width_field = models.PositiveSmallIntegerField(
        _("Banner width field"),
        null=True,
        editable=False,
        help_text=_("Width of the icon")
    )

    icon_alternate_text = models.CharField(
        max_length=100,
        help_text=_("Description of the icon")
    )

    class Meta:
        abstract = True
