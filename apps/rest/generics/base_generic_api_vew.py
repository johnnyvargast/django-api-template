class BaseGenericAPIView:
    service = None
    output_serializer = None

    def get_service(self):
        if self.service:
            return self.service(request=self.request)
        return None
