#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Defines QTI content interfaces

.. $Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

from zope.interface.common.sequence import IFiniteSequence

from nti.schema.field import List
from nti.schema.field import Object

from .. import interfaces as qti_interfaces

from ..basic import interfaces as basic_interfaces
from ..attributes import interfaces as attr_interfaces
	
class IobjectFlow(qti_interfaces.IQTIElement):
	pass

class Iinline(qti_interfaces.IQTIElement):
	pass
			
class Iblock(qti_interfaces.IQTIElement):
	pass
	
class Iflow(IobjectFlow, attr_interfaces.IflowAttrGroup):
	pass
	
class IinlineStatic(Iinline):
	pass
	
class IblockStatic(Iblock):
	pass
	
class IflowStatic(Iflow):
	pass
	
class IsimpleInline(basic_interfaces.IbodyElement,
					IflowStatic,
					IinlineStatic,
					IFiniteSequence):

	inline = List(Object(Iinline),
				  description='inline objects contained',
				  min_length=0)
	
class IsimpleBlock(IflowStatic,
				   basic_interfaces.IbodyElement,
				   IblockStatic,
				   IFiniteSequence):

	block = List(Object(Iblock),
				 description='block objects contained',
				 min_length=0)
	
class IatomicInline(IflowStatic,
					basic_interfaces.IbodyElement,
					IinlineStatic):
	pass
	
class IAtomicBlock(basic_interfaces.IbodyElement,
				   IflowStatic,
				   IblockStatic,
				   IFiniteSequence):

	inline = List(Object(Iinline),
				  description='The ordered inline objects contained',
				  min_length=0)

class ItextRun(IflowStatic,
			   IinlineStatic,
			   basic_interfaces.ITextOrVariable,
			   qti_interfaces.IConcrete):
	pass
	
# xhtml elements

class Iabbr(IsimpleInline, qti_interfaces.IConcrete):
	pass
	
class Iacronym(IsimpleInline, qti_interfaces.IConcrete):
	pass
	
class Iaddress(IAtomicBlock, qti_interfaces.IConcrete):
	pass

class Iblockquote(IsimpleBlock,
				  attr_interfaces.IblockquoteAttrGroup,
				  qti_interfaces.IConcrete):
	pass
	
class Ibr(IatomicInline, qti_interfaces.IConcrete):
	pass
	
class Icite(IsimpleInline, qti_interfaces.IConcrete):
	pass
	
class Icode(IsimpleInline, qti_interfaces.IConcrete):
	pass
	
class Idfn(IsimpleInline, qti_interfaces.IConcrete):
	pass
	
class Idiv(IflowStatic,
		   basic_interfaces.IbodyElement,
		   IblockStatic, IFiniteSequence,
		   qti_interfaces.IConcrete):

	flow = List(Object(Iflow),
				description='flow objects contained',
				min_length=0)
	
class Iem(IsimpleInline, qti_interfaces.IConcrete):
	pass
	
class Ih1(IAtomicBlock, qti_interfaces.IConcrete):
	pass

class Ih2(IAtomicBlock, qti_interfaces.IConcrete):
	pass

class Ih3(IAtomicBlock, qti_interfaces.IConcrete):
	pass	
	
class Ih4(IAtomicBlock, qti_interfaces.IConcrete):
	pass
	
class Ih5(IAtomicBlock, qti_interfaces.IConcrete):
	pass
	
class Ih6(IAtomicBlock, qti_interfaces.IConcrete):
	pass
	
class Ikbd(IsimpleInline, qti_interfaces.IConcrete):
	pass
	
class Ip(IAtomicBlock, qti_interfaces.IConcrete):
	pass
	
class Ipre(IAtomicBlock, qti_interfaces.IConcrete):
	"""
	Although pre inherits from atomicBlock it must not contain, either
	directly or indirectly, any of the following objects:
	img, object, big, small, sub, sup.
	"""
	pass
	
class Iq(IsimpleInline,
		 attr_interfaces.IqAttrGroup,
		 qti_interfaces.IConcrete):
	pass
	
class Isamp(IsimpleInline, qti_interfaces.IConcrete):
	pass
	
class Ispan(IsimpleInline, qti_interfaces.IConcrete):
	pass

class Istrong(IsimpleInline, qti_interfaces.IConcrete):
	pass
	
class Ivar(IsimpleInline, qti_interfaces.IConcrete):
	pass

# list elements

class IDLElement(basic_interfaces.IbodyElement):
	pass

class Idl(IblockStatic,
		  basic_interfaces.IbodyElement,
		  IflowStatic, IFiniteSequence,
		  qti_interfaces.IConcrete):

	dlElement = List(Object(IDLElement),
					 description='The ordered dl elements contained',
					 min_length=0)
	
class Idt(IDLElement, IFiniteSequence, qti_interfaces.IConcrete):

	inline = List(Object(Iinline),
				  description='The ordered inline elements contained',
				  min_length=0)

class Idd(IDLElement, IFiniteSequence, qti_interfaces.IConcrete):

	flow = List(Object(Iflow),
				description='The ordered flow elements contained',
				min_length=0)

class Ili(basic_interfaces.IbodyElement,
		  IFiniteSequence,
		  qti_interfaces.IConcrete):

	flow = List(Object(Iflow),
				description='The ordered flow elements contained',
				min_length=0)

class Iol(IblockStatic,
		  basic_interfaces.IbodyElement,
		  IflowStatic,
		  IFiniteSequence,
		  qti_interfaces.IConcrete):

	li = List(Object(Ili),
			  description='The ordered li elements contained',
			  min_length=0)
	
