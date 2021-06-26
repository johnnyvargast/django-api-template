from rest_framework.generics import DestroyAPIView

from apps.rest.generics import BaseGenericAPIView
from apps.rest.mixins import BaseDestroyModelMixin


class BaseDestroyAPIView(BaseDestroyModelMixin, DestroyAPIView, BaseGenericAPIView):
    pass
