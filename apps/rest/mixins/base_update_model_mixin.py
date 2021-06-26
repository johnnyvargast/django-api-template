from rest_framework.response import Response


class BaseUpdateModelMixin:
    method_update_name = "update"

    def perform_update(self, serializer):
        service = self.get_service()
        if service:
            response = eval(
                "service.{}("
                "instance=self.get_object(),"
                "serializer=serializer,"
                "data=serializer.validated_data"
                ")".format(self.method_update_name)
            )
            if response:
                return response
        else:
            instance = serializer.save()
            return instance

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', True)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        instance = self.perform_update(serializer)
        if instance and self.output_serializer:
            serializer = self.output_serializer(instance)

        return Response(serializer.data)
