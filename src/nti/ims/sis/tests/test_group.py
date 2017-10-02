#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import is_
from hamcrest import none
from hamcrest import assert_that

from nti.testing.matchers import validly_provides
from nti.testing.matchers import verifiably_provides

import fudge
import unittest

from nti.ims.sis.group import Group
from nti.ims.sis.group import TimeFrame

from nti.ims.sis.interfaces import IGroup
from nti.ims.sis.interfaces import ITimeFrame

from nti.ims.sis.sourcedid import SourcedID

from nti.ims.tests import SharedConfiguringTestLayer


class TestGroup(unittest.TestCase):
    
    layer = SharedConfiguringTestLayer
    
    def test_timefram(self):
        tm = TimeFrame(start=100, end=200)
        assert_that(tm, validly_provides(ITimeFrame))
        assert_that(tm, verifiably_provides(ITimeFrame))
        e = fudge.Fake().provides('begin').returns(None)
        e.provides('end').returns(None)
        e.provides('find').returns(None)
        assert_that(TimeFrame.createFromElement(e), is_(none()))
        
    def test_group(self):
        sid = SourcedID(source=u"SIS", id=u"first")
        tm = TimeFrame(start=100, end=200)
        
        first = Group(type=u"type",
                      level=u'level',
                      sourcedid=sid,
                      timeframe=tm,
                      description=u"my group")
        assert_that(first, validly_provides(IGroup))
        assert_that(first, verifiably_provides(IGroup))
        
        sid = SourcedID(source=u"SIS", id=u"second")
        second = Group(type=u"type2",
                       level=u'level2',
                       sourcedid=sid,
                       timeframe=tm,
                       description=u"my second group")
        assert_that(first.__lt__(second), is_(True))
        
        e = fudge.Fake().provides('find').returns(None)
        e.provides('grouptype').returns(None)
        e.provides('description').returns(None)
        e.provides('timeframe').returns(None)
        assert_that(Group.createFromElement(e), is_(none()))
