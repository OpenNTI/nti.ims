#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import is_
from hamcrest import assert_that
from hamcrest import instance_of
from hamcrest import has_properties

import unittest

from persistent import Persistent

from nti.ims.lti.consumer import ConfiguredTool
from nti.ims.lti.consumer import PersistentToolConfig

from nti.ims.tests import SharedConfiguringTestLayer


KWARGS = {
    'consumer_key': u'test_key',
    'secret': u'test_secret',
    'title': u'fake_title',
    'description': u'test_desc',
    'launch_url': u'test_url.com',
    'secure_launch_url': u'secure_test_url.com'
}

XML = u"""<xml>
            <title>Test Config</title>
            <description>A Test Config</description>
            <launch_url>http://testconfig.com</launch_url>
            <secure_launch_url>https://testconfig.com</secure_launch_url>
         </xml>
      """


class TestConsumer(unittest.TestCase):

    layer = SharedConfiguringTestLayer

    def test_persistent_tool_config(self):

        ptc = PersistentToolConfig(**KWARGS)
        assert_that(ptc, 
                    has_properties('title', is_(KWARGS['title']),
                                   'description', is_(KWARGS['description']),
                                   'launch_url', is_(KWARGS['launch_url']),
                                   'secure_launch_url', is_(KWARGS['secure_launch_url'])))

        ptc = PersistentToolConfig.create_from_xml(XML)
        assert_that(ptc, 
                    has_properties('title', is_('Test Config'),
                                   'description', is_('A Test Config'),
                                   'launch_url', is_('http://testconfig.com'),
                                   'secure_launch_url', is_('https://testconfig.com')))
        assert_that(ptc, instance_of(Persistent))

    def test_configured_tool(self):
        tool = ConfiguredTool(**KWARGS)
        config = PersistentToolConfig(**KWARGS)
        tool.config = config
        assert_that(tool, 
                    has_properties('title', is_(KWARGS['title']),
                                   'description', is_(KWARGS['description']),
                                   'launch_url', is_(KWARGS['launch_url']),
                                   'secure_launch_url', is_(KWARGS['secure_launch_url']),
                                   'consumer_key', is_(KWARGS['consumer_key']),
                                   'secret', is_(KWARGS['secret'])))
