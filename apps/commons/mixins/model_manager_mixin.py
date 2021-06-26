from rest_framework.exceptions import ValidationError


class ModelManagerMixin:

    def filter_active(self, *args, **kwargs):
        """
        Returns model instance objects with active filter true.

        :return: Queryset of model instances.
        """
        return self.filter(*args, **kwargs, is_active=True)

    def filter_unarchived_active(self, *args, **kwargs):
        """
        Returns model instance objects with active filter
        true and archive filter false.

        :return: Queryset of model instances.
        """
        return self.filter_active(*args, **kwargs, is_archived=False)

    def filter_unarchived(self, *args, **kwargs):
        """
        Returns model instance objects with is_archived in false.

        :return: Queryset of model instances.
        """
        return self.filter(*args, **kwargs, is_archived=False)

    def filter_archived(self, *args, **kwargs):
        """
        Returns model instance objects with is_archived in True.

        :return: Queryset of model instances.
        """
        return self.filter(*args, **kwargs, is_archived=True)

    def filter_by_uuid(self, *args, **kwargs):
        if 'is_archived' in kwargs and 'is_active' in kwargs:
            query = self.filter(**kwargs)
        elif 'is_archived' in kwargs:
            query = self.filter_active(**kwargs)
        else:
            query = self.filter_unarchived(**kwargs)

        if not query:
            msg = 'The UUID is invalid.'
            label = self.model.__name__.lower()
            raise ValidationError({label: [msg]})

        return query
