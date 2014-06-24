# -*- coding: utf-8 -*-
"""
Defines QTI outcome interfaces

.. $Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

from nti.schema.field import List
from nti.schema.field import Object

from zope.interface.common.sequence import IFiniteSequence

from .. import interfaces as qti_interfaces

from ..expression import interfaces as exp_interfaces

class IoutcomeRule(qti_interfaces.IQTIElement):
	pass
	
class IoutcomeProcessing(IFiniteSequence, qti_interfaces.IConcrete):

	IoutcomeRule = List(Object(IoutcomeRule),
						title="Order list of outcome rules",
						min_length=0)
	
class IoutcomeIf(qti_interfaces.IConcrete):

	expression = Object(exp_interfaces.Iexpression,
						title='The expression',
						required=True)

	outcomeRule = List(Object(IoutcomeRule),
					   title='The ordered outcome rules',
					   required=False,
					   min_length=0)
	
class IoutcomeElseIf(qti_interfaces.IConcrete):
	expression = Object(exp_interfaces.Iexpression,
						title='The expression',
						required=True)

	outcomeRule = List(Object(IoutcomeRule),
					   title='The ordered outcome rules',
					   required=False,
					   min_length=0)
	
class IoutcomeElse(qti_interfaces.IConcrete):
	outcomeRule = List(Object(IoutcomeRule),
					   title='The ordered outcome rules',
					   required=False,
					   min_length=0)
	
class IoutcomeCondition(IoutcomeRule, qti_interfaces.IConcrete):
	
	outcomeIf = Object(IoutcomeIf, title='outcome if', required=True)

	outcomeElseIf = List(Object(IoutcomeElseIf),
						 title='outcome if list',
						 required=False,
						 min_length=0)

	outcomeElse = Object(IoutcomeElse,
						 title='outcome else',
						 required=False)
	
class IexitTest(IoutcomeRule, qti_interfaces.IConcrete):
	pass

