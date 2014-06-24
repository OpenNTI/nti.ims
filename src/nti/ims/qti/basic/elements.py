# -*- coding: utf-8 -*-
"""
.. $Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface
from zope.container import contained as zcontained
from zope.annotation import interfaces as an_interfaces

from nti.externalization.externalization import WithRepr

from nti.schema.field import SchemaConfigured

@WithRepr
@interface.implementer(an_interfaces.IAttributeAnnotatable)
class QTIElement(SchemaConfigured, zcontained.Contained):
	
	_text = None
	_tail = None

	def get_text(self):
		return self._text

	def get_tail(self):
		return self._tail

	@property
	def content(self):
		result = self._text or u''
		result = result+self._tail if self._tail else result
		return result if result else None
