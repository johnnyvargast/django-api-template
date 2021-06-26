from rest_framework_json_api import serializers
from rest_framework_simplejwt.state import token_backend


class LogoutSerializer(serializers.Serializer):
    access = serializers.CharField()

    def validate(self, attrs):
        field_name = 'access'
        access = attrs[field_name]
        try:
            token_backend.decode(access)
        except Exception as ex:
            raise serializers.ValidationError({field_name: [ex]})

        return super().validate(attrs)
