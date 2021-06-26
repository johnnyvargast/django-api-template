from apps.commons.utils import GenericObjectOperations
from . import BaseModelSerializer


class BaseModelOutputSerializer(BaseModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        name = GenericObjectOperations.format_class_name(text=self.Meta.model.__name__)

        if self.context.get("fields", None):
            fields = self.context.pop("fields")
            self.Meta.fields = fields

        if self.context.get("current_serializer", None):
            current_serializer = self.context.get("current_serializer")
            current_name = GenericObjectOperations.format_class_name(
                text=current_serializer.Meta.model.__name__)
            name = "{}.{}".format(current_name, name)

        if self.context.get("include", None):
            if self.context['include'].get(name, None):
                fields = self.context['include'].pop(name)
                self.Meta.fields = fields

                if not self.context['include']:
                    self.context.pop("include")
