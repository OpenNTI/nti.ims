#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import schema
from zope import interface
from zope.container import contained as zcontained
from zope.interface.common.sequence import IFiniteSequence

from nti.common.representation import WithRepr

from nti.schema.field import SchemaConfigured

from ..schema import IQTIAttribute
from ..interfaces import IConcrete
from ..interfaces import IQTIElement
from ..attributes import interfaces as attr_interfaces

def get_schema_fields(iface):

	def _travel(iface, attributes):
		names = iface.names()
		fields = schema.getFields(iface) or {}
		for name in names or ():
			sch_def = fields.get(name, None)
			if sch_def:
				name = getattr(sch_def, '__name__', None) or name
				attributes[name] = sch_def

		for base in iface.getBases() or ():
			_travel(base, attributes)

	result = {}
	_travel(iface, result)
	return result

def _get_attributes(self):
	result = {}
	for k in self._v_attributes.keys():
		v = getattr(self, k, None)
		if v is not None:
			result[k] = v
	return result

def _set_attribute(self, key, value):
	if key in self._v_attributes:
		setattr(self, key, value)
		return True
	return False

def _get_children(self):
	if self._v_is_finite_sequence:
		result = [c for c in self if c is not None]
	else:
		result = {}
		for k in self._v_definitions.keys():
			v = getattr(self, k, None)
			if v is not None:
				result[k] = v
	return result

def _make_getitem(attr):
	def __getitem__(self, index):
		return getattr(self, attr)[index]
	return __getitem__

def _make_setitem(attr):
	def __setitem__(self, key, value):
		getattr(self, attr)[key] = value
	return __setitem__

def _make_iter(attr):
	def __iter__(self):
		return iter(getattr(self, attr))
	return __iter__

def _make_len(attr):
	def __len__(self):
		return len(getattr(self, attr))
	return __len__

def _make_append(attr):
	def append(self, obj):
		return getattr(self, attr).append(obj)
	return append

def _make_sequence(cls, attr):
	cls.__len__ = _make_len(attr)
	cls.__iter__ = _make_iter(attr)
	cls.__getitem__ = _make_getitem(attr)
	cls.__setitem__ = _make_setitem(attr)
	cls.append = _make_append(attr)
		
def QTI(cls):
	
	clazzname = getattr(cls, '__external_class_name__', cls.__name__)
	cls.mime_type = cls.mimeType = 'application/vnd.nextthought.qti.%s' % clazzname.lower()
	cls.parameters = dict()
	
	implemented = getattr(cls, '__implemented__', None)
	implemented = list(implemented.flattened()) if implemented else ()
	if IConcrete not in implemented:
		cls.__external_can_create__ = False
		return cls
	
	cls.__external_can_create__ = True
	is_finite_sequence = False

	attributes = {}
	definitions = {}

	for base in implemented:
		if issubclass(base, IFiniteSequence):
			is_finite_sequence = True

		if 	issubclass(base, IQTIElement) or \
			issubclass(base, attr_interfaces.IAttrGroup):
			r = get_schema_fields(base)
			for k, v in r.items():
				if IQTIAttribute.providedBy(v):
					attributes[k] = v
				else:
					definitions[k] = v

	is_finite_sequence = is_finite_sequence and len(definitions) == 1
	if is_finite_sequence:
		key =  list(definitions.keys())[0]
		_make_sequence(cls, key)
		
	# volatile attributes
	setattr(cls, '_v_attributes', attributes)
	setattr(cls, '_v_definitions', definitions)
	setattr(cls, "_v_is_finite_sequence", is_finite_sequence)

	# helper method
	setattr(cls, "get_children", _get_children)
	setattr(cls, "set_attribute", _set_attribute)
	setattr(cls, "get_attributes", _get_attributes)
	
	return cls

@WithRepr
@interface.implementer(IQTIElement)
class QTIElement(SchemaConfigured, zcontained.Contained):
	pass
