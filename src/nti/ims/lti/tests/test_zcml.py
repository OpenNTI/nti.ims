#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import none
from hamcrest import is_not
from hamcrest import assert_that
from hamcrest import has_property

from zope import component

from nti.ims.lti import interfaces

import nti.testing.base

ZCML_STRING = """
<configure 	xmlns="http://namespaces.zope.org/zope"
			xmlns:zcml="http://namespaces.zope.org/zcml"
			xmlns:lti="http://nextthought.com/ntp/lti"
			i18n_domain='nti.dataserver'>

	<include package="zope.component" />
	<include package="zope.annotation" />
	<include package="z3c.baseregistry" file="meta.zcml" />
	<include package="." file="meta.zcml" />

	<lti:registerConsumer
			 	key="jisc.ac.uk"
			 	secret="secret" />
</configure>
"""

class TestZcml(nti.testing.base.ConfiguringTestBase):

	def test_registration(self):
		self.configure_string(ZCML_STRING)
		consumer = component.queryUtility(interfaces.IConsumer)
		assert_that(consumer, is_not(none()))
		assert_that(consumer, has_property('key', 'jisc.ac.uk'))
		assert_that(consumer, has_property('secret', 'secret'))
		