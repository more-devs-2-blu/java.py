from ..settings import DEBUG

def baseUrl(request):
    if DEBUG:
        return {'BASE_URL': request.build_absolute_uri('/')}
    return {'BASE_URL': f"https://{request.META['HTTP_HOST']}"}