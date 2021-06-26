from rest_framework.generics import RetrieveUpdateAPIView

from apps.rest.generics import BaseGenericAPIView
from apps.rest.mixins import BaseRetrieveModelMixin, BaseUpdateModelMixin


class BaseRetrieveUpdateAPIView(BaseRetrieveModelMixin,
                                BaseUpdateModelMixin,
                                RetrieveUpdateAPIView,
                                BaseGenericAPIView):
    http_method_names = ['get', 'put']
    lookup_field = "uuid"
