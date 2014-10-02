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

from .interfaces import Iweight
from .interfaces import ItestPart
from .interfaces import Iordering
from .interfaces import Iselection
from .interfaces import ItimeLimits
from .interfaces import IassessmentTest
from .interfaces import IvariableMapping
from .interfaces import ItemplateDefault
from .interfaces import IassessmentSection
from .interfaces import IassessmentItemRef
from .interfaces import IassessmentSectionRef

@QTI
@interface.implementer(Iselection)
class Selection(QTIElement):
	createFieldProperties(Iselection)
	
@QTI
@interface.implementer(Iordering)
class Ordering(QTIElement):
	createFieldProperties(Iordering)

@QTI
@interface.implementer(ItimeLimits)
class TimeLimits(QTIElement):
	createFieldProperties(ItimeLimits)

@QTI
@interface.implementer(IvariableMapping)
class VariableMapping(QTIElement):
	createFieldProperties(IvariableMapping)

@QTI
@interface.implementer(ItemplateDefault)
class TemplateDefault(QTIElement):
	createFieldProperties(ItemplateDefault)

@QTI
@interface.implementer(Iweight)
class Weight(QTIElement):
	createFieldProperties(Iweight)

@QTI
@interface.implementer(IassessmentSection)
class AssessmentSection(QTIElement):
	createFieldProperties(IassessmentSection)

@QTI
@interface.implementer(IassessmentSectionRef)
class AssessmentSectionRef(QTIElement):
	createFieldProperties(IassessmentSectionRef)

@QTI
@interface.implementer(IassessmentItemRef)
class AssessmentItemRef(QTIElement):
	createFieldProperties(IassessmentItemRef)
	
@QTI
@interface.implementer(ItestPart)
class TestPart(QTIElement):
	createFieldProperties(ItestPart)

@QTI
@interface.implementer(IassessmentTest)
class AssessmentTest(QTIElement):
	createFieldProperties(IassessmentTest)
