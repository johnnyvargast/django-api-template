from django.conf import settings
from django.contrib import admin

from .base_model_admin import BaseModelAdmin

# change the url of django admin "VIEW SITE"
admin.site.site_url = "/" + settings.DOCUMENTATION_PATH_NAME
