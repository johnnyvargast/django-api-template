from rest_framework.generics import ListAPIView

from apps.rest.generics import BaseGenericAPIView
from apps.rest.mixins import BaseListModelMixin


class BaseListAPIView(BaseListModelMixin, ListAPIView, BaseGenericAPIView):
    pass
