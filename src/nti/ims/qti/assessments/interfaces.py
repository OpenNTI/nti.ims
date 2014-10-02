#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

from nti.schema.field import Object
from nti.schema.field import ListOrTuple

from ..interfaces import IConcrete

from ..attributes.interfaces import IweightAttrGroup
from ..attributes.interfaces import IorderingAttrGroup
from ..attributes.interfaces import IselectionAttrGroup
from ..attributes.interfaces import ItimeLimitsAttrGroup
from ..attributes.interfaces import IsectionPartAttrGroup
from ..attributes.interfaces import IassessmentTestAttrGroup
from ..attributes.interfaces import IvariableMappingAttrGroup
from ..attributes.interfaces import IassessmentItemRefAttrGroup
from ..attributes.interfaces import IassessmentSectionAttrGroup
from ..attributes.interfaces import IassessmentSectionRefAttrGroup

from ..expression.interfaces import Iexpression

from ..content.interfaces import IrubricBlock

from ..feedback.interfaces import ItestFeedback

from ..items.interfaces import IitemSessionControl

from ..outcome.interfaces import IoutcomeProcessing

from ..preconditions.interfaces import IbranchRule
from ..preconditions.interfaces import IpreCondition

from ..variables.interfaces import IoutcomeDeclaration

class Iselection(IselectionAttrGroup, IConcrete):
	pass
	
class Iordering(IorderingAttrGroup, IConcrete):
	pass

class ItimeLimits(ItimeLimitsAttrGroup, IConcrete):
	pass
	
class IvariableMapping(IvariableMappingAttrGroup, IConcrete):
	pass

class ItemplateDefault(IConcrete):
	expression = Object(Iexpression , description="An expression", required=True)

class Iweight(IweightAttrGroup, IConcrete):
	pass
	
class IsectionPart(IsectionPartAttrGroup):

	preCondition = ListOrTuple(Object(IpreCondition),
							   description="An optional ordered set of conditions evaluated during the test",
							   min_length=0)

	branchRule = ListOrTuple(Object(IbranchRule),
							 description="An optional ordered set of rules evaluated during the test",
							 min_length=0)

	itemSessionControl = Object(IitemSessionControl,
							 	description="Parameters used to control the allowable states of each item session in this part",
							 	required=False)

	timeLimits = Object(ItimeLimits,
						description="Optionally controls the amount of time a candidate is allowed for this part of the test",
						required=False)

class IassessmentSection(IassessmentSectionAttrGroup,
						 IsectionPart,
						 IConcrete):

	selection = Object(Iselection,
					   description="The rules used to select which children of the section are to be used for each instance of the test",
					   required=False)

	ordering = Object(Iordering,
					  description="The rules used to determine the order in which the children of the section are to be arranged",
					  required=False)

	rubricBlock = ListOrTuple(Object(IrubricBlock),
							  description="Section rubric is presented to the candidate with each item contained by the section",
							  min_length=0)

	sectionPart = ListOrTuple(Object(IsectionPart),
							  description="The ordered list of section parts",
							  min_length=0)

class IassessmentSectionRef(IassessmentSectionRefAttrGroup,
							IsectionPart,
							IConcrete):
	pass

class IassessmentItemRef(IassessmentItemRefAttrGroup,
						 IsectionPart,
						 IConcrete):

	variableMapping = ListOrTuple(Object(IvariableMapping),
								  description="Variable mappings are used to alter the name of an item outcome for the purposes of this test",
								  min_length=0)

	weight = ListOrTuple(Object(Iweight),
						 description="Weights allow custom values to be defined for scaling an item's outcomes",
						 min_length=0)

	templateDefault = ListOrTuple(Object(ItemplateDefault),
								  description="WA template default is used to alter the default value",
								  min_length=0)
	
class ItestPart(ItimeLimitsAttrGroup, IConcrete):

	preCondition = ListOrTuple(Object(IpreCondition),
							   description="An optional ordered set of conditions evaluated during the test",
							   min_length=0)

	branchRule = ListOrTuple(Object(IbranchRule),
									description="An optional ordered set of rules evaluated during the test",
									min_length=0)

	itemSessionControl = Object(IitemSessionControl,
								description="Parameters used to control the allowable states of each item session in this part",
								required=False)

	timeLimits = Object(ItimeLimits,
						description="Optionally controls the amount of time a candidate is allowed for this part of the test.",
						required=False)

	assessmentSection = ListOrTuple(Object(IassessmentSection),
									description="The items contained in each testPart are arranged into sections and sub-sections",
									min_length=1)

	testFeedback = ListOrTuple(Object(ItestFeedback),
							   description="Test-level feedback specific to this part of the test",
							   min_length=0)

class IassessmentTest(IassessmentTestAttrGroup, IConcrete):

	outcomeDeclaration = ListOrTuple(Object(IoutcomeDeclaration),
									 description="Each test has an associated set of outcomes",
									 min_length=0)

	timeLimits = Object(ItimeLimits,
						description="Optionally controls the amount of time a candidate is allowed for the entire test",
						required=False)

	testPart = ListOrTuple(Object(ItestPart),
						   description="Order list of test parts (sections, sub-sections and so on)",
						   min_length=1)

	outcomeProcessing = Object(IoutcomeProcessing,
							   description="The set of rules used for calculating the values of the test outcomes",
							   required=False)

	testFeedback = ListOrTuple(Object(ItestFeedback),
							   description="The ordered test-level feedback controlled by the test outcomes.",
							   min_length=0)
