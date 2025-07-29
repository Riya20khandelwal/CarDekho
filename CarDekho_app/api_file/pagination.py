from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class Reviewlistpagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'pa'
    page_size_query_param = 'size'
    max_page_size = 2
    last_page_strings = 'last'

class Reviewlistlimitoffpag(LimitOffsetPagination):
    default_limit = 2
    max_limit = 3
    offset_query_param = 'start'
    limit_query_param = 'limitsss'

class Reviewlistcursorpag(CursorPagination):
    page_size = 3
    ordering = 'created'
    # ordering = '-rating'
