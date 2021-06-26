import pytz
from django.utils.timezone import datetime
from pytz import timezone


class GenericDateTimeOperations:
    """
    All the generic date and time related operations.
    """

    DATE_FORMAT = '%d-%m-%Y'
    DATE_TIME_FORMAT = '%d-%m-%Y %H:%M'
    DATE_TIME_FORMAT_DB = '%Y-%m-%d %H:%M:%S'

    def get_current_datetime(self):
        """
        Return current date time object.

        :return object: date-time object
        """
        current_datetime = datetime.now(pytz.utc)
        return current_datetime

    def get_current_time(self):
        """
        Return current time object.

        :return object: time object
        """
        current_datetime = self.get_current_datetime()
        return current_datetime.time()

    def date_to_string(self, date_obj, date_format=None, tz=None):
        """
        Convert the date and time object into a string
        and in the format passed by parameter, in case it is not received by parameter,
        it will take the default format, which is in 'self.DATE_FORMAT'

        :param date_obj: date-time object
        :param date_format: date-time string format
        :param tz: timezone timezone format
        :return: converted date as string
        """
        timezone = pytz.timezone(tz) if tz else pytz.utc
        date_obj = date_obj.astimezone(timezone)
        date_format = date_format or self.DATE_FORMAT
        date_obj = date_obj.strftime(date_format)

        return date_obj

    def change_timezone(self, date_obj, tz=None):
        """
        Change the timezone of the date object received by parameter

        :param date_obj: date-time object
        :param tz: (str) UTC
        """
        if tz:
            tz = timezone(tz)
            return date_obj.astimezone(tz)

        return date_obj.astimezone(pytz.utc)

    def get_current_datetime_in_code(self):
        """
        Return the current date and time in a string
        without symbols and without spaces.
        """
        date_obj = self.get_current_datetime()
        date_code = date_obj.strftime('%d%m%Y%H%M%S')
        return date_code

    def get_datetime_with_timezone(self, tz=None):
        """
        Return the current date and time applying the time zone.

        If you don't have time zone then return only current date and time

        :param tz: (str) time zone
        :return: (datetime) date and time
        """

        date = self.get_current_datetime()
        date = self.change_timezone(date_obj=date, tz=tz)

        return date
