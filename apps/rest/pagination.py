from rest_framework_json_api.pagination import JsonApiPageNumberPagination


class StandardResultsSetPagination(JsonApiPageNumberPagination):
    """ Default data for pagination """
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    page_size = 10
    max_page_size = 50
