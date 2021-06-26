from django.contrib.admin import ModelAdmin
from model_log.mixins import ModelAdminMixin


class BaseModelAdmin(ModelAdminMixin, ModelAdmin):
    """
    Base class for ModelAdmin.

    To use the default values,
    use the properties with the initial name 'custom_'.

    if you want to use the default values of "search_fields",
    and add more fields:

    Example:
        - custom_search_fields = ['name']

    Custom properties:
        - list_display
        - search_fields
        - readonly_fields
        - list_filter

    If you don't want to use the default values of a property,
    just use the original property.

    Example:
        - search_fields = ['name']
    """
    custom_list_display = []
    custom_search_fields = []
    custom_readonly_fields = []
    custom_list_filter = []
    custom_raw_id_fields = []
    ordering = ('-created_at',)
    list_per_page = 50

    def __init__(self, model, admin_site):
        self.assign_default_values()
        super().__init__(model, admin_site)

    def assign_default_values(self):
        """
        Assign default values if custom properties were used.

        Default values apply if the value of
        the original properties has not been modified.
        """
        class_origin = ModelAdmin

        if self.list_display == class_origin.list_display:
            self.list_display = self.set_list_display()

        if self.search_fields == class_origin.search_fields:
            self.search_fields = self.set_search_fields()

        if self.readonly_fields == class_origin.readonly_fields:
            self.readonly_fields = self.set_readonly_fields()

        if self.list_filter == class_origin.list_filter:
            self.list_filter = self.set_list_filter()

        if self.raw_id_fields == class_origin.raw_id_fields:
            self.raw_id_fields = self.set_raw_id_fields()

    def set_list_display(self):
        initial_list = [
            'id',
            'uuid',
        ]
        final_list = [
            'updated_at',
            'created_at',
            'is_archived',
            'is_active',
        ]
        initial_list += self.custom_list_display + final_list
        return initial_list

    def set_search_fields(self):
        search_fields = [
            'id',
            'uuid',
        ]
        search_fields += self.custom_search_fields
        return search_fields

    def set_readonly_fields(self):
        readonly_fields = [
            'id',
            'uuid',
            'created_by',
            'created_at',
            'updated_by',
            'updated_at',
            'archived_at',
            'archived_by',
        ]
        readonly_fields += self.custom_readonly_fields
        return readonly_fields

    def set_list_filter(self):
        list_filter = [
            'created_at',
            'updated_at',
            'is_archived',
            'is_active',
        ]
        list_filter += self.custom_list_filter
        return list_filter

    def set_raw_id_fields(self):
        raw_id_fields = [
            'updated_by',
            'created_by',
            'archived_by',
        ]
        raw_id_fields += self.custom_raw_id_fields
        return raw_id_fields
