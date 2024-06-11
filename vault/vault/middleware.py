from django.http import HttpResponse
from login.views import Login
from django.shortcuts import render


def globalmiddleware(get_response):
    # One-time configuration or setup logic goes here

    def middleware(request):
        if Login:
            allowed_methods = ["GET","POST"]
        if request.method in allowed_methods:
            return Login(request)
        else:
            # Middleware logic for disallowed methods
            return HttpResponse(f"Request method {request.method} is not allowed")

        # Continue with the request processing
        response = get_response(request)

        # Middleware logic after the view is called
        return response

    return middleware
