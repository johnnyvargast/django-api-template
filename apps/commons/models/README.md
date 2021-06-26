### Example
```sh
from django.db import models

from apps.commons.models import BaseModel


class Project(BaseModel):
    name = models.CharField(
        max_length=100,
        verbose_name='Name',
        help_text='Name of the company.')

    start_date = models.DateTimeField(
        verbose_name='Start Date',
        help_text='Start Date of the Project.')

    end_date = models.DateTimeField(
        verbose_name='End Date',
        help_text='End Date of the Project.',
        null=True,
        blank=True)

    is_published = models.BooleanField(
        verbose_name='Is Published',
        help_text='Is published or not.',
        default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'jobs_projects'
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ('-id',)


```