#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)


from zope.component import getAdapter
from zope.component import getMultiAdapter
from zope.component import queryAdapter
from zope.component import queryMultiAdapter

DEFAULT_FIELDS = [
    'tool_consumer_instance_guid',
    'tool_consumer_instance_url',
    'tool_consumer_instance_name',
    'oauth_consumer_key',
    'tool_consumer_info_product_family_code'
]


"""
Filter Strategy interface

must provide params to for matching
must provide fields to search through
must provide a value field to return

filter_request will provide the current field and field value in the request
"""


# A really fancy for loop
def filter_request(filter_strategy, raise_key_error=True):
    """
    :param filter_strategy: A strategy for what to do with the fields of a launch request
    :param raise_key_error: boolean
    """

    params = filter_strategy.params

    fields = filter_strategy.fields

    for field in fields:
        try:
            field_value = params[field]
            filter_strategy(field, field_value)
        except KeyError:
            if raise_key_error:
                raise KeyError
            logger.exception("No value for field %s", field)

    return filter_strategy.value


class AdaptAccountingForConsumer:
    """
    A launch request filter strategy for finding an adapter for a specific consumer
    """

    def __init__(self,
                 request,
                 interface,
                 multi=False,
                 query=True,
                 fields=DEFAULT_FIELDS):

        self.params = request.params
        self.value = None
        self.fields = fields
        self.interface = interface
        self.request = request
        self.foo = queryAdapter if query else getAdapter

        if isinstance(request, tuple) or multi:
            self.foo = queryMultiAdapter if query else getMultiAdapter

    def __call__(self, field, field_value):

        if self.value:
            return

        self.value = self.foo(self.request,
                              self.interface,
                              name=field_value)


class MapValuesToRequest:
    """
    A launch request strategy for mapping values to package specific fields
    """

    def __init__(self,
                 request,
                 mapping):

        self.params = request.params
        self.fields = mapping
        self.value = {}

    def __call__(self, field, field_value):
        self.value[self.fields[field]] = field_value


class GetMappingForConsumer:
    """
    A launch request strategy for getting a tool consumer name
    """

    def __init__(self, request, mapping, fields=DEFAULT_FIELDS):

        self.fields = fields
        self.params = request.params
        self.value = mapping

    def __call__(self, field, field_value):

        self.value.set_consumer_map(field)
