from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.utils import block_token
from apps.users.rest_api.serializers import LogoutSerializer


class LogoutView(APIView):
    permission_classes = [AllowAny, ]

    @swagger_auto_schema(responses={status.HTTP_200_OK: LogoutSerializer()}, request_body=LogoutSerializer)
    def post(self, request, *args, **kwargs):
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data['access']
        block_token(token=token)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
