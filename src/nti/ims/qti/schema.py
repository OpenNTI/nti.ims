#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
QIT schema field types

.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

import re
import six
import numbers
from collections import Iterable

from zope import interface

from zope.schema import URI
from zope.schema.interfaces import WrongType
from zope.schema.interfaces import IFromUnicode
from zope.schema.interfaces import ConstraintNotSatisfied

from nti.schema.field import Int
from nti.schema.field import Bool
from nti.schema.field import List
from nti.schema.field import Float
from nti.schema.field import Choice
from nti.schema.field import ValidTextLine

from .interfaces import IQTIAttribute
			
@interface.implementer(IQTIAttribute)
class BaseQTIAttribute(object):
	
	def fromUnicode(self, value):
		result = super(BaseQTIAttribute, self).fromUnicode(value) if value else None
		return result
	
	def toUnicode(self, value):
		return unicode(value) if value is not None else None
	
class TextLineAttribute(BaseQTIAttribute, ValidTextLine):
	"""
	A :class:`TextLine` type that to mark XML attribute elements
	"""
	
class URIAttribute(BaseQTIAttribute, URI):
	"""
	A :class:`URI` type that to mark XML attribute elements
	"""

@interface.implementer(IFromUnicode)
class BoolAttribute(BaseQTIAttribute, Bool):
	"""
	A :class:`Bool` type that to mark XML attribute elements
	"""
	
class IntAttribute(BaseQTIAttribute, Int):
	"""
	A :class:`Int` type that to mark XML attribute elements
	"""

class FloatAttribute(BaseQTIAttribute, Float):
	"""
	A :class:`Float` type that to mark XML attribute elements
	"""

class ChoiceAttribute(BaseQTIAttribute, Choice):
	"""
	A :class:`Choice` type that to mark XML attribute elements
	"""
	
class MimeTypeAttribute(TextLineAttribute):
	"""
	A :class: for mimetype attributes
	"""

@interface.implementer(IFromUnicode)
class ListAttribute(BaseQTIAttribute, List):
	"""
	A :class:`List` type that to mark XML attribute elements
	"""
	
	pattern = re.compile("[^\s]+")
	
	def fromUnicode(self, value):
		result = []
		for p in self.pattern.findall(value or ''):
			result.append(self.value_type.fromUnicode(p))
		return result
	
	def toUnicode(self, value):
		if isinstance(value, six.string_types):
			result = unicode(value)
		elif isinstance(value, Iterable):
			if not IQTIAttribute.providedBy(self.value_type):
				func = unicode 
			else:
				func = self.value_type.toUnicode
			result = [func(x) for x in value]
			result = ' '.join(result)
		else:
			result = super(ListAttribute, self).toUnicode(value)
		return result
			
class IntegerOrVariableRefAttribute(TextLineAttribute):
	
	"""
	A :class: to mark XML an attribute element for either an Int or a variable ref (string)
	"""
	def _validate(self, value):
		if not (isinstance(value, six.string_types) or \
				isinstance(value, numbers.Integral)):
			raise WrongType(value)

		if not self.constraint(value):
			raise ConstraintNotSatisfied(value)
		
	def fromUnicode(self, value):
		result = super(IntegerOrVariableRefAttribute, self).fromUnicode(value)
		if result:
			try:
				result = int(result)
			except:
				result = unicode(result)
		return result
	
	def constraint(self, value):
		if isinstance(value, six.string_types):
			return '\n' not in value and '\r' not in value
		return isinstance(value, numbers.Integral)
	
class FloatOrVariableRefAttribute(TextLineAttribute):
	"""
	A :class: to mark XML attribute element for either a Float or a variable ref (string)
	"""
	def _validate(self, value):
		if not (isinstance(value, six.string_types) or \
				isinstance(value, (numbers.Integral, numbers.Real))):
			raise WrongType(value)

		if not self.constraint(value):
			raise ConstraintNotSatisfied(value)
		
	def fromUnicode(self, value):
		result = super(FloatOrVariableRefAttribute, self).fromUnicode(value)
		if result:
			try:
				result = float(result)
			except:
				result = unicode(result)
		return result
	
	def constraint(self, value):
		if isinstance(value, six.string_types):
			return '\n' not in value and '\r' not in value
		return isinstance(value, (numbers.Integral, numbers.Real))
	
class StringOrVariableRefAttribute(TextLineAttribute):
	pass

class IdentifierRefAttribute(TextLineAttribute):
	pass
