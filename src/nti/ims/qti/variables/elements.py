#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Defines QTI variable elements

.. $Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface

from nti.schema.fieldproperty import createFieldProperties

from ..basic.elements import QTI
from ..basic.elements import QTIElement
from . import interfaces as var_interfaces

@QTI
@interface.implementer(var_interfaces.Ivalue)
class Value(QTIElement):
	createFieldProperties(var_interfaces.Ivalue)

@QTI
@interface.implementer(var_interfaces.IdefaultValue)
class DefaultValue(QTIElement):
	createFieldProperties(var_interfaces.IdefaultValue)

@QTI
@interface.implementer(var_interfaces.ImapEntry)
class MapEntry(QTIElement):
	createFieldProperties(var_interfaces.ImapEntry)

@QTI
@interface.implementer(var_interfaces.Imapping)
class Mapping(QTIElement):
	createFieldProperties(var_interfaces.Imapping)

@QTI
@interface.implementer(var_interfaces.IareaMapEntry)
class AreaMapEntry(QTIElement):
	createFieldProperties(var_interfaces.IareaMapEntry)

@QTI
@interface.implementer(var_interfaces.IareaMapping)
class AreaMapping(QTIElement):
	createFieldProperties(var_interfaces.IareaMapping)

@QTI
@interface.implementer(var_interfaces.IcorrectResponse)
class CorrectResponse(QTIElement):
	createFieldProperties(var_interfaces.IcorrectResponse)

@QTI
@interface.implementer(var_interfaces.IresponseDeclaration)
class ResponseDeclaration(QTIElement):
	createFieldProperties(var_interfaces.IresponseDeclaration)
	
@QTI
@interface.implementer(var_interfaces.ImatchTableEntry)
class MatchTableEntry(QTIElement):
	createFieldProperties(var_interfaces.ImatchTableEntry)

@QTI
@interface.implementer(var_interfaces.ImatchTable)
class MatchTable(QTIElement):
	createFieldProperties(var_interfaces.ImatchTable)
	
@QTI
@interface.implementer(var_interfaces.IinterpolationTableEntry)
class InterpolationTableEntry(QTIElement):
	createFieldProperties(var_interfaces.IinterpolationTableEntry)
	
@QTI
@interface.implementer(var_interfaces.IinterpolationTable)
class InterpolationTable(QTIElement):
	createFieldProperties(var_interfaces.IinterpolationTable)
	
@QTI
@interface.implementer(var_interfaces.IoutcomeDeclaration)
class OutcomeDeclaration(QTIElement):
	createFieldProperties(var_interfaces.IoutcomeDeclaration)
