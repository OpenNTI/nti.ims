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

from ..basic.elements import QTIElement
from . import interfaces as int_interfaces

@interface.implementer(int_interfaces.IendAttemptInteraction)
class EndAttemptInteraction(QTIElement):
	createFieldProperties(int_interfaces.IendAttemptInteraction)

@interface.implementer(int_interfaces.Iprompt)
class Prompt(QTIElement):
	createFieldProperties(int_interfaces.Iprompt)

@interface.implementer(int_interfaces.IgapText)
class GapText(QTIElement):
	createFieldProperties(int_interfaces.IgapText)

@interface.implementer(int_interfaces.IgapImg)
class GapImg(QTIElement):
	createFieldProperties(int_interfaces.IgapImg)
	
@interface.implementer(int_interfaces.Igap)
class Gap(QTIElement):
	createFieldProperties(int_interfaces.Igap)

@interface.implementer(int_interfaces.IsimpleAssociableChoice)
class SimpleAssociableChoice(QTIElement):
	createFieldProperties(int_interfaces.IsimpleAssociableChoice)

@interface.implementer(int_interfaces.IsimpleChoice)
class SimpleChoice(QTIElement):
	createFieldProperties(int_interfaces.IsimpleChoice)

@interface.implementer(int_interfaces.IassociateInteraction)
class AssociateInteraction(QTIElement):
	createFieldProperties(int_interfaces.IassociateInteraction)

@interface.implementer(int_interfaces.IchoiceInteraction)
class ChoiceInteraction(QTIElement):
	createFieldProperties(int_interfaces.IchoiceInteraction)

@interface.implementer(int_interfaces.IorderInteraction)
class OrderInteraction(QTIElement):
	createFieldProperties(int_interfaces.IorderInteraction)

@interface.implementer(int_interfaces.IsimpleMatchSet)
class SimpleMatchSet(QTIElement):
	createFieldProperties(int_interfaces.IsimpleMatchSet)

@interface.implementer(int_interfaces.ImatchInteraction)
class MatchInteraction(QTIElement):
	createFieldProperties(int_interfaces.ImatchInteraction)

@interface.implementer(int_interfaces.IgapMatchInteraction)
class GapMatchInteraction(QTIElement):
	createFieldProperties(int_interfaces.IgapMatchInteraction)

@interface.implementer(int_interfaces.IinlineChoice)
class InlineChoice(QTIElement):
	createFieldProperties(int_interfaces.IinlineChoice)

@interface.implementer(int_interfaces.IinlineChoiceInteraction)
class InlineChoiceInteraction(QTIElement):
	createFieldProperties(int_interfaces.IinlineChoiceInteraction)

@interface.implementer(int_interfaces.ItextEntryInteraction)
class TextEntryInteraction(QTIElement):
	createFieldProperties(int_interfaces.ItextEntryInteraction)

@interface.implementer(int_interfaces.IextendedTextInteraction)
class ExtendedTextInteraction(QTIElement):
	createFieldProperties(int_interfaces.IextendedTextInteraction)

@interface.implementer(int_interfaces.IhottextInteraction)
class HottextInteraction(QTIElement):
	createFieldProperties(int_interfaces.IhottextInteraction)

@interface.implementer(int_interfaces.Ihottext)
class Hottext(QTIElement):
	createFieldProperties(int_interfaces.Ihottext)

@interface.implementer(int_interfaces.IhotspotChoice)
class HotspotChoice(QTIElement):
	createFieldProperties(int_interfaces.IhotspotChoice)

@interface.implementer(int_interfaces.IassociableHotspot)
class AssociableHotspot(QTIElement):
	createFieldProperties(int_interfaces.IassociableHotspot)

@interface.implementer(int_interfaces.IhotspotInteraction)
class HotspotInteraction(QTIElement):
	createFieldProperties(int_interfaces.IhotspotInteraction)

@interface.implementer(int_interfaces.IselectPointInteraction)
class SelectPointInteraction(QTIElement):
	createFieldProperties(int_interfaces.IselectPointInteraction)

@interface.implementer(int_interfaces.IgraphicOrderInteraction)
class GraphicOrderInteraction(QTIElement):
	createFieldProperties(int_interfaces.IgraphicOrderInteraction)

@interface.implementer(int_interfaces.IgraphicAssociateInteraction)
class GraphicAssociateInteraction(QTIElement):
	createFieldProperties(int_interfaces.IgraphicAssociateInteraction)

@interface.implementer(int_interfaces.IgraphicGapMatchInteraction)
class GraphicGapMatchInteraction(QTIElement):
	createFieldProperties(int_interfaces.IgraphicGapMatchInteraction)

@interface.implementer(int_interfaces.IpositionObjectInteraction)
class PositionObjectInteraction(QTIElement):
	createFieldProperties(int_interfaces.IpositionObjectInteraction)

@interface.implementer(int_interfaces.IpositionObjectStage)
class PositionObjectStage(QTIElement):
	createFieldProperties(int_interfaces.IpositionObjectStage)

@interface.implementer(int_interfaces.IsliderInteraction)
class SliderInteraction(QTIElement):
	createFieldProperties(int_interfaces.IsliderInteraction)

@interface.implementer(int_interfaces.ImediaInteraction)
class MediaInteraction(QTIElement):
	createFieldProperties(int_interfaces.ImediaInteraction)

@interface.implementer(int_interfaces.IdrawingInteraction)
class DrawingInteraction(QTIElement):
	createFieldProperties(int_interfaces.IdrawingInteraction)

@interface.implementer(int_interfaces.IuploadInteraction)
class UploadInteraction(QTIElement):
	createFieldProperties(int_interfaces.IuploadInteraction)

@interface.implementer(int_interfaces.IcustomInteraction)
class CustomInteraction(QTIElement):
	createFieldProperties(int_interfaces.IcustomInteraction)

@interface.implementer(int_interfaces.IinfoControl)
class InfoControl(QTIElement):
	createFieldProperties(int_interfaces.IinfoControl)
