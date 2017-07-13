#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import component
from zope import interface

from nti.ims.lti.interfaces import IOAuthConsumer
from nti.ims.lti.interfaces import IOAuthConsumers

from nti.schema.field import SchemaConfigured

from nti.schema.fieldproperty import createDirectFieldProperties

from nti.site.utils import registerUtility
from nti.site.utils import unregisterUtility


@interface.implementer(IOAuthConsumer)
class OAuthConsumer(SchemaConfigured):
    createDirectFieldProperties(IOAuthConsumer)


@interface.implementer(IOAuthConsumers)
class UtilityBackedOAuthConsumers(object):

    def __getitem__(self, key):
        consumer = component.queryUtility(IOAuthConsumer, name=key)
        if consumer is None:
            raise KeyError(key)
        return consumer

    def __setitem__(self, key, consumer):
        if consumer.key != key:
            raise ValueError('consumer must be stored by key')
        try:
            del self[key]
        except KeyError:
            pass
        registerUtility(component.getSiteManager(),
                        consumer, IOAuthConsumer, name=key)

    def __delitem__(self, key):
        consumer = self[key]
        unregisterUtility(component.getSiteManager(),
                          consumer, IOAuthConsumer, name=key)
