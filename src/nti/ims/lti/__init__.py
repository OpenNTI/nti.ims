#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from zope.component import getAdapter
from zope.component import queryAdapter
from zope.component import getMultiAdapter
from zope.component import queryMultiAdapter
from zope.component import ComponentLookupError

DEFAULT_FIELDS = (
    'tool_consumer_instance_guid',
    'tool_consumer_instance_url',
    'tool_consumer_instance_name',
    'oauth_consumer_key',
    'tool_consumer_info_product_family_code'
)

# XXX: Make sure these strings are unicode type as they later are used in schema validation
SUPPORTED_LTI_EXTENSIONS = {u'canvas.instructure.com': [u'link_selection',
                                                        u'resource_selection',
                                                        u'assignment_selection',
                                                        u'editor_button',
                                                        u'homework_submission',
                                                        u'migration_selection'],
                            u'nextthought.com': []}

logger = __import__('logging').getLogger(__name__)


def adapt_accounting_for_consumer(request,
                                  adaptee,
                                  interface,
                                  multi_adapter_for_tuple=True,
                                  query=True,
                                  fields=DEFAULT_FIELDS):

    params = request.params

    query_type = queryAdapter if query else getAdapter
    if isinstance(adaptee, tuple) and multi_adapter_for_tuple:
        query_type = queryMultiAdapter if query else getMultiAdapter

    for field in fields or ():
        try:
            field_value = params[field]
            adapter = query_type(adaptee, interface, name=field_value)
            if adapter is not None:
                return adapter
        except (KeyError, ComponentLookupError) as e:
            logger.error("malformed requests? %s", e)

    return query_type(adaptee, interface, name="default")
