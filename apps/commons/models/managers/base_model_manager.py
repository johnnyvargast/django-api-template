from django.db import models

from apps.commons.mixins import ModelManagerMixin


class BaseModelManager(ModelManagerMixin, models.Manager):
    """ Custom model manager """
    pass
