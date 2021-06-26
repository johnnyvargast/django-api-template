from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models

from apps.commons.constants import Language
from apps.commons.models import BaseModel
from apps.commons.models.validators import generic_image_size
from apps.commons.utils import UploadTo
from apps.commons.validators import validate_time_zone
from apps.users.constants import GenderType
from apps.users.models.managers import BaseUserModelManager


class BaseUserModel(User, BaseModel):
    """ Class for user models """
    surname_prefix = models.CharField(
        verbose_name='Surname Prefix',
        max_length=32,
        help_text='Surname Prefix of the user.',
        null=True, blank=True)

    gender = models.CharField(
        max_length=15,
        choices=GenderType.choices,
        blank=True,
        verbose_name='Gender')

    birth_date = models.DateField(
        verbose_name='Birth date',
        blank=True, null=True)

    current_time_zone = models.CharField(
        max_length=100,
        help_text='Example: America/Bogota',
        validators=[validate_time_zone],
        blank=True, null=True, )

    description = models.TextField(
        verbose_name='Description',
        blank=True, null=True)

    profile_image = models.ImageField(
        verbose_name='Profile image',
        upload_to=UploadTo('profile_image'),
        validators=[
            generic_image_size,
            FileExtensionValidator(['jpg', 'png'])
        ],
        blank=True, null=True)

    current_language = models.CharField(
        verbose_name='Current Language',
        choices=Language.choices,
        max_length=10,
        null=True,
        blank=True)

    # default manager
    objects = BaseUserModelManager()

    def __str__(self):
        model_name = self.__class__.__name__
        return '{}: {}'.format(model_name, self.username)

    @staticmethod
    def encrypt_password(instance):
        """ Encrypt the password """
        password = instance.password

        if instance.id:
            user = User.objects.get(id=instance.id)
            if not user.password == password:
                instance.set_password(password)
        else:
            instance.set_password(password)

    def save(self, *args, **kwargs):
        """ The password is encrypted """
        self.encrypt_password(self)
        return super(BaseUserModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True
