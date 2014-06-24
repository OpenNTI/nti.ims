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

from .. import interfaces as qti_interfaces

from ..content import interfaces as cnt_interfaces
from ..attributes import interfaces as attr_interfaces

class ImodalFeedback(attr_interfaces.IImodalFeedbackAttrGroup,
					 IFiniteSequence,
					 qti_interfaces.IConcrete):

	flowStatic = List(Object(cnt_interfaces.IflowStatic),
					  title="An ordered list of values",
					  min_length=0)

class ItestFeedback(attr_interfaces.ItestFeedbackAttrGroup,
					IFiniteSequence,
					qti_interfaces.IConcrete):

	flowStatic = List(Object(cnt_interfaces.IflowStatic),
					  title="An optional ordered set of conditions evaluated during the test",
					  min_length=0)
