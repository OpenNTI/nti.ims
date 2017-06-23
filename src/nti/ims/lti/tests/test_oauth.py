#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import raises
from hamcrest import calling
from hamcrest import not_none
from hamcrest import assert_that
from hamcrest import has_property

import unittest

from zope import component

from nti.ims.lti.interfaces import IOAuthConsumers

from nti.ims.lti.oauth import OAuthConsumer

from nti.ims.tests import SharedConfiguringTestLayer


class TestConsumerRegistration(unittest.TestCase):

    layer = SharedConfiguringTestLayer

    def test_utility(self):
        keys = component.getUtility(IOAuthConsumers)
        assert_that(keys, not_none())

    def test_registrations(self):
        keys = component.getUtility(IOAuthConsumers)

        assert_that(calling(keys.__getitem__).with_args('foo'),
                    raises(KeyError))

        consumer = OAuthConsumer(key=u'foo',
                                 secret=u'secret',
                                 title=u'foobar')
        keys[consumer.key] = consumer
        assert_that(keys['foo'], has_property('secret', consumer.secret))

        consumer.key = u'bad'
        assert_that(calling(keys.__setitem__).with_args('foo', consumer),
                    raises(ValueError))

        del keys['foo']

        assert_that(calling(keys.__getitem__).with_args('foo'),
                    raises(KeyError))
