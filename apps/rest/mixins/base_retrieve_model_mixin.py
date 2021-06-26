class BaseRetrieveModelMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        service = self.get_service()
        if service:
            queryset = service.retrieve(queryset=queryset)
        return queryset
