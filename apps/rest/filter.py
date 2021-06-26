import re
from rest_framework_json_api.filters import QueryParameterValidationFilter


class StandardValidationFilter(QueryParameterValidationFilter):
    """ Custom parameter validation filter """

    query_regex = re.compile(r'^(sort|include|page|page_size)$|^(filter|fields|page)(\[[\w\.\-]+\])?$')
