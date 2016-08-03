#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface

from nti.common.representation import WithRepr

from nti.ims.lti.interfaces import IConsumer

from nti.schema.eqhash import EqHash

from nti.schema.fieldproperty import createDirectFieldProperties

from nti.schema.schema import SchemaConfigured

@WithRepr
@EqHash('key', 'secret')
@interface.implementer(IConsumer)
class Consumer(SchemaConfigured):
	createDirectFieldProperties(IConsumer)
