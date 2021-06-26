from django.contrib.auth.models import User
from django.db import models
import uuid

from apps.commons.models.managers import BaseModelManager


class BaseModel(models.Model):
    """
    This is base class model for the application models.
    Here we define default fields for all the UserWarning
    Like:  created_at, updated_at, created_by, updated_by
    """
    uuid = models.UUIDField(
        verbose_name='Unique Identifier',
        help_text='Unique Identifier.',
        unique=True,
        default=uuid.uuid4,
        editable=False)

    is_active = models.BooleanField(
        verbose_name='Active',
        default=True,
        help_text='If the record is active or not.')

    is_archived = models.BooleanField(
        verbose_name='Is Archived',
        default=False,
        help_text='If the registration is filed or not.')

    created_at = models.DateTimeField(
        verbose_name='Date Created',
        help_text='Creation Date.',
        auto_now_add=True)

    updated_at = models.DateTimeField(
        verbose_name='Date Updated',
        help_text='Last Update.',
        auto_now=True)

    archived_at = models.DateTimeField(
        verbose_name='Date archived',
        help_text='Date the record was filed',
        null=True, blank=True)

    updated_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name='Updated By',
        help_text='User Who Last Update This Record',
        related_name='+',
        null=True, blank=True)

    created_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name='Created By',
        help_text='User Who Create This Record',
        related_name='+',
        null=True, blank=True)

    archived_by = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name='Deleted By',
        help_text='User Who archived This Record',
        related_name='+',
        null=True, blank=True)

    # default manager
    objects = BaseModelManager()

    LOGGING_IGNORE_FIELDS = ['updated_at']

    class Meta:
        abstract = True
