#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Defines QTI outcome elements

.. $Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface

from nti.schema.fieldproperty import createFieldProperties

from ..basic.elements import QTI
from ..basic.elements import QTIElement
from . import interfaces as out_interfaces

@QTI
@interface.implementer(out_interfaces.IoutcomeProcessing)
class OutcomeProcessing(QTIElement):
	createFieldProperties(out_interfaces.IoutcomeProcessing)

@QTI
@interface.implementer(out_interfaces.IoutcomeIf)
class OutcomeIf(QTIElement):
	createFieldProperties(out_interfaces.IoutcomeIf)

@QTI
@interface.implementer(out_interfaces.IoutcomeElseIf)
class OutcomeElseIf(QTIElement):
	createFieldProperties(out_interfaces.IoutcomeElseIf)

@QTI
@interface.implementer(out_interfaces.IoutcomeElse)
class OutcomeElse(QTIElement):
	createFieldProperties(out_interfaces.IoutcomeElse)

@QTI
@interface.implementer(out_interfaces.IoutcomeCondition)
class OutcomeCondition(QTIElement):
	createFieldProperties(out_interfaces.IoutcomeCondition)

@QTI
@interface.implementer(out_interfaces.IexitTest)
class ExitTest(QTIElement):
	createFieldProperties(out_interfaces.IexitTest)
