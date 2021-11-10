#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# pylint: disable=protected-access,too-many-public-methods
from collections import defaultdict

from hamcrest import is_
from hamcrest import none
from hamcrest import is_not
from hamcrest import has_length
from hamcrest import assert_that
from hamcrest import instance_of
from hamcrest import has_properties

import pickle
import unittest

import transaction

import ZODB.MappingStorage

from persistent import Persistent

from nti.externalization.internalization import update_from_external_object

from nti.ims.lti.consumer import ConfiguredTool
from nti.ims.lti.consumer import PersistentToolConfig
from nti.ims.lti.consumer import ConfiguredToolContainer

from nti.ims.lti.externalization import _ConfiguredToolExternalizer

from nti.ims.lti.interfaces import IDeepLinking
from nti.ims.lti.interfaces import IExternalToolLinkSelection

from nti.ims.tests import SharedConfiguringTestLayer

from nti.testing.matchers import validly_provides
from nti.testing.matchers import verifiably_provides


KWARGS = {
    'consumer_key': u'test_key',
    'secret': u'test_secret',
    'title': u'Test Config',
    'description': u'A Test Config',
    'launch_url': u'http://testconfig.com',
    'secure_launch_url': u'https://testconfig.com'
}

EXTERNAL_TOOL_LINK_SELECTION_XML = u"""<cartridge_basiclti_link xmlns="http://www.imsglobal.org/xsd/imslticc_v1p0" xmlns:blti="http://www.imsglobal.org/xsd/imsbasiclti_v1p0" xmlns:lticm="http://www.imsglobal.org/xsd/imslticm_v1p0" xmlns:lticp="http://www.imsglobal.org/xsd/imslticp_v1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imslticc_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticc_v1p0.xsd http://www.imsglobal.org/xsd/imsbasiclti_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imsbasiclti_v1p0p1.xsd http://www.imsglobal.org/xsd/imslticm_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticm_v1p0.xsd http://www.imsglobal.org/xsd/imslticp_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticp_v1p0.xsd">
<blti:title>Test Config</blti:title>
<blti:description>A Test Config</blti:description>
<blti:launch_url>http://testconfig.com</blti:launch_url>
<blti:secure_launch_url>https://testconfig.com</blti:secure_launch_url>
<blti:icon>https://www.edu-apps.org/assets/lti_public_resources/vimeo_icon.png</blti:icon>
<blti:extensions platform="canvas.instructure.com">
<lticm:property name="domain">test.org</lticm:property>
<lticm:options name="editor_button">
<lticm:property name="enabled">true</lticm:property>
</lticm:options>
<lticm:property name="icon_url">https://www.edu-apps.org/assets/lti_public_resources/vimeo_icon.png</lticm:property>
<lticm:property name="privacy_level">anonymous</lticm:property>
<lticm:options name="resource_selection">
<lticm:property name="enabled">true</lticm:property>
</lticm:options>
<lticm:property name="selection_height">600</lticm:property>
<lticm:property name="selection_width">560</lticm:property>
<lticm:property name="tool_id">test</lticm:property>
</blti:extensions>
</cartridge_basiclti_link>"""

