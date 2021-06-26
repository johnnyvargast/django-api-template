from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.users.utils import get_user


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = get_user(user=self.user)
        user = {
            "uuid": getattr(user, 'uuid', None),
            "username": user.username,
            "email": user.email
        }
        data["user"] = user
        return data
