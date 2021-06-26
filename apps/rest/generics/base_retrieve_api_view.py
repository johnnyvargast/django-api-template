from rest_framework.generics import RetrieveAPIView

from apps.rest.generics import BaseGenericAPIView
from apps.rest.mixins import BaseRetrieveModelMixin


class BaseRetrieveAPIView(BaseRetrieveModelMixin,
                          RetrieveAPIView,
                          BaseGenericAPIView):
    lookup_field = "uuid"
