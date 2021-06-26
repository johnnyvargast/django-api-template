from django.db import models


class UpperCharField(models.CharField):
    """ Custom field to store its value in uppercase """

    def get_prep_value(self, value):
        if value:
            value = value.upper()
        return super().get_prep_value(value)


class LowerCharField(models.CharField):
    """ Custom field to save its value in lowercase """

    def get_prep_value(self, value):
        if value:
            value = value.lower()
        return super().get_prep_value(value)


class CustomEmailField(models.EmailField):

    def __init__(self, *args, **kwargs):
        super(CustomEmailField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if value is None:
            return value

        return value.lower()
