from django.db import models
from django.utils.translation import gettext_lazy as _


class LogoOpMixin(models.Model):
    """"""

    logo_height_field = models.PositiveSmallIntegerField(
        _("Logo height field"),
        null=True,
        editable=False,
        help_text=_("Height of the logo")
    )

    logo_width_field = models.PositiveSmallIntegerField(
        _("Logo width field"),
        null=True,
        editable=False,
        help_text=_("Width of the logo")
    )

    logo_alternate_text = models.CharField(
        max_length=100,
        help_text=_("Description of the logo")
    )

    class Meta:
        abstract = True
