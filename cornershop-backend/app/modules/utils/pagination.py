from rest_framework import pagination
from rest_framework.response import Response
from app import settings
from .services import get_url
import collections


class CustomPagination(pagination.PageNumberPagination):
    page_size = settings.PAGE_SIZE
    url = settings.URL

    def get_paginated_response(self, data):
        next_url = None
        previous_url = None
        if self.get_next_link() is not None:
            temporal_url = get_url(self.get_next_link())
            next_url = self.url + temporal_url
        if self.get_previous_link() is not None:
            temporal_url = get_url(self.get_previous_link())
            previous_url = self.url + temporal_url
        return Response(collections.OrderedDict([
             ('count', self.page.paginator.count),
             ('countItemsOnPage', self.page_size),
             ('current', self.page.number),
             ('next', next_url),
             ('previous', previous_url),
             ('results', data)
         ]))
