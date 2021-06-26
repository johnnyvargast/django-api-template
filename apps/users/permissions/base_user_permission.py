from apps.rest.permissions import BasePermission


class BaseUserPermission(BasePermission):
    relationship_name = None

    def has_permission(self, request, view):
        response = super().has_permission(request, view)
        if not response:
            return response

        user = request.user
        if hasattr(user, self.relationship_name):
            return True

        return False
