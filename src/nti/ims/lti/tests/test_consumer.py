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

from nti.ims.lti.consumer import ConfiguredToolContainer

from nti.ims.lti.interfaces import IConfiguredTool
from nti.ims.lti.interfaces import IConfiguredToolContainer

from nti.testing.matchers import verifiably_provides

import nti.testing.base


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

        tools = ConfiguredToolContainer()
        assert_that(tools, verifiably_provides(IConfiguredToolContainer))

        tool = TestConfiguredTool()
        assert_that(tool, verifiably_provides(IConfiguredTool))

        tools.add_tool(tool)

        tool = tools.get_tool(tool.title)
        assert_that(tool, verifiably_provides(IConfiguredTool))
        assert_that(tools, has_length(1))

        tools.delete_tool(tool.title)
        assert_that(tools, has_length(0))
