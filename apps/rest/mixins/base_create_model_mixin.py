from rest_framework import status
from rest_framework.response import Response


class BaseCreateModelMixin:
    method_post_name = "create"

    def perform_create(self, serializer):
        service = self.get_service()
        if service:
            response = eval(
                "service.{}("
                "serializer=serializer,"
                "data=serializer.validated_data"
                ")".format(self.method_post_name)
            )
            if response:
                return response
        else:
            instance = serializer.save()
            return instance

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_create(serializer)

        if instance and self.output_serializer:
            serializer = self.output_serializer(instance)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
