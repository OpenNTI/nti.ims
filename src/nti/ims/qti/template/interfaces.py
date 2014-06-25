#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Defines QTI template interfaces

.. $Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

from nti.schema.field import List
from nti.schema.field import Object

from zope.interface.common.sequence import IFiniteSequence

from .. import interfaces as qti_interfaces

from ..basic import interfaces as basic_interfaces
from ..content import interfaces as cnt_interfaces
from ..variables import interfaces as var_interfaces
from ..expression import interfaces as exp_interfaces
from ..attributes import interfaces as attr_interfaces
	
class ItemplateDeclaration(var_interfaces.IvariableDeclaration,
						   attr_interfaces.ItemplateDeclarationAttrGroup,
						   qti_interfaces.IConcrete):
	pass

class ItemplateElement(basic_interfaces.IbodyElement,
					   attr_interfaces.ItemplateElementAttrGroup):
	pass

class ItemplateBlock(cnt_interfaces.IblockStatic,
					 cnt_interfaces.IflowStatic,
					 ItemplateElement,
					 IFiniteSequence,
					 qti_interfaces.IConcrete):

	blockStatic = List(Object(cnt_interfaces.IblockStatic),
					   title="The ordered list of blockStatic elements",
					   min_length=0)

class ItemplateInline(cnt_interfaces.IflowStatic,
					  cnt_interfaces.IinlineStatic,
					  ItemplateElement,
					  IFiniteSequence,
					  qti_interfaces.IConcrete):

	inlineStatic = List(Object(cnt_interfaces.IinlineStatic),
						title="The ordered list of inlineStatic elements",
						min_length=0)

class IintegerOrVariableRef(qti_interfaces.IConcrete):
	pass
	
class IfloatOrVariableRef(qti_interfaces.IConcrete):
	pass
	
class IstringOrVariableRef(qti_interfaces.IConcrete):
	pass
	
class ItemplateRule(qti_interfaces.IQTIElement):
	pass
	
class ItemplateProcessing(qti_interfaces.IConcrete):
	templateRule = List(Object(ItemplateRule),
						title="The ordered list of templateRule elements",
						min_length=1)

class ItemplateConstraint(ItemplateRule, IFiniteSequence, qti_interfaces.IConcrete):

	expression = List(Object(exp_interfaces.Iexpression),
					  title="The expressions",
					  min_length=0)

class ItemplateIf(qti_interfaces.IConcrete):
	expression = Object(exp_interfaces.Iexpression,
						title="The expression",
						required=True)
	
	templateRule = List(Object(ItemplateRule),
						title="The ordered list of templateRule elements",
						min_length=0)

class ItemplateElseIf(qti_interfaces.IConcrete):

	expression = Object(exp_interfaces.Iexpression,
						title="The expression",
						required=True)

	templateRule = List(Object(ItemplateRule),
						title="The ordered list of templateRule elements",
						min_length=0)
	
class ItemplateElse(qti_interfaces.IConcrete):
	
	templateRule = List(Object(ItemplateRule),
						title="The ordered list of templateRule elements",
						min_length=0)

class ItemplateCondition(ItemplateRule, qti_interfaces.IConcrete):

	templateIf = Object(ItemplateIf,
						title='The templateIf',
						required=True)

	templateElseIf = List(Object(ItemplateElseIf),
						  title='The order list of templateIf elements',
						  min_length=0)

	templateElse = Object(ItemplateElse,
						  title='The templateElse elements',
						  required=False)
	
class IsetTemplateValue(ItemplateRule,
						attr_interfaces.IsetTemplateValueAttrGroup,
						qti_interfaces.IConcrete):

	expression = Object(exp_interfaces.Iexpression,
						title="The expression",
						required=True)
	
class IsetCorrectResponse(ItemplateRule,
						  attr_interfaces.IsetCorrectResponseAttrGroup,
						  qti_interfaces.IConcrete):

	expression = Object(exp_interfaces.Iexpression,
						title="The expression",
						required=True)

class IsetDefaultValue(ItemplateRule,
					   attr_interfaces.IsetDefaultValueAttrGroup,
					   qti_interfaces.IConcrete):

	expression = Object(exp_interfaces.Iexpression,
						title="The expression",
						required=True)

class IexitTemplate(ItemplateRule, qti_interfaces.IConcrete):
	pass
