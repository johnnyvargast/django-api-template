from django.db import models
from django.utils.text import slugify

from apps.commons.models import BaseModel


class BaseModelWithSlug(BaseModel):
    """
    Add the Slug to the model that inherits from this class.

    In order to use it, it is also necessary to specify
    which fields will be used to create the Slug.

    Override the attribute:
    FIELDS_FOR_SLUG = ['field_example', 'another_field_example']
    """
    slug = models.SlugField(
        verbose_name='Slug',
        help_text='Unique slug for each record.',
        unique=True, blank=True)

    # fields that will be taken to create the slug.
    # overwrite in main model.
    FIELDS_FOR_SLUG = []

    @staticmethod
    def convert_to_slug(instance, fields):
        """ Create a single string with received fields """
        slug = ''
        for item in fields:
            slug = "{} {} ".format(slug, getattr(instance, item))
        slug = slugify(slug)
        return slug

    @staticmethod
    def unique_slug(slug, instance):
        """ Verify that the slug is unique among records """

        def slug_exists(instance, value):
            query = instance.__class__.objects.filter(slug=value)
            # if the record is being edited
            if instance.pk:
                query = query.exclude(id=instance.id)
            return query.exists()

        if slug_exists(instance=instance, value=slug):
            i = 1
            while True:
                slug_x = str(i) + "-" + slug
                if slug_exists(instance=instance, value=slug_x):
                    i += 1
                else:
                    break
            slug_available = slug_x
        else:
            slug_available = slug

        return slug_available

    @classmethod
    def create_slug(cls, instance):
        """ Create slug """
        # list of fields to create the slug
        fields = cls.FIELDS_FOR_SLUG

        if fields:
            if instance.id:
                current_instance = instance.__class__.objects.get(id=instance.id)
                edit_slug = False
                for item in fields:
                    if getattr(current_instance, item) != getattr(instance, item):
                        edit_slug = True
                if edit_slug:
                    slug = cls.convert_to_slug(
                        instance=instance,
                        fields=fields)
                    slug = cls.unique_slug(slug=slug, instance=instance)
                    instance.slug = slug

            else:
                slug = cls.convert_to_slug(
                    instance=instance,
                    fields=fields)
                slug = cls.unique_slug(slug=slug, instance=instance)
                instance.slug = slug

    def save(self, *args, **kwargs):
        """ Create slug """
        self.create_slug(self)
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True
