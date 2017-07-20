#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division

__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope.component import queryAdapter
from zope.component import queryMultiAdapter

DEFAULT_FIELDS = [
    'tool_consumer_instance_guid',
    'tool_consumer_instance_url',
    'tool_consumer_instance_name',
    'oauth_consumer_key',
    'tool_consumer_info_product_family_code'
]


# TODO these methods can be combined
class LTIRequestFilter(object):

    @classmethod
    def user_adapter_filter(cls, request, user_interface, fields=DEFAULT_FIELDS):
        """
        Filters a launch request specific fields
        :param request: ILTIRequest
        :param user_interface: the interface being adapted
        :param fields: where to check for the adapter
        :return: adapter, or None if not found
        """

        params = request.params

        # Check the suspected locations
        for field in fields:
            try:
                adapter_name = params[field]
                adapter = queryAdapter(request,
                                       user_interface,
                                       name=adapter_name)
                if adapter:
                    return adapter
            except KeyError:
                logger.exception('No key in field %s', field)

        return None

    @classmethod
    def mapping_adapter_filter(cls, request, factory, map_interface, fields=DEFAULT_FIELDS):
        """
        Filters a launch request specific fields
        :param request: ILTIRequest
        :param factory: package specific factory
        :param map_interface: the interface being adapted
        :param fields: where to check for the adapter
        :return: adapter, or None if not found
        """

        params = request.params

        # Check the suspected locations
        for field in fields:
            try:
                adapter_name = params[field]
                adapter = queryMultiAdapter((request, factory),
                                            map_interface,
                                            name=adapter_name)
                if adapter:
                    return adapter
            except KeyError:
                logger.exception('No key in field %s', field)

        return None
