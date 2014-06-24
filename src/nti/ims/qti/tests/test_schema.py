#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import is_
from hamcrest import none
from hamcrest import assert_that

from nti.schema.field import Int

from nti.ims.qti.schema import ListAttribute
from nti.ims.qti.schema import FloatOrVariableRefAttribute
from nti.ims.qti.schema import IntegerOrVariableRefAttribute

from nti.ims.tests import IMSTestCase

class TestQTISchema(IMSTestCase):

	def test_special(self):		
		s = IntegerOrVariableRefAttribute(title='foo')
		assert_that(s.fromUnicode('1'), is_(1))
		assert_that(s.fromUnicode('val'), is_('val'))
		
		s = FloatOrVariableRefAttribute(title='foo')
		assert_that(s.fromUnicode('2.4'), is_(2.4))
		assert_that(s.fromUnicode('val'), is_('val'))
		assert_that(s.fromUnicode(None), is_(none()))
		
		s = ListAttribute(title='foo', value_type=Int(title='the value'))
		assert_that(s.fromUnicode('1'), is_([1]))
		assert_that(s.fromUnicode('1 2 3'), is_([1, 2, 3]))
		
		try:
			s.fromUnicode('1 2 x')
			self.fail("allowed invalid value")
		except:
			pass
		
		assert_that(s.toUnicode('1'), is_('1'))
		assert_that(s.toUnicode([1]), is_('1'))
		assert_that(s.toUnicode([1, 2, 3]), is_('1 2 3'))
		assert_that(s.toUnicode(None), is_(none()))

