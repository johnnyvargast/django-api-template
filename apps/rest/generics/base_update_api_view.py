from rest_framework.generics import UpdateAPIView

from apps.rest.generics import BaseGenericAPIView
from apps.rest.mixins import BaseUpdateModelMixin


class BaseUpdateAPIView(BaseUpdateModelMixin, UpdateAPIView, BaseGenericAPIView):
    http_method_names = ['put']
    lookup_field = "uuid"
