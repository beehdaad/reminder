from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib import admin
from django.utils.text import slugify


__all__ = [
    "TitleSlugMixin",
    "TitleSlugSummaryMixin",
    "TitleSlugSummaryDescriptionMixin"
]

class TitleSlugMixin(models.Model):
    """"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__class__.title.field.help_text = _(
            "Title of {}".format(self.__class__.__name__)
        )

    title = models.CharField(
        max_length=255,
        null=False,
        unique=True,
        help_text=_("Title")
    )

    slug = models.SlugField(
        max_length=255,
        editable=False,
        allow_unicode=True,
        unique=True,
        help_text=_(
            "Slug is a news paper term, A short label for"
            "a text containing only letters, numbers and underscores"
            "or hyphens, generally used in URLs."
        )
    )

    class Meta:
        abstract=True

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title, allow_unicode=True)
        super().save(*args, **kwargs)


class TitleSlugSummaryMixin(TitleSlugMixin):
    """"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__class__.summary.field.help_text = _(
            "Summary of {}".format(self.__class__.__name__)
        )

    summary = models.CharField(
        _("Summary"),
        max_length=255,
        unique=True,
    )

    class Meta:
        abstract=True


class TitleSlugSummaryDescriptionMixin(TitleSlugSummaryMixin):
    """"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__class__.description.field.help_text = _(
            "Description of {}".format(self.__class__.__name__)
        )

    description = models.TextField(
        _("Description"),
        unique=True,
    )

    class Meta:
        abstract=True
