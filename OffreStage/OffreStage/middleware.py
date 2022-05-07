from django.shortcuts import redirect

from . import settings


class RequiredLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        response = self.get_response(request)
        return response

    def process_request(self, request):
        if not request.user.is_authenticated:
            return redirect("/account/login")
