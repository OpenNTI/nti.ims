# -*- coding: utf-8 -*-
"""
.. $Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface

from nti.schema.field import SchemaConfigured
from nti.schema.fieldproperty import createFieldProperties

from ..basic.elements import QTIElement

from . import interfaces as ast_interfaces

@interface.implementer(ast_interfaces.Iselection)
class Selection(SchemaConfigured, QTIElement):
	createFieldProperties(ast_interfaces.Iselection)
	
@interface.implementer(ast_interfaces.Iordering)
class Ordering(SchemaConfigured, QTIElement):
	createFieldProperties(ast_interfaces.Iordering)

@interface.implementer(ast_interfaces.ItimeLimits)
class TimeLimits(SchemaConfigured, QTIElement):
	createFieldProperties(ast_interfaces.ItimeLimits)

@interface.implementer(ast_interfaces.IvariableMapping)
class VariableMapping(SchemaConfigured, QTIElement):
	createFieldProperties(ast_interfaces.IvariableMapping)

@interface.implementer(ast_interfaces.ItemplateDefault)
class TemplateDefault(SchemaConfigured, QTIElement):
	createFieldProperties(ast_interfaces.ItemplateDefault)

@interface.implementer(ast_interfaces.Iweight)
class Weight(SchemaConfigured, QTIElement):
	createFieldProperties(ast_interfaces.Iweight)

@interface.implementer(ast_interfaces.IassessmentSection)
class AssessmentSection(SchemaConfigured, QTIElement):
	createFieldProperties(ast_interfaces.IassessmentSection)

@interface.implementer(ast_interfaces.IassessmentSectionRef)
class AssessmentSectionRef(SchemaConfigured, QTIElement):
	createFieldProperties(ast_interfaces.IassessmentSectionRef)

@interface.implementer(ast_interfaces.IassessmentItemRef)
class AssessmentItemRef(SchemaConfigured, QTIElement):
	createFieldProperties(ast_interfaces.IassessmentItemRef)
	
@interface.implementer(ast_interfaces.ItestPart)
class TestPart(SchemaConfigured, QTIElement):
	createFieldProperties(ast_interfaces.ItestPart)

@interface.implementer(ast_interfaces.IassessmentTest)
class AssessmentTest(SchemaConfigured, QTIElement):
	createFieldProperties(ast_interfaces.IassessmentTest)
