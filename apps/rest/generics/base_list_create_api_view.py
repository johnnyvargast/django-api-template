from rest_framework.generics import ListCreateAPIView

from apps.rest.generics import BaseGenericAPIView
from apps.rest.mixins import BaseListModelMixin, BaseCreateModelMixin


class BaseListCreateAPIView(BaseListModelMixin,
                            BaseCreateModelMixin,
                            ListCreateAPIView,
                            BaseGenericAPIView):
    pass
