from .models import RequestTracking


class RequestTrackingMiddleware:
    """Track user request"""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)

        if request.user is not None:
            RequestTracking.objects.create(
                user=request.user,
                path=request.path,
                status=response.status_code,
                method=request.method
            )

        return response
