from rest_framework.generics import RetrieveDestroyAPIView

from apps.rest.generics import BaseGenericAPIView
from apps.rest.mixins import BaseRetrieveModelMixin, BaseDestroyModelMixin


class BaseRetrieveDestroyAPIView(BaseRetrieveModelMixin,
                                 BaseDestroyModelMixin,
                                 RetrieveDestroyAPIView,
                                 BaseGenericAPIView):
    http_method_names = ['get', 'delete']
    lookup_field = "uuid"
