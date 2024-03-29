#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# pylint: disable=protected-access,too-many-public-methods

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
			xmlns:ims="http://nextthought.com/ntp/ims">

	<include package="zope.component" file="meta.zcml" />
	<include package="zope.security" file="meta.zcml" />
	<include package="zope.component" />
	<include package="." file="meta.zcml" />

	<configure>
		<ims:registerLTIConsumer 	key="foo.bar.com"
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
