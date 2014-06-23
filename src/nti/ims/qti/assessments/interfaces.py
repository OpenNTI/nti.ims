# -*- coding: utf-8 -*-
"""
.. $Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

from nti.schema.field import Object
from nti.schema.field import ListOrTuple

from ..content import interfaces as cnt_interfaces
from ..outcome import interfaces as out_interfaces
from ..items import interfaces as items_interfaces
from ..variables import interfaces as var_interfaces
from ..expression import interfaces as exp_interfaces
from ..attributes import interfaces as attr_interfaces
from ..preconditions import interfaces as pre_interfaces
from ..feedback import interfaces as feedback_interfaces

from .. import interfaces as qti_interfaces

class Iselection(attr_interfaces.IselectionAttrGroup, qti_interfaces.IConcrete):
	pass
	
class Iordering(attr_interfaces.IorderingAttrGroup, qti_interfaces.IConcrete):
	pass

class ItimeLimits(attr_interfaces.ItimeLimitsAttrGroup, qti_interfaces.IConcrete):
	pass
	
class IvariableMapping(attr_interfaces.IvariableMappingAttrGroup, qti_interfaces.IConcrete):
	pass

class ItemplateDefault(qti_interfaces.IConcrete):
	expression = Object(exp_interfaces.Iexpression , title="An expression", required=True)

class Iweight(attr_interfaces.IweightAttrGroup, qti_interfaces.IConcrete):
	pass
	
class IsectionPart(attr_interfaces.IsectionPartAttrGroup):
	preCondition = ListOrTuple(Object(pre_interfaces.IpreCondition),
							   title="An optional ordered set of conditions evaluated during the test",
							   min_length=0)

	branchRule = ListOrTuple(Object(pre_interfaces.IbranchRule),
							 title="An optional ordered set of rules evaluated during the test",
							 min_length=0)

	itemSessionControl = Object(items_interfaces.IitemSessionControl,
							 	title="Parameters used to control the allowable states of each item session in this part",
							 	required=False)

	timeLimits = Object(ItimeLimits,
						title="Optionally controls the amount of time a candidate is allowed for this part of the test",
						required=False)

class IassessmentSection(attr_interfaces.IassessmentSectionAttrGroup,
						 IsectionPart,
						 qti_interfaces.IConcrete):
	selection = Object(Iselection,
					   title="The rules used to select which children of the section are to be used for each instance of the test",
					   required=False)

	ordering = Object(Iordering,
					  title="The rules used to determine the order in which the children of the section are to be arranged",
					  required=False)

	rubricBlock = ListOrTuple(Object(cnt_interfaces.IrubricBlock),
							  title="Section rubric is presented to the candidate with each item contained by the section",
							  min_length=0)

	sectionPart = ListOrTuple(Object(IsectionPart),
							  title="The ordered list of section parts",
							  min_length=0)

class IassessmentSectionRef(attr_interfaces.IassessmentSectionRefAttrGroup,
							IsectionPart,
							qti_interfaces.IConcrete):
	pass

class IassessmentItemRef(attr_interfaces.IassessmentItemRefAttrGroup,
						 IsectionPart,
						 qti_interfaces.IConcrete):

	variableMapping = ListOrTuple(Object(IvariableMapping),
								  title="Variable mappings are used to alter the name of an item outcome for the purposes of this test",
								  min_length=0)

	weight = ListOrTuple(Object(Iweight),
						 title="Weights allow custom values to be defined for scaling an item's outcomes",
						 min_length=0)

	templateDefault = ListOrTuple(Object(ItemplateDefault),
								  title="WA template default is used to alter the default value",
								  min_length=0)
	
class ItestPart(attr_interfaces.ItimeLimitsAttrGroup, qti_interfaces.IConcrete):
	preCondition = ListOrTuple(Object(pre_interfaces.IpreCondition),
							   title="An optional ordered set of conditions evaluated during the test",
							   min_length=0)

	branchRule = ListOrTuple(Object(pre_interfaces.IbranchRule),
									title="An optional ordered set of rules evaluated during the test",
									min_length=0)

	itemSessionControl = Object(items_interfaces.IitemSessionControl,
								title="Parameters used to control the allowable states of each item session in this part",
								required=False)

	timeLimits = Object(ItimeLimits,
						title="Optionally controls the amount of time a candidate is allowed for this part of the test.",
						required=False)

	assessmentSection = ListOrTuple(Object(IassessmentSection),
									title="The items contained in each testPart are arranged into sections and sub-sections",
									min_length=1)

	testFeedback = ListOrTuple(Object(feedback_interfaces.ItestFeedback),
							   title="Test-level feedback specific to this part of the test",
							   min_length=0)

class IassessmentTest(attr_interfaces.IassessmentTestAttrGroup, qti_interfaces.IConcrete):

	outcomeDeclaration = ListOrTuple(Object(var_interfaces.IoutcomeDeclaration),
									 title="Each test has an associated set of outcomes",
									 min_length=0)

	timeLimits = Object(ItimeLimits,
						title="Optionally controls the amount of time a candidate is allowed for the entire test",
						required=False)

	testPart = ListOrTuple(Object(ItestPart),
						   title="Order list of test parts (sections, sub-sections and so on)",
						   min_length=1)

	outcomeProcessing = Object(out_interfaces.IoutcomeProcessing,
							   title="The set of rules used for calculating the values of the test outcomes",
							   required=False)

	testFeedback = ListOrTuple(Object(feedback_interfaces.ItestFeedback),
							   title="The ordered test-level feedback controlled by the test outcomes.",
							   min_length=0)