DEEP_LINKING_XML = u"""
<cartridge_basiclti_link xmlns="https://www.imsglobal.org/xsd/imslticc_v1p0" xmlns:blti="https://www.imsglobal.org/xsd/imsbasiclti_v1p0" xmlns:lticm="https://www.imsglobal.org/xsd/imslticm_v1p0" xmlns:lticp="https://www.imsglobal.org/xsd/imslticp_v1p0" xmlns:xsi="https://www.w3.org/2001/XMLSchema-instance" xsi:schemalocation="https://www.imsglobal.org/xsd/imslticc_v1p0 https://www.imsglobal.org/xsd/lti/ltiv1p0/imslticc_v1p0.xsd https://www.imsglobal.org/xsd/imsbasiclti_v1p0 https://www.imsglobal.org/xsd/lti/ltiv1p0/imsbasiclti_v1p0p1.xsd https://www.imsglobal.org/xsd/imslticm_v1p0 https://www.imsglobal.org/xsd/lti/ltiv1p0/imslticm_v1p0.xsd https://www.imsglobal.org/xsd/imslticp_v1p0 https://www.imsglobal.org/xsd/lti/ltiv1p0/imslticp_v1p0.xsd">
<blti:title>Codio</blti:title>
<blti:description>Platform for teaching computer science and Math</blti:description>
<blti:launch_url> https://apollo.codio.com/lti </blti:launch_url>
<blti:icon>https://codio.com/favicon-16x16-e0ed56f7.png</blti:icon>
<blti:custom/>
<blti:extensions platform="canvas.instructure.com">
<lticm:property name="tool_id">codio</lticm:property>
<lticm:property name="icon_url">https://codio.com/favicon-16x16-e0ed56f7.png</lticm:property>
<lticm:property name="domain">codio.com</lticm:property>
<lticm:property name="privacy_level">public</lticm:property>
<lticm:property name="selection_width">800</lticm:property>
<lticm:property name="selection_height">600</lticm:property>
<lticm:property name="text">Codio</lticm:property>
<lticm:options name="editor_button">
<lticm:property name="message_type">ContentItemSelectionRequest</lticm:property>
<lticm:property name="enabled">true</lticm:property>
<lticm:property name="url">https://apollo.codio.com/lti/editor_button</lticm:property>
<lticm:property name="text">Codio</lticm:property>
<lticm:property name="icon_url">https://codio.com/favicon-16x16-e0ed56f7.png</lticm:property>
<lticm:property name="selection_width">900</lticm:property>
<lticm:property name="selection_height">600</lticm:property>
</lticm:options>
<lticm:options name="resource_selection">
<lticm:property name="message_type">ContentItemSelectionRequest</lticm:property>
<lticm:property name="enabled">true</lticm:property>
<lticm:property name="url">https://apollo.codio.com/lti/resource_selection</lticm:property>
<lticm:property name="text">Codio</lticm:property>
<lticm:property name="icon_url">https://codio.com/favicon-16x16-e0ed56f7.png</lticm:property>
<lticm:property name="selection_width">900</lticm:property>
<lticm:property name="selection_height">600</lticm:property>
</lticm:options>
<lticm:options name="course_navigation">
<lticm:property name="enabled"/>
<lticm:property name="url">https://apollo.codio.com/lti/course_navigation</lticm:property>
<lticm:property name="text">Codio</lticm:property>
<lticm:property name="visibility">public</lticm:property>
</lticm:options>
</blti:extensions>
</cartridge_basiclti_link>"""


