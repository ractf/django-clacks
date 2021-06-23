"""Relevant Middleware classes used to add our custom header."""

from dataclasses import dataclass
from typing import Callable

from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.utils.functional import cached_property

from clacks import DEFAULT_NAMES


@dataclass
class ClacksMiddleware:
    """Custom middleware to add the 'X-Clacks-Overhead' header to all responses."""

    get_response: Callable[[HttpRequest], HttpResponse]

    def __call__(self, request: HttpRequest) -> HttpResponse:
        """Use the CLACKS_NAMES setting to determine header contents."""
        response = self.get_response(request)
        response.headers["X-Clacks-Overhead"] = self.clacks_content
        return response

    @cached_property
    def clacks_content(self) -> str:
        """Return a comma-separated list of names to use in our header."""
        return "GNU " + ", ".join(getattr(settings, "CLACKS_NAMES", DEFAULT_NAMES))
