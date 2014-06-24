# -*- coding: utf-8 -*-
"""
Defines QTI outcome elements

.. $Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface

from nti.schema.fieldproperty import createFieldProperties

from ..basic.elements import QTIElement
from . import interfaces as exp_interfaces

@interface.implementer(exp_interfaces.IbaseValue)
class BaseValue(QTIElement):
	createFieldProperties(exp_interfaces.IbaseValue)

@interface.implementer(exp_interfaces.Ivariable)
class Variable(QTIElement):
	createFieldProperties(exp_interfaces.Ivariable)

@interface.implementer(exp_interfaces.Idefault)
class Default(QTIElement):
	createFieldProperties(exp_interfaces.Idefault)

@interface.implementer(exp_interfaces.Icorrect)
class Correct(QTIElement):
	createFieldProperties(exp_interfaces.Icorrect)

@interface.implementer(exp_interfaces.ImapResponse)
class MapResponse(QTIElement):
	createFieldProperties(exp_interfaces.ImapResponse)

@interface.implementer(exp_interfaces.ImapResponsePoint)
class MapResponsePoint(QTIElement):
	createFieldProperties(exp_interfaces.ImapResponsePoint)

@interface.implementer(exp_interfaces.ImathConstant)
class MathConstant(QTIElement):
	createFieldProperties(exp_interfaces.ImathConstant)

@interface.implementer(exp_interfaces.Inull)
class Null(QTIElement):
	createFieldProperties(exp_interfaces.Inull)

@interface.implementer(exp_interfaces.IrandomInteger)
class RandomInteger(QTIElement):
	createFieldProperties(exp_interfaces.IrandomInteger)

@interface.implementer(exp_interfaces.IrandomFloat)
class RandomFloat(QTIElement):
	createFieldProperties(exp_interfaces.IrandomFloat)

@interface.implementer(exp_interfaces.ItestVariables)
class TestVariables(QTIElement):
	createFieldProperties(exp_interfaces.ItestVariables)

@interface.implementer(exp_interfaces.IoutcomeMaximum)
class OutcomeMaximum(QTIElement):
	createFieldProperties(exp_interfaces.IoutcomeMaximum)

@interface.implementer(exp_interfaces.IoutcomeMinimum)
class OutcomeMinimum(QTIElement):
	createFieldProperties(exp_interfaces.IoutcomeMinimum)

@interface.implementer(exp_interfaces.InumberCorrect)
class NumberCorrect(QTIElement):
	createFieldProperties(exp_interfaces.InumberCorrect)

@interface.implementer(exp_interfaces.InumberIncorrect)
class NumberIncorrect(QTIElement):
	createFieldProperties(exp_interfaces.InumberIncorrect)

@interface.implementer(exp_interfaces.InumberResponded)
class NumberResponded(QTIElement):
	createFieldProperties(exp_interfaces.InumberResponded)

@interface.implementer(exp_interfaces.InumberPresented)
class NumberPresented(QTIElement):
	createFieldProperties(exp_interfaces.InumberPresented)

@interface.implementer(exp_interfaces.InumberSelected)
class NumberSelected(QTIElement):
	createFieldProperties(exp_interfaces.InumberSelected)

@interface.implementer(exp_interfaces.IroundTo)
class RoundTo(QTIElement):
	createFieldProperties(exp_interfaces.IroundTo)

@interface.implementer(exp_interfaces.IstatsOperator)
class StatsOperator(QTIElement):
	createFieldProperties(exp_interfaces.IstatsOperator)
	
@interface.implementer(exp_interfaces.Imax)
class Max(QTIElement):
	createFieldProperties(exp_interfaces.Imax)
	
@interface.implementer(exp_interfaces.Imin)
class Min(QTIElement):
	createFieldProperties(exp_interfaces.Imin)

@interface.implementer(exp_interfaces.ImathOperator)
class MathOperator(QTIElement):
	createFieldProperties(exp_interfaces.ImathOperator)

@interface.implementer(exp_interfaces.Igcd)
class Gcd(QTIElement):
	createFieldProperties(exp_interfaces.Igcd)

@interface.implementer(exp_interfaces.Ilcm)
class Lcm(QTIElement):
	createFieldProperties(exp_interfaces.Ilcm)

@interface.implementer(exp_interfaces.Irepeat)
class Repeat(QTIElement):
	createFieldProperties(exp_interfaces.Irepeat)

@interface.implementer(exp_interfaces.Imultiple)
class Multiple(QTIElement):
	createFieldProperties(exp_interfaces.Imultiple)

@interface.implementer(exp_interfaces.Iordered)
class Ordered(QTIElement):
	createFieldProperties(exp_interfaces.Iordered)

@interface.implementer(exp_interfaces.IcontainerSize)
class ContainerSize(QTIElement):
	createFieldProperties(exp_interfaces.IcontainerSize)
	
@interface.implementer(exp_interfaces.IisNull)
class IsNull(QTIElement):
	createFieldProperties(exp_interfaces.IisNull)

@interface.implementer(exp_interfaces.Iindex)
class Index(QTIElement):
	createFieldProperties(exp_interfaces.Iindex)

@interface.implementer(exp_interfaces.IfieldValue)
class FieldValue(QTIElement):
	createFieldProperties(exp_interfaces.IfieldValue)

@interface.implementer(exp_interfaces.Irandom)
class Random(QTIElement):
	createFieldProperties(exp_interfaces.Irandom)

@interface.implementer(exp_interfaces.Imember)
class Member(QTIElement):
	createFieldProperties(exp_interfaces.Imember)

@interface.implementer(exp_interfaces.Idelete)
class Delete(QTIElement):
	createFieldProperties(exp_interfaces.Idelete)

@interface.implementer(exp_interfaces.Icontains)
class Contains(QTIElement):
	createFieldProperties(exp_interfaces.Icontains)

@interface.implementer(exp_interfaces.Isubstring)
class Substring(QTIElement):
	createFieldProperties(exp_interfaces.Isubstring)

@interface.implementer(exp_interfaces.Inot)
class Not(QTIElement):
	createFieldProperties(exp_interfaces.Inot)

@interface.implementer(exp_interfaces.Iand)
class And(QTIElement):
	createFieldProperties(exp_interfaces.Iand)

@interface.implementer(exp_interfaces.Ior)
class Or(QTIElement):
	createFieldProperties(exp_interfaces.Ior)

@interface.implementer(exp_interfaces.IanyN)
class AnyN(QTIElement):
	createFieldProperties(exp_interfaces.IanyN)

@interface.implementer(exp_interfaces.Imatch)
class Match(QTIElement):
	createFieldProperties(exp_interfaces.Imatch)

@interface.implementer(exp_interfaces.IstringMatch)
class StringMatch(QTIElement):
	createFieldProperties(exp_interfaces.IstringMatch)

@interface.implementer(exp_interfaces.IpatternMatch)
class PatternMatch(QTIElement):
	createFieldProperties(exp_interfaces.IpatternMatch)

@interface.implementer(exp_interfaces.Iequal)
class Equal(QTIElement):
	createFieldProperties(exp_interfaces.Iequal)

@interface.implementer(exp_interfaces.IequalRounded)
class EqualRounded(QTIElement):
	createFieldProperties(exp_interfaces.IequalRounded)

@interface.implementer(exp_interfaces.Iinside)
class Inside(QTIElement):
	createFieldProperties(exp_interfaces.Iinside)

@interface.implementer(exp_interfaces.Ilt)
class Lt(QTIElement):
	createFieldProperties(exp_interfaces.Ilt)

@interface.implementer(exp_interfaces.Igt)
class Gt(QTIElement):
	createFieldProperties(exp_interfaces.Igt)

@interface.implementer(exp_interfaces.Ilte)
class Lte(QTIElement):
	createFieldProperties(exp_interfaces.Ilte)

@interface.implementer(exp_interfaces.Igte)
class Gte(QTIElement):
	createFieldProperties(exp_interfaces.Igte)

@interface.implementer(exp_interfaces.IdurationLT)
class DurationLT(QTIElement):
	createFieldProperties(exp_interfaces.IdurationLT)

@interface.implementer(exp_interfaces.IdurationGTE)
class DurationGTE(QTIElement):
	createFieldProperties(exp_interfaces.IdurationGTE)

@interface.implementer(exp_interfaces.Isum)
class Sum(QTIElement):
	createFieldProperties(exp_interfaces.Isum)

@interface.implementer(exp_interfaces.Iproduct)
class Product(QTIElement):
	createFieldProperties(exp_interfaces.Iproduct)

@interface.implementer(exp_interfaces.Isubtract)
class Subtract(QTIElement):
	createFieldProperties(exp_interfaces.Isubtract)

@interface.implementer(exp_interfaces.Idivide)
class Divide(QTIElement):
	createFieldProperties(exp_interfaces.Idivide)

@interface.implementer(exp_interfaces.Ipower)
class Power(QTIElement):
	createFieldProperties(exp_interfaces.Ipower)

@interface.implementer(exp_interfaces.IintegerDivide)
class IntegerDivide(QTIElement):
	createFieldProperties(exp_interfaces.IintegerDivide)

@interface.implementer(exp_interfaces.IintegerModulus)
class IntegerModulus(QTIElement):
	createFieldProperties(exp_interfaces.IintegerModulus)

@interface.implementer(exp_interfaces.Itruncate)
class Truncate(QTIElement):
	createFieldProperties(exp_interfaces.Itruncate)

@interface.implementer(exp_interfaces.Iround)
class Round(QTIElement):
	createFieldProperties(exp_interfaces.Iround)

@interface.implementer(exp_interfaces.IintegerToFloat)
class IntegerToFloat(QTIElement):
	createFieldProperties(exp_interfaces.IintegerToFloat)

@interface.implementer(exp_interfaces.IcustomOperator)
class CustomOperator(QTIElement):
	createFieldProperties(exp_interfaces.IcustomOperator)