class Iul(IblockStatic,
		  basic_interfaces.IbodyElement,
		  IflowStatic,
		  IFiniteSequence,
		  qti_interfaces.IConcrete):

	li = List(Object(Ili),
			  description='The ordered li elements contained',
			  min_length=0)
		
# object elements

class Iobject(basic_interfaces.IbodyElement,
			  IflowStatic,
			  IinlineStatic,
			  IFiniteSequence,
			  attr_interfaces.IobjectAttrGroup,
			  qti_interfaces.IConcrete):

	objectFlow = List(Object(IobjectFlow),
					  description='The ordered objectflow elements contained',
					  min_length=0)

class Iparam(IobjectFlow,
			 attr_interfaces.IparamAttrGroup,
			 qti_interfaces.IConcrete):
	pass
	
# presentation Elements

class Ib(IsimpleInline, qti_interfaces.IConcrete):
	pass

class Ibig(IsimpleInline, qti_interfaces.IConcrete):
	pass

class Ihr(IblockStatic,
		  basic_interfaces.IbodyElement,
		  IflowStatic,
		  qti_interfaces.IConcrete):
	pass

class Ii(IsimpleInline, qti_interfaces.IConcrete):
	pass

class Ismall(IsimpleInline, qti_interfaces.IConcrete):
	pass

class Isub(IsimpleInline, qti_interfaces.IConcrete):
	pass

class Isup(IsimpleInline, qti_interfaces.IConcrete):
	pass	

class Itt(IsimpleInline, qti_interfaces.IConcrete):
	pass

# table elements

class Icaption(basic_interfaces.IbodyElement,
			   IFiniteSequence,
			   qti_interfaces.IConcrete):

	inline = List(Object(Iinline),
				  description='The ordered inline elements contained',
				  min_length=0)

class Icol(basic_interfaces.IbodyElement, attr_interfaces.IcolAttrGroup, qti_interfaces.IConcrete):
	pass	
	
class Icolgroup(basic_interfaces.IbodyElement,
				attr_interfaces.IcolgroupAttrGroup,
				IFiniteSequence,
				qti_interfaces.IConcrete):

	col = List(Object(Icol),
			   description='The ordered col elements contained',
			   min_length=0)

class ItableCell(basic_interfaces.IbodyElement,
				 attr_interfaces.ItableCellAttrGroup,
				 IFiniteSequence):

	flow = List(Object(Iflow),
				description='The ordered flow elements contained',
				min_length=0)

class Itd(ItableCell, qti_interfaces.IConcrete):
	pass
	
class Ith(ItableCell, qti_interfaces.IConcrete):
	pass
	
class Itr(basic_interfaces.IbodyElement,
		  IFiniteSequence,
		  qti_interfaces.IConcrete):

	tableCell = List(Object(ItableCell),
					 description='tableCell elements contained',
					 min_length=0)
	
class Ithead(basic_interfaces.IbodyElement,
			 IFiniteSequence,
			 qti_interfaces.IConcrete):

	tr = List(Object(Itr),
			  description='The ordered tr elements contained',
			  min_length=1)
	
class Itfoot(basic_interfaces.IbodyElement,
			 IFiniteSequence,
			 qti_interfaces.IConcrete):

	tr = List(Object(Itr),
			  description='The ordered tr elements contained',
			  min_length=1)
	
class Itbody(basic_interfaces.IbodyElement,
			 IFiniteSequence,
			 qti_interfaces.IConcrete):

	tr = List(Object(Itr),
			  description='The ordered tr elements contained',
			  min_length=1)
	
class Itable(IblockStatic,
			 basic_interfaces.IbodyElement, IflowStatic,
			 attr_interfaces.ItableAttrGroup,
			 qti_interfaces.IConcrete):

	caption = Object(Icaption, description='the table caption')

	col = List(Object(Icol),
			   description='Table direct col (Must not contain any colgroup elements)',
			   min_length=0,
			   required=False)

	colgroup = List(Object(Icolgroup),
					description='Table direct colgroups (Must not contain any col elements)',
					min_length=0,
					required=False)

	thead = Object(Ithead, description='table head', required=False)

	tfoot = Object(Itfoot, description='table head', required=False)

	tbody = List(Object(Itbody), description='table body', min_length=1, required=True)

# image Element

class Iimg(IatomicInline,
		   attr_interfaces.IimgAttrGroup,
		   qti_interfaces.IConcrete):
	pass

# hypertext Element

class Ia(IatomicInline,
		 attr_interfaces.IaAttrGroup,
		 qti_interfaces.IConcrete):
	pass

# math element

class Imath(IblockStatic,
			IflowStatic,
			IinlineStatic,
			qti_interfaces.IConcrete):
	pass

# variable element

class IfeedbackElement(attr_interfaces.IFeedbackAttrGroup):
	pass

class IfeedbackBlock(IfeedbackElement,
					 IsimpleBlock,
					 qti_interfaces.IConcrete):
	pass

class IfeedbackInline(IfeedbackElement,
					  IsimpleInline,
					  qti_interfaces.IConcrete):
	pass
	
class IrubricBlock(attr_interfaces.IviewAttrGroup,
				   qti_interfaces.IConcrete):
	pass

# formatting items with stylesheets

class Istylesheet(attr_interfaces.IstylesheetAttrGroup,
				  qti_interfaces.IConcrete):
	pass
	
class IitemBody(basic_interfaces.IbodyElement,
				qti_interfaces.IConcrete):

	blocks = List(Object(Iblock),
				  description='The item body blocks',
				  required=False)

