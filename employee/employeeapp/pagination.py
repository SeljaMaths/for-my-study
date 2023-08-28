from rest_framework import pagination
from rest_framework.response import Response


class employee_pagination(pagination.PageNumberPagination):
    page_size = 2


class employee_limitpagination(pagination.LimitOffsetPagination):
    default_limit = 2
    max_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'start'


class employee_cursorpagination(pagination.CursorPagination):
    page_size = 2
    ordering = "age"


class custompagination(pagination.PageNumberPagination):
    page_size = 2

    def get_paginated_response(self, data):
        return Response(
            {'navigation':{
                'next_page':self.get_next_link(),
                'previous_page':self.get_previous_link(),
            },
                'page_count':self.page.paginator.count,
                'current_page':self.page.number,
                'results':data
            }
        )
