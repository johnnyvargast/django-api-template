from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.rest.generics import BaseGenericAPIView
from apps.rest.mixins import BaseRetrieveModelMixin, BaseUpdateModelMixin, BaseDestroyModelMixin


class BaseRetrieveUpdateDestroyAPIView(BaseRetrieveModelMixin,
                                       BaseUpdateModelMixin,
                                       BaseDestroyModelMixin,
                                       RetrieveUpdateDestroyAPIView,
                                       BaseGenericAPIView):
    http_method_names = ['get', 'put', 'delete']
    lookup_field = "uuid"
