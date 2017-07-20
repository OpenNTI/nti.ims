#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904


from hamcrest import is_
from hamcrest import assert_that

from nti.testing.matchers import verifiably_provides

from zope import interface

from nti.ims.lti.config import ToolConfigFactory

from nti.ims.lti.interfaces import ITool
from nti.ims.lti.interfaces import IToolConfig
from nti.ims.lti.interfaces import IToolConfigBuilder

import nti.testing.base


ZCML_STRING = u"""
<configure	xmlns="http://namespaces.zope.org/zope"
			xmlns:i18n="http://namespaces.zope.org/i18n"
			xmlns:zcml="http://namespaces.zope.org/zcml"
			xmlns:ims="http://nextthought.com/ntp/lti">

	<include package="zope.component" file="meta.zcml" />
	<include package="zope.security" file="meta.zcml" />
	<include package="zope.component" />
	<include package="." file="meta.zcml" />

	<configure>
		<subscriber factory=".tests.test_config.FakeConfigBuilder"
		            for=".tests.test_config.FakeTool"
		            provides=".interfaces.IToolConfigBuilder" />
	</configure>
</configure>
"""


@interface.implementer(ITool)
class FakeTool(object):

    title = u'My fake tool'

    description = u'A fake tool for testing'

    __name__ = title


@interface.implementer(IToolConfigBuilder)
class FakeConfigBuilder(object):

    def __init__(self, tool):
        pass

    def configure(self, config):
        config.set_custom_param('test_key', 'test_value')
        return config


class TestConfigFactory(nti.testing.base.ConfiguringTestBase):

    def test_config_builder(self):
        self.configure_string(ZCML_STRING)
        tool = FakeTool()
        factory = ToolConfigFactory(tool)
        config = factory()
        assert_that(config.get_custom_param('test_key'), is_('test_value'))

    def test_basic_attributes(self):
        tool = FakeTool()
        factory = ToolConfigFactory(tool)
        config = factory()
        assert_that(config.title, is_(tool.title))
        assert_that(config.__name__, is_(tool.__name__))
        assert_that(config.description, is_(tool.description))
        assert_that(config, verifiably_provides(IToolConfig))
