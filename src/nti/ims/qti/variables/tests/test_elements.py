#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import is_
from hamcrest import none
from hamcrest import not_none
from hamcrest import has_entry
from hamcrest import assert_that
from hamcrest import has_property

from nti.externalization import internalization
from nti.externalization.externalization import toExternalObject

from nti.ims.qti.variables import interfaces
from nti.ims.qti.variables.elements import Value

from nti.testing.matchers import verifiably_provides

from nti.ims.tests import IMSTestCase

class TestVariablesElements(IMSTestCase):
	
	def test_value(self):
		v = Value(fieldIdentifier="foo", baseType="float")
		assert_that(v, verifiably_provides(interfaces.Ivalue))
		
		ext_obj = toExternalObject(v)
		assert_that(ext_obj, has_entry('Class', 'Value'))
		assert_that(ext_obj, has_entry('baseType', 'float'))
		assert_that(ext_obj, has_entry('content', is_(none())))
		assert_that(ext_obj, has_entry('fieldIdentifier', 'foo'))
		assert_that(ext_obj, has_entry('MimeType', 'application/vnd.nextthought.qti.value'))
		
		factory = internalization.find_factory_for(ext_obj)
		assert_that(factory, is_(not_none()))

		new_io = factory()
		internalization.update_from_external_object(new_io, ext_obj)
		assert_that(new_io, has_property('content', is_(none())))
		assert_that(new_io, has_property('baseType', is_('float')))
		assert_that(new_io, has_property('fieldIdentifier', is_('foo')))
