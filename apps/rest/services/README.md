### Example
```sh
from apps.jobs.models import Project
from apps.rest.services import BaseService


class ProjectService(BaseService):

    def list(self, queryset, **kwargs):
        return queryset.filter(user=self.user)

    def create(self, serializer=None, data=None, **kwargs):
        data = self.get_data(serializer, data)

        instance = Project.objects.create(
            user=self.user,
            **data)
        return instance

    def update(self, instance, serializer=None, data=None, **kwargs):
        data = self.get_data(serializer, data)

        return super().update(instance, serializer, data)

```