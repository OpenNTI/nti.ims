#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# pylint: disable=protected-access,too-many-public-methods

from hamcrest import is_
from hamcrest import none
from hamcrest import is_not
from hamcrest import has_length
from hamcrest import assert_that
from hamcrest import instance_of
from hamcrest import has_properties

from nti.testing.time import time_monotonically_increases

import time
import pickle
import unittest

import transaction

import ZODB.MappingStorage

from persistent import Persistent

from nti.ims.lti.consumer import _ConfiguredToolExternalizer
from nti.ims.lti.consumer import ConfiguredTool
from nti.ims.lti.consumer import PersistentToolConfig
from nti.ims.lti.consumer import ConfiguredToolContainer

from nti.ims.tests import SharedConfiguringTestLayer

KWARGS = {
    'consumer_key': u'test_key',
    'secret': u'test_secret',
    'title': u'Test Config',
    'description': u'A Test Config',
    'launch_url': u'http://testconfig.com',
    'secure_launch_url': u'https://testconfig.com'
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

    @time_monotonically_increases
    def test_persistent_tool_config(self):
        # Test properties
        ptc = PersistentToolConfig(**KWARGS)
        assert_that(ptc,
                    has_properties('title', is_(KWARGS['title']),
                                   'description', is_(KWARGS['description']),
                                   'launch_url', is_(KWARGS['launch_url']),
                                   'secure_launch_url', is_(KWARGS['secure_launch_url'])))

        # Test pickling
        ptc_dump = pickle.dumps(ptc)
        ptc_unpickled = pickle.loads(ptc_dump)
        assert_that(ptc_unpickled,
                    has_properties('title', is_(KWARGS['title']),
                                   'description', is_(KWARGS['description']),
                                   'launch_url', is_(KWARGS['launch_url']),
                                   'secure_launch_url', is_(KWARGS['secure_launch_url'])))

        # Test creation time
        t = time.time()
        assert_that(ptc.createdTime, is_(t - 1))
        assert_that(ptc_unpickled.createdTime, is_(t - 1))

        # Test ZODB storage and retrieval
        self._assert_zodb_store(ptc)

        # Test XML Creation
        ptc = PersistentToolConfig.create_from_xml(XML)
        assert_that(ptc,
                    has_properties('title', is_(KWARGS['title']),
                                   'description', is_(KWARGS['description']),
                                   'launch_url', is_(KWARGS['launch_url']),
                                   'secure_launch_url', is_(KWARGS['secure_launch_url'])))
        assert_that(ptc, instance_of(Persistent))

        self._assert_zodb_store(ptc)

        ptc = PersistentToolConfig(custom_params={}, extensions={})
        ptc.set_custom_param('key', 'val')
        ptc.set_ext_param('ext_key', 'key', 'val')
        ptc.set_ext_params('ext_key', {'key': 'val'})

    def _assert_zodb_store(self, ptc):
        db = ZODB.DB(ZODB.MappingStorage.MappingStorage())
        conn = db.open()
        conn.root.config = ptc
        transaction.commit()
        conn.close()
        # Minimize the cache to force retrieval from storage
        db.cacheMinimize()
        conn = db.open()
        stored_ptc = conn.root.config
        assert_that(stored_ptc,
                    has_properties('title', is_(KWARGS['title']),
                                   'description', is_(KWARGS['description']),
                                   'launch_url', is_(KWARGS['launch_url']),
                                   'secure_launch_url', is_(KWARGS['secure_launch_url'])))

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

    def test_configured_tool_externalization(self):
        config = PersistentToolConfig(**KWARGS)
        tool = ConfiguredTool(**KWARGS)
        tool.config = config
        externalizer = _ConfiguredToolExternalizer(tool)
        ext_tool = externalizer.toExternalObject()
        assert_that(ext_tool['title'], is_(KWARGS['title']))
        assert_that(ext_tool['description'], is_(KWARGS['description']))
        assert_that(ext_tool['consumer_key'], is_(KWARGS['consumer_key']))
        assert_that(ext_tool['launch_url'], is_(KWARGS['launch_url']))
        assert_that(ext_tool['secure_launch_url'], is_(KWARGS['secure_launch_url']))
        # Check that config and secret do not exist
        # pylint: disable=pointless-statement
        with self.assertRaises(KeyError) as context:
            ext_tool['config']
        assert_that("'config'", is_(str(context.exception)))
        with self.assertRaises(KeyError) as context:
            ext_tool['secret']
        assert_that("'secret'", is_(str(context.exception)))

    def test_container(self):
        tool = PersistentToolConfig(**KWARGS)
        container = ConfiguredToolContainer()
        container.add_tool(tool)
        assert_that(container, has_length(1))
        assert_that(tool, has_properties('__name__', is_not(none())))
        assert_that(container[tool], is_not(none()))
        container.delete_tool(tool)
        assert_that(container, has_length(0))
