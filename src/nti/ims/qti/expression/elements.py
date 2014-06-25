#!/usr/bin/env python
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

from ..basic.elements import QTI
from ..basic.elements import QTIElement
from . import interfaces as exp_interfaces

@QTI
@interface.implementer(exp_interfaces.IbaseValue)
class BaseValue(QTIElement):
	createFieldProperties(exp_interfaces.IbaseValue)

@QTI
@interface.implementer(exp_interfaces.Ivariable)
class Variable(QTIElement):
	createFieldProperties(exp_interfaces.Ivariable)

@QTI
@interface.implementer(exp_interfaces.Idefault)
class Default(QTIElement):
	createFieldProperties(exp_interfaces.Idefault)

@QTI
@interface.implementer(exp_interfaces.Icorrect)
class Correct(QTIElement):
	createFieldProperties(exp_interfaces.Icorrect)

@QTI
@interface.implementer(exp_interfaces.ImapResponse)
class MapResponse(QTIElement):
	createFieldProperties(exp_interfaces.ImapResponse)

@QTI
@interface.implementer(exp_interfaces.ImapResponsePoint)
class MapResponsePoint(QTIElement):
	createFieldProperties(exp_interfaces.ImapResponsePoint)

@QTI
@interface.implementer(exp_interfaces.ImathConstant)
class MathConstant(QTIElement):
	createFieldProperties(exp_interfaces.ImathConstant)

@QTI
@interface.implementer(exp_interfaces.Inull)
class Null(QTIElement):
	createFieldProperties(exp_interfaces.Inull)

@QTI
@interface.implementer(exp_interfaces.IrandomInteger)
class RandomInteger(QTIElement):
	createFieldProperties(exp_interfaces.IrandomInteger)

@QTI
@interface.implementer(exp_interfaces.IrandomFloat)
class RandomFloat(QTIElement):
	createFieldProperties(exp_interfaces.IrandomFloat)

@QTI
@interface.implementer(exp_interfaces.ItestVariables)
class TestVariables(QTIElement):
	createFieldProperties(exp_interfaces.ItestVariables)

@QTI
@interface.implementer(exp_interfaces.IoutcomeMaximum)
class OutcomeMaximum(QTIElement):
	createFieldProperties(exp_interfaces.IoutcomeMaximum)

@QTI
@interface.implementer(exp_interfaces.IoutcomeMinimum)
class OutcomeMinimum(QTIElement):
	createFieldProperties(exp_interfaces.IoutcomeMinimum)

@QTI
@interface.implementer(exp_interfaces.InumberCorrect)
class NumberCorrect(QTIElement):
	createFieldProperties(exp_interfaces.InumberCorrect)

@QTI
@interface.implementer(exp_interfaces.InumberIncorrect)
class NumberIncorrect(QTIElement):
	createFieldProperties(exp_interfaces.InumberIncorrect)

@QTI
@interface.implementer(exp_interfaces.InumberResponded)
class NumberResponded(QTIElement):
	createFieldProperties(exp_interfaces.InumberResponded)

@QTI
@interface.implementer(exp_interfaces.InumberPresented)
class NumberPresented(QTIElement):
	createFieldProperties(exp_interfaces.InumberPresented)

@QTI
@interface.implementer(exp_interfaces.InumberSelected)
class NumberSelected(QTIElement):
	createFieldProperties(exp_interfaces.InumberSelected)

@QTI
@interface.implementer(exp_interfaces.IroundTo)
class RoundTo(QTIElement):
	createFieldProperties(exp_interfaces.IroundTo)

@QTI
@interface.implementer(exp_interfaces.IstatsOperator)
class StatsOperator(QTIElement):
	createFieldProperties(exp_interfaces.IstatsOperator)
	
@QTI
@interface.implementer(exp_interfaces.Imax)
class Max(QTIElement):
	createFieldProperties(exp_interfaces.Imax)
	
@QTI
@interface.implementer(exp_interfaces.Imin)
class Min(QTIElement):
	createFieldProperties(exp_interfaces.Imin)

@QTI
@interface.implementer(exp_interfaces.ImathOperator)
class MathOperator(QTIElement):
	createFieldProperties(exp_interfaces.ImathOperator)

@QTI
@interface.implementer(exp_interfaces.Igcd)
class Gcd(QTIElement):
	createFieldProperties(exp_interfaces.Igcd)

@QTI
@interface.implementer(exp_interfaces.Ilcm)
class Lcm(QTIElement):
	createFieldProperties(exp_interfaces.Ilcm)

@QTI
@interface.implementer(exp_interfaces.Irepeat)
class Repeat(QTIElement):
	createFieldProperties(exp_interfaces.Irepeat)

@QTI
@interface.implementer(exp_interfaces.Imultiple)
class Multiple(QTIElement):
	createFieldProperties(exp_interfaces.Imultiple)

@QTI
@interface.implementer(exp_interfaces.Iordered)
class Ordered(QTIElement):
	createFieldProperties(exp_interfaces.Iordered)

@QTI
@interface.implementer(exp_interfaces.IcontainerSize)
class ContainerSize(QTIElement):
	createFieldProperties(exp_interfaces.IcontainerSize)
	
@QTI
@interface.implementer(exp_interfaces.IisNull)
class IsNull(QTIElement):
	createFieldProperties(exp_interfaces.IisNull)

