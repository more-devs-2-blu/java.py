from django.utils.deprecation import MiddlewareMixin
from django.views.decorators.csrf import csrf_exempt

class CsrfExemptMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST':
            request._dont_enforce_csrf_checks = True

        response = self.get_response(request)
        return response