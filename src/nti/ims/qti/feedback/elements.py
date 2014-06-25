#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Defines QTI feedback elements

.. $Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface

from nti.schema.fieldproperty import createFieldProperties

from ..basic.elements import QTI
from ..basic.elements import QTIElement
from . import interfaces as fbk_interfaces

@QTI
@interface.implementer(fbk_interfaces.ImodalFeedback)
class ModalFeedback(QTIElement):
	createFieldProperties(fbk_interfaces.ImodalFeedback)

@QTI
@interface.implementer(fbk_interfaces.ItestFeedback)
class TestFeedback(QTIElement):
	createFieldProperties(fbk_interfaces.ItestFeedback)
