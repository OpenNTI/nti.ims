# -*- coding: utf-8 -*-
"""
Defines QTI outcome elements

$Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface

from nti.schema.fieldproperty import createFieldProperties

from ..basic.elements import QTIElement
from . import interfaces as cnt_interfaces

@interface.implementer(cnt_interfaces.ItextRun)
class TextRun(QTIElement):
	createFieldProperties(cnt_interfaces.ItextRun)

@interface.implementer(cnt_interfaces.Iabbr)
class Abbr(QTIElement):
	createFieldProperties(cnt_interfaces.Iabbr)

@interface.implementer(cnt_interfaces.Iacronym)
class Acronym(QTIElement):
	createFieldProperties(cnt_interfaces.Iacronym)

@interface.implementer(cnt_interfaces.Iaddress)
class Address(QTIElement):
	createFieldProperties(cnt_interfaces.Iaddress)

@interface.implementer(cnt_interfaces.Iblockquote)
class Blockquote(QTIElement):
	createFieldProperties(cnt_interfaces.Iblockquote)

@interface.implementer(cnt_interfaces.Ibr)
class Br(QTIElement):
	createFieldProperties(cnt_interfaces.Ibr)

@interface.implementer(cnt_interfaces.Icite)
class Cite(QTIElement):
	createFieldProperties(cnt_interfaces.Icite)

@interface.implementer(cnt_interfaces.Icode)
class Code(QTIElement):
	createFieldProperties(cnt_interfaces.Icode)

@interface.implementer(cnt_interfaces.Idfn)
class Dfn(QTIElement):
	createFieldProperties(cnt_interfaces.Idfn)
	
@interface.implementer(cnt_interfaces.Idiv)
class Div(QTIElement):
	createFieldProperties(cnt_interfaces.Idiv)

@interface.implementer(cnt_interfaces.Iem)
class Em(QTIElement):
	createFieldProperties(cnt_interfaces.Iem)
	
@interface.implementer(cnt_interfaces.Ih1)
class H1(QTIElement):
	createFieldProperties(cnt_interfaces.Ih1)

@interface.implementer(cnt_interfaces.Ih2)
class H2(QTIElement):
	createFieldProperties(cnt_interfaces.Ih2)

@interface.implementer(cnt_interfaces.Ih3)
class H3(QTIElement):
	createFieldProperties(cnt_interfaces.Ih3)

@interface.implementer(cnt_interfaces.Ih4)
class H4(QTIElement):
	createFieldProperties(cnt_interfaces.Ih4)

@interface.implementer(cnt_interfaces.Ih5)
class H5(QTIElement):
	createFieldProperties(cnt_interfaces.Ih5)

@interface.implementer(cnt_interfaces.Ih6)
class H6(QTIElement):
	createFieldProperties(cnt_interfaces.Ih6)

@interface.implementer(cnt_interfaces.Ikbd)
class Kbd(QTIElement):
	createFieldProperties(cnt_interfaces.Ikbd)

@interface.implementer(cnt_interfaces.Ip)
class Ip(QTIElement):
	createFieldProperties(cnt_interfaces.Ip)

@interface.implementer(cnt_interfaces.Ipre)
class Ipre(QTIElement):
	createFieldProperties(cnt_interfaces.Ipre)
	
@interface.implementer(cnt_interfaces.Iq)
class Q(QTIElement):
	createFieldProperties(cnt_interfaces.Iq)

@interface.implementer(cnt_interfaces.Isamp)
class Samp(QTIElement):
	createFieldProperties(cnt_interfaces.Isamp)

@interface.implementer(cnt_interfaces.Ispan)
class Span(QTIElement):
	createFieldProperties(cnt_interfaces.Ispan)
	
@interface.implementer(cnt_interfaces.Istrong)
class Strong(QTIElement):
	createFieldProperties(cnt_interfaces.Istrong)

@interface.implementer(cnt_interfaces.Ivar)
class Var(QTIElement):
	createFieldProperties(cnt_interfaces.Ivar)

@interface.implementer(cnt_interfaces.Idl)
class Dl(QTIElement):
	createFieldProperties(cnt_interfaces.Idl)
	
@interface.implementer(cnt_interfaces.Idt)
class Dt(QTIElement):
	createFieldProperties(cnt_interfaces.Idt)

@interface.implementer(cnt_interfaces.Idd)
class Dd(QTIElement):
	createFieldProperties(cnt_interfaces.Idd)

@interface.implementer(cnt_interfaces.Ili)
class Li(QTIElement):
	createFieldProperties(cnt_interfaces.Ili)

@interface.implementer(cnt_interfaces.Iol)
class Ol(QTIElement):
	createFieldProperties(cnt_interfaces.Iol)
	
@interface.implementer(cnt_interfaces.Iul)
class Ul(QTIElement):
	createFieldProperties(cnt_interfaces.Iul)

@interface.implementer(cnt_interfaces.Iobject)
class Object(QTIElement):
	createFieldProperties(cnt_interfaces.Iobject)

@interface.implementer(cnt_interfaces.Iparam)
class Param(QTIElement):
	createFieldProperties(cnt_interfaces.Iparam)

@interface.implementer(cnt_interfaces.Ib)
class B(QTIElement):
	createFieldProperties(cnt_interfaces.Ib)

@interface.implementer(cnt_interfaces.Ibig)
class Big(QTIElement):
	createFieldProperties(cnt_interfaces.Ibig)

@interface.implementer(cnt_interfaces.Ihr)
class Hr(QTIElement):
	createFieldProperties(cnt_interfaces.Ihr)

@interface.implementer(cnt_interfaces.Ii)
class I(QTIElement):
	createFieldProperties(cnt_interfaces.Ii)

@interface.implementer(cnt_interfaces.Ismall)
class Small(QTIElement):
	createFieldProperties(cnt_interfaces.Ismall)

@interface.implementer(cnt_interfaces.Isub)
class Sub(QTIElement):
	createFieldProperties(cnt_interfaces.Isub)

@interface.implementer(cnt_interfaces.Isup)
class Sup(QTIElement):
	createFieldProperties(cnt_interfaces.Isup)

@interface.implementer(cnt_interfaces.Itt)
class Tt(QTIElement):
	createFieldProperties(cnt_interfaces.Itt)

@interface.implementer(cnt_interfaces.Icaption)
class Caption(QTIElement):
	createFieldProperties(cnt_interfaces.Icaption)

@interface.implementer(cnt_interfaces.Icol)
class Col(QTIElement):
	createFieldProperties(cnt_interfaces.Icol)
	
@interface.implementer(cnt_interfaces.Icolgroup)
class Colgroup(QTIElement):
	createFieldProperties(cnt_interfaces.Icolgroup)

@interface.implementer(cnt_interfaces.Itd)
class Td(QTIElement):
	createFieldProperties(cnt_interfaces.Itd)

@interface.implementer(cnt_interfaces.Ith)
class Th(QTIElement):
	createFieldProperties(cnt_interfaces.Ith)

@interface.implementer(cnt_interfaces.Itr)
class Tr(QTIElement):
	createFieldProperties(cnt_interfaces.Itr)
	
@interface.implementer(cnt_interfaces.Ithead)
class Thead(QTIElement):
	createFieldProperties(cnt_interfaces.Ithead)

@interface.implementer(cnt_interfaces.Itfoot)
class Tfoot(QTIElement):
	createFieldProperties(cnt_interfaces.Itfoot)
	
@interface.implementer(cnt_interfaces.Itbody)
class Tbody(QTIElement):
	createFieldProperties(cnt_interfaces.Itbody)

@interface.implementer(cnt_interfaces.Itable)
class Table(QTIElement):
	createFieldProperties(cnt_interfaces.Itable)
	
@interface.implementer(cnt_interfaces.Iimg)
class Img(QTIElement):
	createFieldProperties(cnt_interfaces.Iimg)

@interface.implementer(cnt_interfaces.Ia)
class A(QTIElement):
	createFieldProperties(cnt_interfaces.Ia)

@interface.implementer(cnt_interfaces.Imath)
class Math(QTIElement):
	createFieldProperties(cnt_interfaces.Imath)

@interface.implementer(cnt_interfaces.IfeedbackBlock)
class FeedbackBlock(QTIElement):
	createFieldProperties(cnt_interfaces.IfeedbackBlock)

@interface.implementer(cnt_interfaces.IfeedbackInline)
class FeedbackInline(QTIElement):
	createFieldProperties(cnt_interfaces.IfeedbackInline)

@interface.implementer(cnt_interfaces.IrubricBlock)
class RubricBlock(QTIElement):
	createFieldProperties(cnt_interfaces.IrubricBlock)

@interface.implementer(cnt_interfaces.Istylesheet)
class Stylesheet(QTIElement):
	createFieldProperties(cnt_interfaces.Istylesheet)

@interface.implementer(cnt_interfaces.IitemBody)
class ItemBody(QTIElement):
	createFieldProperties(cnt_interfaces.IitemBody)
