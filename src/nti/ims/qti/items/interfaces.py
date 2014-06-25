#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Defines QTI items interfaces

.. $Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

from nti.schema.field import List
from nti.schema.field import Object

from .. import interfaces as qti_interfaces

from ..content import interfaces as cnt_interfaces
from ..response import interfaces as rsp_interfaces
from ..template import interfaces as tmp_interfaces
from ..feedback import interfaces as feed_interfaces
from ..variables import interfaces as var_interfaces
from ..attributes import interfaces as attr_interfaces

class IitemSessionControl(attr_interfaces.IitemSessionControlAttrGroup,
						  qti_interfaces.IConcrete):
	pass

class IassessmentItem(attr_interfaces.IassessmentItemAttrGroup,
					  qti_interfaces.IConcrete):

	responseDeclaration = List(Object(var_interfaces.IresponseDeclaration),
							   min_length=0,
							   required=True)

	outcomeDeclaration = List(Object(var_interfaces.IoutcomeDeclaration),
							  min_length=0,
							  required=True)

	templateDeclaration = List(Object(tmp_interfaces.ItemplateDeclaration),
							   min_length=0,
							   required=True)

	templateProcessing = Object(tmp_interfaces.ItemplateProcessing,
								required=False)

	stylesheet = List(Object(cnt_interfaces.Istylesheet),
					  min_length=0,
					  title='Ordered list',
					  required=False)

	itemBody = Object(cnt_interfaces.IitemBody, required=False)

	responseProcessing = Object(rsp_interfaces.IresponseProcessing,
								required=False)

	modalFeedback = List(Object(feed_interfaces.ImodalFeedback),
						 min_length=0,
						 title='Ordered list',
						 required=False)
