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

from nti.ims import MessageFactory as _

DEFAULT_FIELDS = [
    'tool_consumer_instance_guid',
    'tool_consumer_instance_url',
    'tool_consumer_instance_name',
    'oauth_consumer_key',
    'tool_consumer_info_product_family_code'
]


def adapt_accounting_for_consumer(request,
                                  adaptee,
                                  interface,
                                  multi=False,
                                  query=True,
                                  fields=DEFAULT_FIELDS):

    params = request.params

    query_type = queryAdapter if query else getAdapter
    if isinstance(request, tuple) or multi:
        query_type = queryMultiAdapter if query else getMultiAdapter

    for field in fields:
        try:
            field_value = params[field]
            adapter = query_type(adaptee, interface, field_value)
            if adapter is not None:
                return adapter
        except KeyError:
            msg = _('No value for field %s', field)
            logger.exception(msg)

    return None

