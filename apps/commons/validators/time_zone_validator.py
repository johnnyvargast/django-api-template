import pytz
from django.core.exceptions import ValidationError


def validate_time_zone(value):
    if value not in pytz.all_timezones:
        raise ValidationError('Invalid timezone string')
