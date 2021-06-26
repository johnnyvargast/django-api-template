### Example
```sh
from django.contrib import admin

from apps.commons.admin import BaseModelAdmin
from apps.jobs.models import Project


@admin.register(Project)
class ProjectAdmin(BaseModelAdmin):
    custom_list_display = [
        'name',
        'start_date',
        'end_date',
        'is_published',
    ]

    list_filter = [
        'is_published',
    ]

```