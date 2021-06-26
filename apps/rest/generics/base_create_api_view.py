from rest_framework.generics import CreateAPIView

from apps.rest.generics import BaseGenericAPIView
from apps.rest.mixins import BaseCreateModelMixin


class BaseCreateAPIView(BaseCreateModelMixin, CreateAPIView, BaseGenericAPIView):
    pass
