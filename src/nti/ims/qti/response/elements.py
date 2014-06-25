# -*- coding: utf-8 -*-
"""
Defines QTI response elements

.. $Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface

from nti.schema.fieldproperty import createFieldProperties

from ..basic.elements import QTI
from ..basic.elements import QTIElement
from . import interfaces as rsp_interfaces

@QTI
@interface.implementer(rsp_interfaces.IresponseProcessing)
class ResponseProcessing(QTIElement):
	createFieldProperties(rsp_interfaces.IresponseProcessing)

@QTI
@interface.implementer(rsp_interfaces.IresponseIf)
class ResponseIf(QTIElement):
	createFieldProperties(rsp_interfaces.IresponseIf)

@QTI
@interface.implementer(rsp_interfaces.IresponseElseIf)
class ResponseElseIf(QTIElement):
	createFieldProperties(rsp_interfaces.IresponseElseIf)

@QTI
@interface.implementer(rsp_interfaces.IresponseElse)
class ResponseElse(QTIElement):
	createFieldProperties(rsp_interfaces.IresponseElse)

@QTI
@interface.implementer(rsp_interfaces.IresponseCondition)
class ResponseCondition(QTIElement):
	createFieldProperties(rsp_interfaces.IresponseCondition)

@QTI
@interface.implementer(rsp_interfaces.IsetOutcomeValue)
class SetOutcomeValue(QTIElement):
	createFieldProperties(rsp_interfaces.IsetOutcomeValue)

@QTI
@interface.implementer(rsp_interfaces.IlookupOutcomeValue)
class LookupOutcomeValue(QTIElement):
	createFieldProperties(rsp_interfaces.IlookupOutcomeValue)

@QTI
@interface.implementer(rsp_interfaces.IexitResponse)
class ExitResponse(QTIElement):
	createFieldProperties(rsp_interfaces.IexitResponse)
