#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import assert_that

from nti.testing.matchers import validly_provides
from nti.testing.matchers import verifiably_provides

import unittest

from nti.ims.sis.group import Group
from nti.ims.sis.group import TimeFrame

from nti.ims.sis.interfaces import IGroup
from nti.ims.sis.interfaces import ITimeFrame

from nti.ims.sis.sourcedid import SourcedID

from nti.ims.tests import SharedConfiguringTestLayer


class TestGroup(unittest.TestCase):
    
    layer = SharedConfiguringTestLayer
    
    def test_interface(self):
        sid = SourcedID(source=u"SIS", id=u"112133307")
        tm = TimeFrame(start=100, end=200)
        assert_that(tm, validly_provides(ITimeFrame))
        assert_that(tm, verifiably_provides(ITimeFrame))
        
        group = Group(type=u"type",
                      level=u'level',
                      sourcedid=sid,
                      timeframe=tm,
                      description=u"my group")
        assert_that(group, validly_provides(IGroup))
        assert_that(group, verifiably_provides(IGroup))
