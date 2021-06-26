from rest_framework import permissions


class BasePermission(permissions.IsAuthenticated):
    message = 'The action taken is not allowed.'
