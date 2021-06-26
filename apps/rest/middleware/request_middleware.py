try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

from threading import local


class _RequestLocal(local):
    """
    Class for storing the request as local variable per thread
    """
    request = None


_request_local = _RequestLocal()


class RequestMiddleware(MiddlewareMixin):

    def process_request(self, request):
        _request_local.request = request

    def process_response(self, request, response):
        if hasattr(_request_local, "request"):
            del _request_local.request
        return response


def get_current_user():
    if _request_local.request and _request_local.request.user and _request_local.request.user.is_authenticated:
        return _request_local.request.user
    return None
