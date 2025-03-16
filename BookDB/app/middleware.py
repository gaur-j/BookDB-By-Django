from django.utils.deprecation import MiddlewareMixin

class MyCustomMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f"User IP: {request.META.get('REMOTE_ADDR')}")

