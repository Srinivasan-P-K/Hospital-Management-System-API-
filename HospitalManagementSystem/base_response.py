from django.http import JsonResponse as DefaultJsonResponse

class JsonErrorResponse(DefaultJsonResponse):

    def __init__(self, error, **kwargs):
        super().__init__({'result': 0, 'data': None, 'error': error, 'stackTrace': ''}, **kwargs)

class JsonCatchErrorResponse(DefaultJsonResponse):

    def __init__(self, stackTrace, **kwargs):
        super().__init__({'result':-1, 'data': None, 'error': stackTrace, 'stackTrace': 'Internal Server Error'}, **kwargs)

class JsonResponse(DefaultJsonResponse):

    def __init__(self, data={}, **kwargs):
        super().__init__({'result': 1, 'data': data, 'error': None, 'stackTrace': ''}, **kwargs)

class JsonPaginateResponse(DefaultJsonResponse):
    def __init__(self, data = {}, count = 0, links = {}, **kwargs):
        super().__init__({'result':1, 'count': count, 'links': links, 'data': data, 'error': None, 'stackTrace': ''}, **kwargs)

class JsonSessionExpiredResponse(DefaultJsonResponse):
    def __init__(self, detail, code, **kwargs):
        super().__init__({'detail': detail, 'code': code}, status=401, **kwargs)
