#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division

__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from hamcrest import assert_that
from hamcrest import  has_length

from lti.tool_config import ToolConfig

from zope.component import queryUtility
from zope import interface

from nti.ims.lti.interfaces import IConfiguredTool
from nti.ims.lti.interfaces import IConfiguredTools

from nti.testing.matchers import verifiably_provides

import nti.testing.base


ZCML_STRING = """<configure	xmlns="http://namespaces.zope.org/zope"
			                xmlns:i18n="http://namespaces.zope.org/i18n"
			                xmlns:zcml="http://namespaces.zope.org/zcml">

	                        <include package="zope.component" file="meta.zcml" />
	                        <include package="zope.component" />

                            <utility factory=".oauth.UtilityBackedOAuthConsumers"
                                     provides=".interfaces.IOAuthConsumers"/>
                        
                            <utility factory="nti.containers.containers.CaseInsensitiveLastModifiedBTreeContainer"
                                     provides=".interfaces.IConfiguredTools" />
                        
                            <adapter factory=".config.ToolConfigFactory"
                                     provides=".interfaces.IToolConfigFactory"
                                     for=".interfaces.ITool" />
                        
                            <adapter factory=".consumer.ConfiguredTool"
                                     provides=".interfaces.IConfiguredTool"
                                     for="pyramid.interfaces.IRequest" />
                        
                        </configure>"""


@interface.implementer(IConfiguredTool)
class TestConfiguredTool(object):

    key = u'test_key'
    secret = u'test_secret'
    params = {u'test': u'param',
              u'fake': u'param'}
    title = u'fake_title'
    description = u'test_desc'
    config = ToolConfig()


class TestConsumer(nti.testing.base.ConfiguringTestBase):

    def test_configured_tools(self):

        self.configure_string(ZCML_STRING)

        tools = queryUtility(IConfiguredTools)
        # assert_that(tools, verifiably_provides(IConfiguredTools))

        tool = TestConfiguredTool()
        assert_that(tool, verifiably_provides(IConfiguredTool))

        tools[tool.title] = tool

        tool = tools[tool.title]
        assert_that(tool, verifiably_provides(IConfiguredTool))

        tools = queryUtility(IConfiguredTools)
        tool = tools[tool.title]
        assert_that(tool, verifiably_provides(IConfiguredTool))
        assert_that(tools, has_length(1))
