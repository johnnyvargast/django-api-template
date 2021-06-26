from rest_framework.permissions import BasePermission


class PublicRead(BasePermission):
    def has_permission(self, request, view):
        return str(request.method).upper() == "GET"


class PublicCreate(BasePermission):
    def has_permission(self, request, view):
        return str(request.method).upper() == "POST"


class PublicUpdate(BasePermission):
    def has_permission(self, request, view):
        return str(request.method).upper() == "PUT"


class PublicDestroy(BasePermission):
    def has_permission(self, request, view):
        return str(request.method).upper() == "DELETE"
