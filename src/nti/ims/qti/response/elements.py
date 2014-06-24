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

from ..basic.elements import QTIElement
from . import interfaces as rsp_interfaces

@interface.implementer(rsp_interfaces.IresponseProcessing)
class ResponseProcessing(QTIElement):
	createFieldProperties(rsp_interfaces.IresponseProcessing)

@interface.implementer(rsp_interfaces.IresponseIf)
class ResponseIf(QTIElement):
	createFieldProperties(rsp_interfaces.IresponseIf)

@interface.implementer(rsp_interfaces.IresponseElseIf)
class ResponseElseIf(QTIElement):
	createFieldProperties(rsp_interfaces.IresponseElseIf)

@interface.implementer(rsp_interfaces.IresponseElse)
class ResponseElse(QTIElement):
	createFieldProperties(rsp_interfaces.IresponseElse)

@interface.implementer(rsp_interfaces.IresponseCondition)
class ResponseCondition(QTIElement):
	createFieldProperties(rsp_interfaces.IresponseCondition)

@interface.implementer(rsp_interfaces.IsetOutcomeValue)
class SetOutcomeValue(QTIElement):
	createFieldProperties(rsp_interfaces.IsetOutcomeValue)

@interface.implementer(rsp_interfaces.IlookupOutcomeValue)
class LookupOutcomeValue(QTIElement):
	createFieldProperties(rsp_interfaces.IlookupOutcomeValue)

@interface.implementer(rsp_interfaces.IexitResponse)
class ExitResponse(QTIElement):
	createFieldProperties(rsp_interfaces.IexitResponse)
