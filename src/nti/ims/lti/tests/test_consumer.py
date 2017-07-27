#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division

__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from hamcrest import assert_that
from hamcrest import  has_length

import unittest

from nti.ims.lti.consumer import ConfiguredTool
from nti.ims.lti.consumer import ConfiguredToolContainer

from nti.ims.lti.interfaces import IConfiguredTool
from nti.ims.lti.interfaces import IConfiguredToolContainer

from nti.ims.tests import SharedConfiguringTestLayer

from nti.testing.matchers import verifiably_provides


KWARGS = {u'key': u'test_key',
          u'secret': u'test_secret',
          u'title': u'fake_title',
          u'description': u'test_desc'
          }


class TestConsumer(unittest.TestCase):

    layer = SharedConfiguringTestLayer

    def test_configured_tools(self):

        tools = ConfiguredToolContainer()
        assert_that(tools, verifiably_provides(IConfiguredToolContainer))

        tool = ConfiguredTool(**KWARGS)
        assert_that(tool, verifiably_provides(IConfiguredTool))

        tools.add_tool(tool)
        assert_that(tools, has_length(1))

        tool = tools[tool]
        assert_that(tools, has_length(1))
        assert_that(tool, verifiably_provides(IConfiguredTool))

        tools.delete_tool(tool)
        assert_that(tools, has_length(0))

        tool = ConfiguredTool(**KWARGS)
        tools.add_tool(tool)
        assert_that(tools, has_length(1))
        tools.delete_tool(tool.__name__)
        assert_that(tools, has_length(0))
