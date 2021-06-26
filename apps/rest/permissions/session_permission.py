from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken

from apps.rest.permissions import BasePermission


class SessionPermission(BasePermission):
    """
    Global permission check for blocked IPs.
    """
    message = 'You are not authenticated.'

    def has_permission(self, request, view):
        authorization = request.headers.get("Authorization")
        if authorization:
            token = authorization.split(" ")[1]
            return not BlacklistedToken.objects.filter(token__token=token).exists()
        return False
