from rest_framework import pagination, serializers
from rest_framework.response import Response
from .base_response import JsonPaginateResponse

class CustomPagination(pagination.PageNumberPagination):
    page_size_query_param = 'limit'
    page_query_param = 'page'

    min_limit = 5
    max_limit = 1000
    min_page = 1
    max_page = 1000

    def paginate_queryset(self, queryset, request, view=None):

        try:

            limit = request.query_params.get(self.page_size_query_param)
            page = request.query_params.get(self.page_query_param)

            # Validate limit
            if limit is not None:
                try:
                    limit = int(limit)
                except ValueError:
                    raise serializers.ValidationError({
                        "limit": ["Limit must be an integer."]
                    })

                if limit < self.min_limit:
                    raise serializers.ValidationError({
                        "limit": [f"Limit must be >= {self.min_limit}"]
                    })

                if limit > self.max_limit:
                    raise serializers.ValidationError({
                        "limit": [f"Limit must be <= {self.max_limit}"]
                    })

            # Validate page
            if page is not None:
                try:
                    page = int(page)
                except ValueError:
                    raise serializers.ValidationError({
                        "page": ["Page must be an integer."]
                    })

                if page < self.min_page:
                    raise serializers.ValidationError({
                        "page": [f"Page must be >= {self.min_page}"]
                    })

                if page > self.max_page:
                    raise serializers.ValidationError({
                        "page": [f"Page must be <= {self.max_page}"]
                    })

            return super().paginate_queryset(queryset, request, view)
        except Exception as e:
            print('Its act here')
            request.query_params['page'] = self.min_page
            request.query_params['limit'] = self.min_limit
            return super(self.__class__, self).paginate_queryset(queryset, request, view)
    
    def get_paginated_response(self, data, is_custom_data=False):
       links = {
            'next': self.get_next_link(),
            'previous': self.get_previous_link()
       }
       
       if is_custom_data:
           return data, self.page.paginator.count, links
       
       return JsonPaginateResponse(data, self.page.paginator.count, links)