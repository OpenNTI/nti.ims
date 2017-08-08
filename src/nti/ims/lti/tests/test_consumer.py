#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import is_
from hamcrest import has_length
from hamcrest import instance_of
from hamcrest import assert_that

from persistent import Persistent

from nti.app.testing.application_webtest import ApplicationLayerTest

from nti.dataserver.tests import mock_dataserver

from nti.dataserver.tests.mock_dataserver import WithMockDSTrans

from nti.ims.lti.consumer import ConfiguredTool
from nti.ims.lti.consumer import ConfiguredToolContainer
from nti.ims.lti.consumer import PersistentToolConfig


KWARGS = {u'consumer_key': u'test_key',
          u'secret': u'test_secret',
          u'title': u'fake_title',
          u'description': u'test_desc',
          u'launch_url': u'test_url.com',
          u'secure_launch_url': u'secure_test_url.com'
          }

XML = u"""<xml>
            <title>Test Config</title>
            <description>A Test Config</description>
            <launch_url>http://testconfig.com</launch_url>
            <secure_launch_url>https://testconfig.com</secure_launch_url>
         </xml>
      """


class TestConsumer(ApplicationLayerTest):

    @WithMockDSTrans
    def test_configured_tool_container(self):

        transaction = mock_dataserver.current_transaction
        tools = ConfiguredToolContainer()
        transaction.add(tools)

        tool = ConfiguredTool(**KWARGS)

        tools.add_tool(tool)
        assert_that(tools, has_length(1))

        tool = tools[tool]
        assert_that(tools, has_length(1))

        tools.delete_tool(tool)
        assert_that(tools, has_length(0))

        tool = ConfiguredTool(**KWARGS)
        tools.add_tool(tool)
        assert_that(tools, has_length(1))
        tools.delete_tool(tool.__name__)
        assert_that(tools, has_length(0))

    def test_persistent_tool_config(self):

        ptc = PersistentToolConfig(**KWARGS)

        assert_that(ptc.title, is_(KWARGS[u'title']))
        assert_that(ptc.description, is_(KWARGS[u'description']))
        assert_that(ptc.launch_url, is_(KWARGS[u'launch_url']))
        assert_that(ptc.secure_launch_url, is_(KWARGS[u'secure_launch_url']))

        ptc = PersistentToolConfig.create_from_xml(XML)

        assert_that(ptc.title, is_('Test Config'))
        assert_that(ptc.description, is_('A Test Config'))
        assert_that(ptc.launch_url, is_('http://testconfig.com'))
        assert_that(ptc.secure_launch_url, is_('https://testconfig.com'))

        assert_that(ptc, instance_of(Persistent))

    def test_configured_tool(self):

        tool = ConfiguredTool(**KWARGS)
        config = PersistentToolConfig(**KWARGS)
        tool.config = config

        assert_that(tool.title, is_(KWARGS[u'title']))
        assert_that(tool.description, is_(KWARGS[u'description']))
        assert_that(tool.launch_url, is_(KWARGS[u'launch_url']))
        assert_that(tool.secure_launch_url, is_(KWARGS[u'secure_launch_url']))
        assert_that(tool.consumer_key, is_(KWARGS[u'consumer_key']))
        assert_that(tool.secret, is_(KWARGS[u'secret']))
