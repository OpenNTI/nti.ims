#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Defines QTI item elements

.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface

from nti.schema.fieldproperty import createFieldProperties

from ..basic.elements import QTI
from ..basic.elements import QTIElement
from . import interfaces as itms_interfaces

@QTI
@interface.implementer(itms_interfaces.IitemSessionControl)
class ItemSessionControl(QTIElement):
	createFieldProperties(itms_interfaces.IitemSessionControl)

@QTI
@interface.implementer(itms_interfaces.IassessmentItem)
class AssessmentItem(QTIElement):
	createFieldProperties(itms_interfaces.IassessmentItem)
