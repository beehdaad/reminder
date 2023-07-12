from django.core.validators import BaseValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.utils.deconstruct import deconstructible
from django.core.files.images import get_image_dimensions


@deconstructible
class DimensionValidator(BaseValidator):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __call__(self, value):
        pic = value.file.open()
        width, height = get_image_dimensions(pic)
        if width > self.width and height > self.height:
            raise ValidationError(
                _(
                    f"The {width} and {height} of the photo must be equal. (square crop)"
                ),
                code=self.code
            )
