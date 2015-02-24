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

from .interfaces import Iinclude
from .interfaces import IoutcomeProcessingFragment
from .interfaces import IresponseProcessingFragment

@QTI
@interface.implementer(Iinclude)
class Include(QTIElement):
	createFieldProperties(Iinclude)

@QTI
@interface.implementer(IresponseProcessingFragment)
class ResponseProcessingFragment(QTIElement):
	createFieldProperties(IresponseProcessingFragment)

@QTI
@interface.implementer(IoutcomeProcessingFragment)
class OutcomeProcessingFragment(QTIElement):
	createFieldProperties(IoutcomeProcessingFragment)
