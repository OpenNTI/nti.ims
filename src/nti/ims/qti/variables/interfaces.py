# -*- coding: utf-8 -*-
"""
Defines QTI variables interfaces

.. $Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

from nti.schema.field import List
from nti.schema.field import Object

from zope.interface.common.sequence import IFiniteSequence

from .. import interfaces as qti_interfaces

from ..basic import interfaces as basic_interfaces
from ..attributes import interfaces as attr_interfaces

class Ivalue(attr_interfaces.IvalueAttrGroup, qti_interfaces.IConcrete):
	pass

class IdefaultValue(attr_interfaces.IdefaultValueAttrGroup,
					IFiniteSequence,
					qti_interfaces.IConcrete):

	value = List(Object(Ivalue), title="An ordered list of values", min_length=1)

class IvariableDeclaration(basic_interfaces.IbodyElement,
						   attr_interfaces.IvalueDeclarationAttrGroup):

	defaultValue = Object(IdefaultValue,
						  title="An optional default value for the variable",
						  required=False)

class ImapEntry(attr_interfaces.ImappingEntryAttrGroup, qti_interfaces.IConcrete):
	pass
	
class Imapping(attr_interfaces.ImappingAttrGroup,
			   IFiniteSequence,
			   qti_interfaces.IConcrete):

	mapEntry = List(Object(ImapEntry),
					title="The map is defined by a set of mapEntries",
					min_length=1)
	
# response variables

class IareaMapEntry(attr_interfaces.IareaMapEntryAttrGroup, qti_interfaces.IConcrete):
	pass
	
class IareaMapping(attr_interfaces.IareaMappingAttrGroup,
				   IFiniteSequence,
				   qti_interfaces.IConcrete):

	areaMapEntry = List(Object(IareaMapEntry),
						title="An ordered list of entries",
						min_length=1)
	
class IcorrectResponse(attr_interfaces.IcorrectResponseAttrGroup,
					   IFiniteSequence,
					   qti_interfaces.IConcrete):
	
	value = List(Object(Ivalue),
				 title="An ordered list of values",
				 min_length=1)

class IresponseDeclaration(IvariableDeclaration, qti_interfaces.IConcrete):

	correctResponse = Object(IcorrectResponse,
							title="May indicate the only possible value of the response variable",
							required=False)

	mapping = Object(Imapping,
					 title="Response mapping",
					 required=False)

	areaMapping = Object(IareaMapping,
						 title="Provides an alternative form of mapping",
						 required=False)
	
# outcome variables

class IlookupTable(attr_interfaces.IlookupTableAttrGroup):
	pass
	
class ImatchTableEntry(attr_interfaces.ImatchTableEntryAttrGroup,
					   qti_interfaces.IConcrete):
	pass
	
class ImatchTable(IlookupTable, IFiniteSequence, qti_interfaces.IConcrete):

	matchTableEntry = List(Object(ImatchTableEntry),
						   title="An ordered list of entries",
						   min_length=1)

class IinterpolationTableEntry(attr_interfaces.IinterpolationTableEntryAttrGroup,
							   qti_interfaces.IConcrete):
	pass
	
class IinterpolationTable(IlookupTable, IFiniteSequence, qti_interfaces.IConcrete):

	interpolationTableEntry = List(Object(IinterpolationTableEntry),
								   title="An ordered list of entries",
								   min_length=1)
	
class IoutcomeDeclaration(IvariableDeclaration,
						  IFiniteSequence,
						  attr_interfaces.IoutcomeDeclarationAttrGroup,
						  qti_interfaces.IConcrete):

	lookupTable = Object(IlookupTable, title="The lookup table", required=False)
	
