#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Defines QTI Interaction elements

.. $Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface

from nti.schema.fieldproperty import createFieldProperties

from ..basic.elements import QTI
from ..basic.elements import QTIElement
from . import interfaces as int_interfaces

@QTI
@interface.implementer(int_interfaces.IendAttemptInteraction)
class EndAttemptInteraction(QTIElement):
	createFieldProperties(int_interfaces.IendAttemptInteraction)

@QTI
@interface.implementer(int_interfaces.Iprompt)
class Prompt(QTIElement):
	createFieldProperties(int_interfaces.Iprompt)

@QTI
@interface.implementer(int_interfaces.IgapText)
class GapText(QTIElement):
	createFieldProperties(int_interfaces.IgapText)

@QTI
@interface.implementer(int_interfaces.IgapImg)
class GapImg(QTIElement):
	createFieldProperties(int_interfaces.IgapImg)
	
@QTI
@interface.implementer(int_interfaces.Igap)
class Gap(QTIElement):
	createFieldProperties(int_interfaces.Igap)

@QTI
@interface.implementer(int_interfaces.IsimpleAssociableChoice)
class SimpleAssociableChoice(QTIElement):
	createFieldProperties(int_interfaces.IsimpleAssociableChoice)

@QTI
@interface.implementer(int_interfaces.IsimpleChoice)
class SimpleChoice(QTIElement):
	createFieldProperties(int_interfaces.IsimpleChoice)

@QTI
@interface.implementer(int_interfaces.IassociateInteraction)
class AssociateInteraction(QTIElement):
	createFieldProperties(int_interfaces.IassociateInteraction)

@QTI
@interface.implementer(int_interfaces.IchoiceInteraction)
class ChoiceInteraction(QTIElement):
	createFieldProperties(int_interfaces.IchoiceInteraction)

@QTI
@interface.implementer(int_interfaces.IorderInteraction)
class OrderInteraction(QTIElement):
	createFieldProperties(int_interfaces.IorderInteraction)

@QTI
@interface.implementer(int_interfaces.IsimpleMatchSet)
class SimpleMatchSet(QTIElement):
	createFieldProperties(int_interfaces.IsimpleMatchSet)

@QTI
@interface.implementer(int_interfaces.ImatchInteraction)
class MatchInteraction(QTIElement):
	createFieldProperties(int_interfaces.ImatchInteraction)

@QTI
@interface.implementer(int_interfaces.IgapMatchInteraction)
class GapMatchInteraction(QTIElement):
	createFieldProperties(int_interfaces.IgapMatchInteraction)

@QTI
@interface.implementer(int_interfaces.IinlineChoice)
class InlineChoice(QTIElement):
	createFieldProperties(int_interfaces.IinlineChoice)

@QTI
@interface.implementer(int_interfaces.IinlineChoiceInteraction)
class InlineChoiceInteraction(QTIElement):
	createFieldProperties(int_interfaces.IinlineChoiceInteraction)

@QTI
@interface.implementer(int_interfaces.ItextEntryInteraction)
class TextEntryInteraction(QTIElement):
	createFieldProperties(int_interfaces.ItextEntryInteraction)

@QTI
@interface.implementer(int_interfaces.IextendedTextInteraction)
class ExtendedTextInteraction(QTIElement):
	createFieldProperties(int_interfaces.IextendedTextInteraction)

@QTI
@interface.implementer(int_interfaces.IhottextInteraction)
class HottextInteraction(QTIElement):
	createFieldProperties(int_interfaces.IhottextInteraction)

@QTI
@interface.implementer(int_interfaces.Ihottext)
class Hottext(QTIElement):
	createFieldProperties(int_interfaces.Ihottext)

@QTI
@interface.implementer(int_interfaces.IhotspotChoice)
class HotspotChoice(QTIElement):
	createFieldProperties(int_interfaces.IhotspotChoice)

@QTI
@interface.implementer(int_interfaces.IassociableHotspot)
class AssociableHotspot(QTIElement):
	createFieldProperties(int_interfaces.IassociableHotspot)

@QTI
@interface.implementer(int_interfaces.IhotspotInteraction)
class HotspotInteraction(QTIElement):
	createFieldProperties(int_interfaces.IhotspotInteraction)

@QTI
@interface.implementer(int_interfaces.IselectPointInteraction)
class SelectPointInteraction(QTIElement):
	createFieldProperties(int_interfaces.IselectPointInteraction)

@QTI
@interface.implementer(int_interfaces.IgraphicOrderInteraction)
class GraphicOrderInteraction(QTIElement):
	createFieldProperties(int_interfaces.IgraphicOrderInteraction)

@QTI
@interface.implementer(int_interfaces.IgraphicAssociateInteraction)
class GraphicAssociateInteraction(QTIElement):
	createFieldProperties(int_interfaces.IgraphicAssociateInteraction)

@QTI
@interface.implementer(int_interfaces.IgraphicGapMatchInteraction)
class GraphicGapMatchInteraction(QTIElement):
	createFieldProperties(int_interfaces.IgraphicGapMatchInteraction)

@QTI
@interface.implementer(int_interfaces.IpositionObjectInteraction)
class PositionObjectInteraction(QTIElement):
	createFieldProperties(int_interfaces.IpositionObjectInteraction)

@QTI
@interface.implementer(int_interfaces.IpositionObjectStage)
class PositionObjectStage(QTIElement):
	createFieldProperties(int_interfaces.IpositionObjectStage)

@QTI
@interface.implementer(int_interfaces.IsliderInteraction)
class SliderInteraction(QTIElement):
	createFieldProperties(int_interfaces.IsliderInteraction)

@QTI
@interface.implementer(int_interfaces.ImediaInteraction)
class MediaInteraction(QTIElement):
	createFieldProperties(int_interfaces.ImediaInteraction)

@QTI
@interface.implementer(int_interfaces.IdrawingInteraction)
class DrawingInteraction(QTIElement):
	createFieldProperties(int_interfaces.IdrawingInteraction)

@QTI
@interface.implementer(int_interfaces.IuploadInteraction)
class UploadInteraction(QTIElement):
	createFieldProperties(int_interfaces.IuploadInteraction)

@QTI
@interface.implementer(int_interfaces.IcustomInteraction)
class CustomInteraction(QTIElement):
	createFieldProperties(int_interfaces.IcustomInteraction)

@QTI
@interface.implementer(int_interfaces.IinfoControl)
class InfoControl(QTIElement):
	createFieldProperties(int_interfaces.IinfoControl)
