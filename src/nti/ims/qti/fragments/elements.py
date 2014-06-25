#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Defines QTI fragment elements

.. $Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface

from nti.schema.fieldproperty import createFieldProperties

from ..basic.elements import QTI
from ..basic.elements import QTIElement
from . import interfaces as frg_interfaces

@QTI
@interface.implementer(frg_interfaces.Iinclude)
class Include(QTIElement):
	createFieldProperties(frg_interfaces.Iinclude)

@QTI
@interface.implementer(frg_interfaces.IresponseProcessingFragment)
class ResponseProcessingFragment(QTIElement):
	createFieldProperties(frg_interfaces.IresponseProcessingFragment)

@QTI
@interface.implementer(frg_interfaces.IoutcomeProcessingFragment)
class OutcomeProcessingFragment(QTIElement):
	createFieldProperties(frg_interfaces.IoutcomeProcessingFragment)
