# -*- coding: utf-8 -*-
"""
Defines QTI response interfaces

.. $Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

from nti.schema.field import List
from nti.schema.field import Object

from zope.interface.common.sequence import IFiniteSequence

from .. import interfaces as qti_interfaces

from ..outcome import interfaces as out_interfaces
from ..expression import interfaces as exp_interfaces
from ..attributes import interfaces as attr_interfaces

# generalized response processing

class IresponseRule(qti_interfaces.IQTIElement):
	pass
	
class IresponseProcessing(attr_interfaces.IresponseProcessingAttrGroup,
						  IFiniteSequence,
						  qti_interfaces.IConcrete):

	responseRule = List(Object(IresponseRule),
						title="An ordered list of values",
						min_length=1)

class IresponseIf(qti_interfaces.IConcrete):
	
	expression = Object(exp_interfaces.Iexpression,
						title='The expression',
						required=True)

	responseRule = List(Object(IresponseRule),
						title='The ordered response rules',
						required=False,
						min_length=0)

class IresponseElseIf(qti_interfaces.IConcrete):
	
	expression = Object(exp_interfaces.Iexpression,
						title='The expression',
						required=True)

	responseRule = List(Object(IresponseRule),
						title='The ordered response rules',
						required=False,
						min_length=0)

class IresponseElse(qti_interfaces.IConcrete):
	
	responseRule = List(Object(IresponseRule),
						title='The ordered response rules',
						required=False,
						min_length=0)

class IresponseCondition(IresponseRule, qti_interfaces.IConcrete):

	responseIf = Object(IresponseIf,
						title='response if',
						required=True)

	responseElseIf = List(Object(IresponseElseIf),
						  title='response if list',
						  required=False,
						  min_length=0)

	responseElse = Object(IresponseElse, title='response else', required=False)

class IsetOutcomeValue(out_interfaces.IoutcomeRule,
					   IresponseRule,
					   attr_interfaces.IsetOutcomeValueAttrGroup,
					   qti_interfaces.IConcrete):

	expression = Object(exp_interfaces.Iexpression,
						title='The expression',
						required=True)

class IlookupOutcomeValue(out_interfaces.IoutcomeRule,
						  IresponseRule,
						  attr_interfaces.IlookupOutcomeValueAttrGroup,
						  qti_interfaces.IConcrete):

	expression = Object(exp_interfaces.Iexpression,
						title='A single cardinality expression',
						required=True)
	
class IexitResponse(IresponseRule, qti_interfaces.IConcrete):
	pass

