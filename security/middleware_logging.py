import time
from .models import RequestLog


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)

        duration = time.time() - start_time

        if request.path.startswith(('/admin', '/static')):
            return response

        try:
            if request.content_type in [
                'application/json',
                'application/x-www-form-urlencoded'
            ]:
                body = request.body[:2000].decode('utf-8', errors='replace')
            else:
                body = 'Body não logado'
        except Exception as e:
            body = f"Erro ao ler body: {e}"

        try:
            response_body = response.content[:2000].decode(
                'utf-8', errors='replace'
            )
        except Exception:
            response_body = ''

        RequestLog.objects.create(
            method=request.method,
            url=request.path,
            body=body,
            duration=duration,
            response_status=response.status_code,
            response_body=response_body
        )

        return response
