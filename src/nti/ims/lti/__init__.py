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


def adapt_accounting_for_consumer(request,
                                  interface,
                                  multi=False,
                                  query=True,
                                  fields=DEFAULT_FIELDS):

    params = request.params

    foo = queryAdapter if query else getAdapter

    if isinstance(request, tuple) or multi:
        foo = queryMultiAdapter if query else getMultiAdapter

    # Check the suspected locations
    for field in fields:
        try:
            adapter_name = params[field]
            adapter = foo(request,
                          interface,
                          name=adapter_name)
            if adapter:
                return adapter
        except KeyError:
            logger.exception('No key in field %s', field)

    return None
