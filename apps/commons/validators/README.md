### Example
```sh
from apps.commons.admin import BaseModelAdmin

class ExampleModel(BaseModel):
    current_time_zone = models.CharField(
        max_length=100,
        help_text='Example: America/Bogota',
        validators=[validate_time_zone],
        blank=True, null=True)

```