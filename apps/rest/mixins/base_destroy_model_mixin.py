class BaseDestroyModelMixin:
    method_delete_name = "delete"

    def perform_destroy(self, instance):
        service = self.get_service()
        if service:
            eval("service.{}(instance=instance)".format(self.method_delete_name))
        else:
            super().perform_destroy(instance)
