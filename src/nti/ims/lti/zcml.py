#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Directives to be used in ZCML: registering static keys.

.. $Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

import functools

from zope import interface
from zope.configuration import fields
from zope.component.zcml import utility

from .consumer import Consumer
from .interfaces import IConsumer

class IRegisterConsumer(interface.Interface):
	"""
	The arguments needed for registering consumer keys
	"""
	name = fields.TextLine(title="Consumer iden", required=False, default='')
	key = fields.TextLine(title="Consumer key", required=True)
	secret = fields.TextLine(title="Consumer secret", required=True)

def registerConsumer(_context, key, secret, name=u''):
	factory = functools.partial(Consumer, key=key, secret=secret)
	utility(_context, provides=IConsumer, factory=factory, name=name)
