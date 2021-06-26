### Example
```sh
from rest_framework_json_api import serializers

from apps.jobs.models import Project
from apps.rest.serializers import BaseModelSerializer


class ProjectSerializer(BaseModelSerializer):
    class Meta:
        model = Project
        fields = [
            'name',
            'start_date',
            'end_date',
            'is_published',
        ]

```