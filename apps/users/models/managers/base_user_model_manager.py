from django.contrib.auth.models import UserManager

from apps.commons.mixins import ModelManagerMixin


class BaseUserModelManager(ModelManagerMixin, UserManager):
    pass
