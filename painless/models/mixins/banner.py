from django.db import models
from django.utils.translation import gettext_lazy as _


class BannerOpMixin(models.Model):
    """"""

    banner_height_field = models.PositiveSmallIntegerField(
        _("Banner height field"),
        null=True,
        editable=False,
        help_text=_("Height of the banner")
    )

    banner_width_field = models.PositiveSmallIntegerField(
        _("Banner width field"),
        null=True,
        editable=False,
        help_text=_("Width of the banner")
    )

    banner_alternate_text = models.CharField(
        max_length=100,
        help_text=_("Description of the banner")
    )

    class Meta:
        abstract = True
