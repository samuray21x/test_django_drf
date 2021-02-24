import logging

from django.shortcuts import HttpResponse
from django.http import JsonResponse


logger = logging.getLogger(__name__)


class MainExceptionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        logger.error(exception)
        return HttpResponse(content='Unknown server error', status=500)
