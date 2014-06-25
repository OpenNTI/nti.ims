#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface

from nti.schema.fieldproperty import createFieldProperties

from ..basic.elements import QTI
from ..basic.elements import QTIElement

from . import interfaces as ast_interfaces

@QTI
@interface.implementer(ast_interfaces.Iselection)
class Selection(QTIElement):
	createFieldProperties(ast_interfaces.Iselection)
	
@QTI
@interface.implementer(ast_interfaces.Iordering)
class Ordering(QTIElement):
	createFieldProperties(ast_interfaces.Iordering)

@QTI
@interface.implementer(ast_interfaces.ItimeLimits)
class TimeLimits(QTIElement):
	createFieldProperties(ast_interfaces.ItimeLimits)

@QTI
@interface.implementer(ast_interfaces.IvariableMapping)
class VariableMapping(QTIElement):
	createFieldProperties(ast_interfaces.IvariableMapping)

@QTI
@interface.implementer(ast_interfaces.ItemplateDefault)
class TemplateDefault(QTIElement):
	createFieldProperties(ast_interfaces.ItemplateDefault)

@QTI
@interface.implementer(ast_interfaces.Iweight)
class Weight(QTIElement):
	createFieldProperties(ast_interfaces.Iweight)

@QTI
@interface.implementer(ast_interfaces.IassessmentSection)
class AssessmentSection(QTIElement):
	createFieldProperties(ast_interfaces.IassessmentSection)

@QTI
@interface.implementer(ast_interfaces.IassessmentSectionRef)
class AssessmentSectionRef(QTIElement):
	createFieldProperties(ast_interfaces.IassessmentSectionRef)

@QTI
@interface.implementer(ast_interfaces.IassessmentItemRef)
class AssessmentItemRef(QTIElement):
	createFieldProperties(ast_interfaces.IassessmentItemRef)
	
@QTI
@interface.implementer(ast_interfaces.ItestPart)
class TestPart(QTIElement):
	createFieldProperties(ast_interfaces.ItestPart)

@QTI
@interface.implementer(ast_interfaces.IassessmentTest)
class AssessmentTest(QTIElement):
	createFieldProperties(ast_interfaces.IassessmentTest)
