#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# pylint: disable=protected-access,too-many-public-methods,arguments-differ

from zope import component

from zope.component.hooks import setHooks

from nti.testing.layers import GCLayerMixin
from nti.testing.layers import ZopeComponentLayer
from nti.testing.layers import ConfiguringLayerMixin

import zope.testing.cleanup


class SharedConfiguringTestLayer(GCLayerMixin,
                                 ZopeComponentLayer,
                                 ConfiguringLayerMixin):

    set_up_packages = ('nti.ims',)

    @classmethod
    def setUp(cls):
        cls.setUpPackages()

    @classmethod
    def tearDown(cls):
        cls.tearDownPackages()
        zope.testing.cleanup.cleanUp()

    @classmethod
    def testSetUp(cls, unused_test=None):
        setHooks()

    @classmethod
    def testTearDown(cls):
        pass

import unittest


class IMSTestCase(unittest.TestCase):
    layer = SharedConfiguringTestLayer
