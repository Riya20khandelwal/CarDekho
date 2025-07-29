from rest_framework.pagination import PageNumberPagination

class Reviewlistpagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'pa'
    page_size_query_param = 'size'
    max_page_size = 2
    last_page_strings = 'last'
