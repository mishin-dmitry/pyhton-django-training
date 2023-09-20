from typing import Any

from django.http import HttpRequest


def set_useragent_on_request_middleware(get_response):
    def middleware(request: HttpRequest):
        request.user_agent = request.META["HTTP_USER_AGENT"]
        response = get_response(request)

        return response

    return middleware


class CountRequestsMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response
        self.requests_count = 0
        self.response_count = 0
        self.exceptions_count = 0

    def __call__(self, request: HttpRequest) -> Any:
        self.requests_count += 1
        response = self.get_response(request)
        self.response_count += 1

        print(
            f"requests_count={self.requests_count}, responses_count={self.response_count}"
        )

        return response

    def process_exception(self, request: HttpRequest, exception: Exception):
        self.exceptions_count += 1
        print(f"Exceptions count={self.exceptions_count}")
