#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division

__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope.component import queryAdapter

DEFAULT_FIELDS = [
    'tool_consumer_instance_guid',
    'tool_consumer_instance_url',
    'tool_consumer_instance_name',
    'oauth_consumer_key',
    'tool_consumer_info_product_family_code'
]


class LaunchRequestFilter(object):

    @classmethod
    def filter_for_adapter(cls, request, interface, fields=DEFAULT_FIELDS):
        """
        Filters a launch request specific fields
        :param request: ILTIRequest
        :param interface: the interface being adapted
        :param fields: where to check for the value
        :return: the field name where the value is contained, or None if not found
        """

        params = request.params

        # Check the suspected locations
        for field in fields:
            try:
                adapter_name = params[field]
                adapter = queryAdapter(request,
                                       interface,
                                       name=adapter_name)
                if adapter:
                    return adapter
            except KeyError:
                logger.exception('No key in field %s', field)

        return None