class TestConsumer(unittest.TestCase):

    layer = SharedConfiguringTestLayer

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
        assert_that(ptc.createdTime, is_(ptc_unpickled.createdTime))

        # Test ZODB storage and retrieval
        self._assert_zodb_store(ptc)

        # Test XML Creation
        ptc = PersistentToolConfig.create_from_xml(EXTERNAL_TOOL_LINK_SELECTION_XML)
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
        config = PersistentToolConfig.create_from_xml(EXTERNAL_TOOL_LINK_SELECTION_XML)
        tool.config = config
        assert_that(tool,
                    has_properties('title', is_(KWARGS['title']),
                                   'description', is_(KWARGS['description']),
                                   'launch_url', is_(KWARGS['launch_url']),
                                   'secure_launch_url', is_(KWARGS['secure_launch_url']),
                                   'consumer_key', is_(KWARGS['consumer_key']),
                                   'secret', is_(KWARGS['secret'])))

    def test_configured_tool_internalization(self):
        # Test normal case with no extensions
        config = PersistentToolConfig(**KWARGS)
        parsed = {'consumer_key': u'Test_Consumer_Key',
                  'secret': u'Test_Secret',
                  'config': config}
        tool = ConfiguredTool()
        update_from_external_object(tool, parsed)
        assert_that(tool.extensions, has_length(0))

        # Test normal case with External Tool Link Selection extensions
        config = PersistentToolConfig.create_from_xml(EXTERNAL_TOOL_LINK_SELECTION_XML)
        parsed = {'consumer_key': u'Test_Consumer_Key',
                  'secret': u'Test_Secret',
                  'config': config}
        tool = ConfiguredTool()
        update_from_external_object(tool, parsed)
        assert_that(tool.extensions, has_length(2))
        for extension in tool.extensions:
            assert_that(extension.enabled, is_(True))
            assert_that(extension.selection_height, is_(400))
            assert_that(extension.selection_width, is_(500))
            assert_that(extension, verifiably_provides(IExternalToolLinkSelection))
            assert_that(extension, validly_provides(IExternalToolLinkSelection))

        # Test normal case with Deep Linking
        config = PersistentToolConfig.create_from_xml(DEEP_LINKING_XML)
        parsed = {'consumer_key': u'Test_Consumer_Key',
                  'secret': u'Test_Secret',
                  'config': config}
        tool = ConfiguredTool()
        update_from_external_object(tool, parsed)
        assert_that(tool.extensions, has_length(2))
        for extension in tool.extensions:
            assert_that(extension.enabled, is_(True))
            assert_that(extension.selection_height, is_(600))
            assert_that(extension.selection_width, is_(900))
            assert_that(extension, verifiably_provides(IDeepLinking))
            assert_that(extension, validly_provides(IDeepLinking))
            assert_that(extension.text, is_(u'Codio'))
            assert_that(extension.icon_url, is_(u'https://codio.com/favicon-16x16-e0ed56f7.png'))

        # Test import case with External Tool Link Selection extensions
        parsed = {'consumer_key': u'Test_Consumer_Key',
                  'secret': u'Test_Secret',
                  'config_xml': EXTERNAL_TOOL_LINK_SELECTION_XML
                  }
        tool = ConfiguredTool()
        update_from_external_object(tool, parsed)
        assert_that(tool.extensions, has_length(2))
        for extension in tool.extensions:
            assert_that(extension.enabled, is_(True))
            assert_that(extension.selection_height, is_(400))
            assert_that(extension.selection_width, is_(500))
            assert_that(extension, verifiably_provides(IExternalToolLinkSelection))
            assert_that(extension, validly_provides(IExternalToolLinkSelection))

        # Test import case with Deep Linking
        config = PersistentToolConfig.create_from_xml(DEEP_LINKING_XML)
        parsed = {'consumer_key': u'Test_Consumer_Key',
                  'secret': u'Test_Secret',
                  'config': config}
        tool = ConfiguredTool()
        update_from_external_object(tool, parsed)
        assert_that(tool.extensions, has_length(2))
        for extension in tool.extensions:
            assert_that(extension.enabled, is_(True))
            assert_that(extension.selection_height, is_(600))
            assert_that(extension.selection_width, is_(900))
            assert_that(extension, verifiably_provides(IDeepLinking))
            assert_that(extension, validly_provides(IDeepLinking))
            assert_that(extension.text, is_(u'Codio'))
            assert_that(extension.icon_url, is_(u'https://codio.com/favicon-16x16-e0ed56f7.png'))

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
        config = PersistentToolConfig(**KWARGS)
        tool = ConfiguredTool(**KWARGS)
        tool.config = config
        tool.ntiid = 'test'
        container = ConfiguredToolContainer()
        container.add_tool(tool)
        assert_that(container, has_length(1))
        assert_that(container[tool], is_not(none()))
        container.delete_tool(tool)
        assert_that(container, has_length(0))

    def test_internal_access(self):
        config = PersistentToolConfig(**KWARGS)
        base_dict = defaultdict(lambda: None)

        assert_that(config.extensions, is_(base_dict))
        assert_that(config.custom_params, is_(base_dict))
        assert_that(config.get_ext_params('test'), is_(None))
        assert_that(config.get_ext_param('test_ext_key', 'test_param_key'), is_(None))
        assert_that(config.get_custom_param('test'), is_(None))
        assert_that(config.extensions, is_(base_dict))
        assert_that(config.custom_params, is_(base_dict))

        config.set_ext_params('test_key', {})
        assert_that(config.get_ext_params('test_key'), is_({}))
        config.set_ext_param('test_key', 'test_param', 'test')
        config.set_custom_param('test_key', 'test_param')
        assert_that(config.get_ext_params('test_key'), is_({'test_param': 'test'}))
        assert_that(config.get_ext_param('test_key', 'test_param'), is_('test'))
        assert_that(config.get_custom_param('test_key'), is_('test_param'))

        config.set_ext_params('test_key', {})
        assert_that(config.get_ext_params('test_key'), is_({}))
        config.set_custom_param('test_key', 'new_test_param')
        config.set_ext_param('test_key', 'test_param', 'new_test')
        assert_that(config.get_ext_params('test_key'), is_({'test_param': 'new_test'}))
        assert_that(config.get_ext_param('test_key', 'test_param'), is_('new_test'))
        assert_that(config.get_custom_param('test_key'), is_('new_test_param'))
