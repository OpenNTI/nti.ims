#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Defines QTI feedback interfaces

.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

from zope.interface.common.sequence import IFiniteSequence

from nti.schema.field import List
from nti.schema.field import Object

from ..interfaces import IConcrete

from ..content.interfaces import IflowStatic
from ..attributes.interfaces import ItestFeedbackAttrGroup
from ..attributes.interfaces import IImodalFeedbackAttrGroup

class ImodalFeedback(IImodalFeedbackAttrGroup,
					 IFiniteSequence,
					 IConcrete):

	flowStatic = List(Object(IflowStatic),
					  title="An ordered list of values",
					  min_length=0)

class ItestFeedback(ItestFeedbackAttrGroup,
					IFiniteSequence,
					IConcrete):

	flowStatic = List(Object(IflowStatic),
					  title="An optional ordered set of conditions evaluated during the test",
					  min_length=0)
