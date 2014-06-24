# -*- coding: utf-8 -*-
"""
Defines QTI precondition elements

.. $Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface

from nti.schema.fieldproperty import createFieldProperties

from ..basic.elements import QTIElement
from . import interfaces as pre_interfaces

@interface.implementer(pre_interfaces.IpreCondition)
class PreCondition(QTIElement):
	createFieldProperties(pre_interfaces.IpreCondition)

@interface.implementer(pre_interfaces.IbranchRule)
class BranchRule(QTIElement):
	createFieldProperties(pre_interfaces.IbranchRule)
