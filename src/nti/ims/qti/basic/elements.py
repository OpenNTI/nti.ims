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

from nti.externalization.externalization import WithRepr

from nti.schema.field import SchemaConfigured

from ..schema import IQTIAttribute
from ..attributes import interfaces as attr_interfaces

from .. import interfaces as qti_interfaces

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
		
class QTIMetaType(type):

	def __new__(cls, name, bases, attrs):
		t = type.__new__(cls, name, bases, attrs)
		clazzname = getattr(cls, '__external_class_name__', name)
		t.mime_type = t.mimeType = 'application/vnd.nextthought.qti.%s' % clazzname.lower()
		t.parameters = dict()
		
		implemented = getattr(cls, '__implemented__', None)
		implemented = list(implemented.flattened()) if implemented else ()
		if not qti_interfaces.IConcrete in implemented:
			t.__external_can_create__ = False
			return t
		
		t.__external_can_create__ = True
		is_finite_sequence = False
	
		attributes = {}
		definitions = {}
	
		for base in implemented:
			if issubclass(base, IFiniteSequence):
				is_finite_sequence = True
	
			if 	issubclass(base, qti_interfaces.IQTIElement) or \
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
			_make_sequence(t, key)
			
		# volatile attributes
		setattr(t, '_v_attributes', attributes)
		setattr(t, '_v_definitions', definitions)
		setattr(t, "_v_is_finite_sequence", is_finite_sequence)
	
		# helper method
		setattr(t, "get_children", _get_children)
		setattr(t, "set_attribute", _set_attribute)
		setattr(t, "get_attributes", _get_attributes)
		
		return t

@WithRepr
@interface.implementer(qti_interfaces.IQTIElement)
class QTIElement(SchemaConfigured, zcontained.Contained):
	__metaclass__ = QTIMetaType