@QTI
@interface.implementer(exp_interfaces.Iindex)
class Index(QTIElement):
	createFieldProperties(exp_interfaces.Iindex)

@QTI
@interface.implementer(exp_interfaces.IfieldValue)
class FieldValue(QTIElement):
	createFieldProperties(exp_interfaces.IfieldValue)

@QTI
@interface.implementer(exp_interfaces.Irandom)
class Random(QTIElement):
	createFieldProperties(exp_interfaces.Irandom)

@QTI
@interface.implementer(exp_interfaces.Imember)
class Member(QTIElement):
	createFieldProperties(exp_interfaces.Imember)

@QTI
@interface.implementer(exp_interfaces.Idelete)
class Delete(QTIElement):
	createFieldProperties(exp_interfaces.Idelete)

@QTI
@interface.implementer(exp_interfaces.Icontains)
class Contains(QTIElement):
	createFieldProperties(exp_interfaces.Icontains)

@QTI
@interface.implementer(exp_interfaces.Isubstring)
class Substring(QTIElement):
	createFieldProperties(exp_interfaces.Isubstring)

@QTI
@interface.implementer(exp_interfaces.Inot)
class Not(QTIElement):
	createFieldProperties(exp_interfaces.Inot)

@QTI
@interface.implementer(exp_interfaces.Iand)
class And(QTIElement):
	createFieldProperties(exp_interfaces.Iand)

@QTI
@interface.implementer(exp_interfaces.Ior)
class Or(QTIElement):
	createFieldProperties(exp_interfaces.Ior)

@QTI
@interface.implementer(exp_interfaces.IanyN)
class AnyN(QTIElement):
	createFieldProperties(exp_interfaces.IanyN)

@QTI
@interface.implementer(exp_interfaces.Imatch)
class Match(QTIElement):
	createFieldProperties(exp_interfaces.Imatch)

@QTI
@interface.implementer(exp_interfaces.IstringMatch)
class StringMatch(QTIElement):
	createFieldProperties(exp_interfaces.IstringMatch)

@QTI
@interface.implementer(exp_interfaces.IpatternMatch)
class PatternMatch(QTIElement):
	createFieldProperties(exp_interfaces.IpatternMatch)

@QTI
@interface.implementer(exp_interfaces.Iequal)
class Equal(QTIElement):
	createFieldProperties(exp_interfaces.Iequal)

@QTI
@interface.implementer(exp_interfaces.IequalRounded)
class EqualRounded(QTIElement):
	createFieldProperties(exp_interfaces.IequalRounded)

@QTI
@interface.implementer(exp_interfaces.Iinside)
class Inside(QTIElement):
	createFieldProperties(exp_interfaces.Iinside)

@QTI
@interface.implementer(exp_interfaces.Ilt)
class Lt(QTIElement):
	createFieldProperties(exp_interfaces.Ilt)

@QTI
@interface.implementer(exp_interfaces.Igt)
class Gt(QTIElement):
	createFieldProperties(exp_interfaces.Igt)

@QTI
@interface.implementer(exp_interfaces.Ilte)
class Lte(QTIElement):
	createFieldProperties(exp_interfaces.Ilte)

@QTI
@interface.implementer(exp_interfaces.Igte)
class Gte(QTIElement):
	createFieldProperties(exp_interfaces.Igte)

@QTI
@interface.implementer(exp_interfaces.IdurationLT)
class DurationLT(QTIElement):
	createFieldProperties(exp_interfaces.IdurationLT)

@QTI
@interface.implementer(exp_interfaces.IdurationGTE)
class DurationGTE(QTIElement):
	createFieldProperties(exp_interfaces.IdurationGTE)

@QTI
@interface.implementer(exp_interfaces.Isum)
class Sum(QTIElement):
	createFieldProperties(exp_interfaces.Isum)

@QTI
@interface.implementer(exp_interfaces.Iproduct)
class Product(QTIElement):
	createFieldProperties(exp_interfaces.Iproduct)

@QTI
@interface.implementer(exp_interfaces.Isubtract)
class Subtract(QTIElement):
	createFieldProperties(exp_interfaces.Isubtract)

@QTI
@interface.implementer(exp_interfaces.Idivide)
class Divide(QTIElement):
	createFieldProperties(exp_interfaces.Idivide)

@QTI
@interface.implementer(exp_interfaces.Ipower)
class Power(QTIElement):
	createFieldProperties(exp_interfaces.Ipower)

@QTI
@interface.implementer(exp_interfaces.IintegerDivide)
class IntegerDivide(QTIElement):
	createFieldProperties(exp_interfaces.IintegerDivide)

@QTI
@interface.implementer(exp_interfaces.IintegerModulus)
class IntegerModulus(QTIElement):
	createFieldProperties(exp_interfaces.IintegerModulus)

@QTI
@interface.implementer(exp_interfaces.Itruncate)
class Truncate(QTIElement):
	createFieldProperties(exp_interfaces.Itruncate)

@QTI
@interface.implementer(exp_interfaces.Iround)
class Round(QTIElement):
	createFieldProperties(exp_interfaces.Iround)

@QTI
@interface.implementer(exp_interfaces.IintegerToFloat)
class IntegerToFloat(QTIElement):
	createFieldProperties(exp_interfaces.IintegerToFloat)

@QTI
@interface.implementer(exp_interfaces.IcustomOperator)
class CustomOperator(QTIElement):
	createFieldProperties(exp_interfaces.IcustomOperator)
