from django.db import models
from django.utils.translation import gettext_lazy as _


class PictureOpMixin(models.Model):
    """"""

    pic_height_field = models.PositiveSmallIntegerField(
        _("Picture height field"),
        null=True,
        editable=False,
        help_text=_("Height of the picture")
    )

    pic_width_field = models.PositiveSmallIntegerField(
        _("Picture width field"),
        null=True,
        editable=False,
        help_text=_("Width of the picture")
    )

    pic_alternate_text = models.CharField(
        max_length=100,
        help_text=_("Description of the image")
    )

    class Meta:
        abstract = True
