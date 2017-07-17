#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
sheldon.smith
7/17/17

"""

from __future__ import print_function, absolute_import, division

__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from hamcrest import is_
from hamcrest import assert_that
from nti.testing.matchers import verifiably_provides

from zope import interface

from nti.ims.lti.config import ToolConfigFactory

from nti.ims.lti.interfaces import IToolConsumerInstance

import nti.testing.base




@interface.implementer(IToolConsumerInstance)
class FakeToolConsumerInstance(object):

    user_id = u'A fake user'

    context_type = ['fake_context', 'more_fake_context', 'most_fake_context']

    presentation_target = u'http://fakeurl.com'

    presentation_width = 12345

    custom_values = {'fake' : 0, 'pretend' : 1}


class TestConfigFactory(nti.testing.base.ConfiguringTestBase):

    def test_basic_attributes(self):
        tool = FakeToolConsumerInstance()

        # test textline field
        assert_that(tool.user_id, is_(tool.user_id))

        # test list field
        assert_that(tool.context_type, is_(tool.context_type))
        assert_that(len(tool.context_type), is_(3))
        assert_that(tool.context_type[0], is_(tool.context_type[0]))

        # test URL field
        assert_that(tool.presentation_target, is_(tool.presentation_target))

        # test number field
        assert_that(tool.presentation_width, is_(12345))

        # test dict field
        assert_that(tool.custom_values['fake'], is_(tool.custom_values['fake']))
        assert_that(len(tool.custom_values), is_(2))
