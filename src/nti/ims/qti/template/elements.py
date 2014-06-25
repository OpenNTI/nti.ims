#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Defines QTI template element

.. $Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface

from nti.schema.fieldproperty import createFieldProperties

from ..basic.elements import QTI
from ..basic.elements import QTIElement
from . import interfaces as tmp_interfaces

@QTI
@interface.implementer(tmp_interfaces.ItemplateDeclaration)
class TemplateDeclaration(QTIElement):
	createFieldProperties(tmp_interfaces.ItemplateDeclaration)

@QTI
@interface.implementer(tmp_interfaces.ItemplateBlock)
class TemplateBlock(QTIElement):
	createFieldProperties(tmp_interfaces.ItemplateBlock)

@QTI
@interface.implementer(tmp_interfaces.ItemplateInline)
class TemplateInline(QTIElement):
	createFieldProperties(tmp_interfaces.ItemplateInline)

@QTI
@interface.implementer(tmp_interfaces.IintegerOrVariableRef)
class IntegerOrVariableRef(QTIElement):
	createFieldProperties(tmp_interfaces.IintegerOrVariableRef)

@QTI
@interface.implementer(tmp_interfaces.IfloatOrVariableRef)
class FloatOrVariableRef(QTIElement):
	createFieldProperties(tmp_interfaces.IfloatOrVariableRef)

@QTI
@interface.implementer(tmp_interfaces.IstringOrVariableRef)
class StringOrVariableRef(QTIElement):
	createFieldProperties(tmp_interfaces.IstringOrVariableRef)

@QTI
@interface.implementer(tmp_interfaces.ItemplateProcessing)
class TemplateProcessing(QTIElement):
	createFieldProperties(tmp_interfaces.ItemplateProcessing)

@QTI
@interface.implementer(tmp_interfaces.ItemplateConstraint)
class TemplateConstraint(QTIElement):
	createFieldProperties(tmp_interfaces.ItemplateConstraint)

@QTI
@interface.implementer(tmp_interfaces.ItemplateIf)
class TemplateIf(QTIElement):
	createFieldProperties(tmp_interfaces.ItemplateIf)
	
@QTI
@interface.implementer(tmp_interfaces.ItemplateElseIf)
class TemplateElseIf(QTIElement):
	createFieldProperties(tmp_interfaces.ItemplateElseIf)

@QTI
@interface.implementer(tmp_interfaces.ItemplateElse)
class TemplateElse(QTIElement):
	createFieldProperties(tmp_interfaces.ItemplateElse)

@QTI
@interface.implementer(tmp_interfaces.ItemplateCondition)
class TemplateCondition(QTIElement):
	createFieldProperties(tmp_interfaces.ItemplateCondition)

@QTI
@interface.implementer(tmp_interfaces.IsetTemplateValue)
class SetTemplateValue(QTIElement):
	createFieldProperties(tmp_interfaces.IsetTemplateValue)
	
@QTI
@interface.implementer(tmp_interfaces.IsetCorrectResponse)
class SetCorrectResponse(QTIElement):
	createFieldProperties(tmp_interfaces.IsetCorrectResponse)

@QTI
@interface.implementer(tmp_interfaces.IsetDefaultValue)
class SetDefaultValue(QTIElement):
	createFieldProperties(tmp_interfaces.IsetDefaultValue)

@QTI
@interface.implementer(tmp_interfaces.IexitTemplate)
class ExitTemplate(QTIElement):
	createFieldProperties(tmp_interfaces.IexitTemplate)
