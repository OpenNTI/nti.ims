#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division

__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

DEFAULT_FIELDS = [
    'tool_consumer_instance_guid',
    'tool_consumer_instance_url',
    'tool_consumer_instance_name',
    'oauth_consumer_key',
    'tool_consumer_info_product_family_code'
]


class LaunchRequestFieldFilter(object):

    def filter(self, request, value=None, fields=None):
        """
        Filters a launch request specific fields
        :param request: ILTIRequest
        :param value: the term being searched for
        :param fields: where to check for the value
        :return: the field name where the value is contained, or None if not found
        """

        if not fields:
            fields = DEFAULT_FIELDS

        params = request.params

        for field in fields:
            if params[field] == value:
                return field
        return None
