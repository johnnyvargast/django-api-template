class BaseService:
    """
    Base Class for Model Services

    To obtain the current user you can use 'self.user'
    """
    # by default the logs will be archived,
    # if you want to permanently delete change to True.
    destroy = False

    @staticmethod
    def get_data(serializer, data):
        data = data or (serializer.validated_data if serializer else None) or {}
        return data

    def __init__(self, request=None, user=None):
        self.request = request
        self.user = user or (self.request.user if request else None)

    def create(self, serializer=None, data=None, **kwargs):
        if serializer:
            serializer.save()

    def list(self, queryset, **kwargs):
        return queryset

    def retrieve(self, queryset, **kwargs):
        return queryset

    def update(self, instance, serializer=None, data=None, **kwargs):
        if data is not None:
            for key, value in data.items():
                setattr(instance, key, value)
            instance.save()
        else:
            if serializer:
                instance = serializer.save()

        return instance

    def delete(self, instance, **kwargs):
        if self.destroy:
            instance.delete()
        else:
            instance.is_archived = True
            instance.save()
