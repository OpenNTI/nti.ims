#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import not_none
from hamcrest import assert_that
from hamcrest import has_property

from zope import component

from nti.ims.lti.interfaces import IOAuthConsumer

import nti.testing.base


ZCML_STRING = u"""
<configure	xmlns="http://namespaces.zope.org/zope"
			xmlns:i18n="http://namespaces.zope.org/i18n"
			xmlns:zcml="http://namespaces.zope.org/zcml"
			xmlns:lti="http://nextthought.com/ntp/lti">

	<include package="zope.component" file="meta.zcml" />
	<include package="zope.security" file="meta.zcml" />
	<include package="zope.component" />
	<include package="." file="meta.zcml" />

	<configure>
		<lti:registerLTIConsumer 	key="foo.bar.com"
									secret="FhodCgoSGxoKCh8RCi4="
									title="Global foo.bar.com" />
	</configure>
</configure>
"""


class TestZcml(nti.testing.base.ConfiguringTestBase):

    def test_registration(self):
        self.configure_string(ZCML_STRING)
        consumer = component.queryUtility(IOAuthConsumer, name='foo.bar.com')
        assert_that(consumer, not_none())
        assert_that(consumer, has_property('key', "foo.bar.com"))
        assert_that(consumer, has_property('secret', "sssssshhhhhhhh"))
        assert_that(consumer, has_property('title', "Global foo.bar.com"))
