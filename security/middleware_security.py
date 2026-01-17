import uuid
from django.http import HttpResponseBadRequest

MAX_BODY_SIZE = 1_000_000  # 1MB


class BasicSecurityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.id = str(uuid.uuid4())

        if request.method not in ['GET', 'POST', 'PUT', 'DELETE']:
            return HttpResponseBadRequest("Método inválido")

        if not request.headers.get('User-Agent'):
            return HttpResponseBadRequest("User-Agent ausente")

        content_length = request.META.get('CONTENT_LENGTH')
        try:
            if content_length and int(content_length) > MAX_BODY_SIZE:
                return HttpResponseBadRequest("Payload muito grande")
        except ValueError:
            return HttpResponseBadRequest("Content-Length inválido")

        return self.get_response(request)
