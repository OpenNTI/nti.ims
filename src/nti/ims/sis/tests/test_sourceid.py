#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import is_
from hamcrest import none
from hamcrest import is_not
from hamcrest import assert_that
from hamcrest import greater_than
from hamcrest import has_property

from nti.testing.matchers import validly_provides
from nti.testing.matchers import verifiably_provides

import fudge
import unittest

from nti.ims.sis.interfaces import ISourcedID

from nti.ims.sis.sourcedid import SourcedID

from nti.ims.tests import SharedConfiguringTestLayer


class TestSourceID(unittest.TestCase):

    layer = SharedConfiguringTestLayer

    def test_interface(self):
        sid = SourcedID(source=u"SIS", id=u"112133307")
        assert_that(sid, validly_provides(ISourcedID))
        assert_that(sid, verifiably_provides(ISourcedID))

    def test_model(self):
        a = SourcedID(source=u"SIS", id=u"112133307")
        assert_that(a, has_property("source", "SIS"))
        assert_that(a, has_property("id", "112133307"))

        b = SourcedID(source=u"SIS", id=u"112133307")
        c = SourcedID(source=u"SIS", id=u"112133443")
        assert_that(a, is_(b))
        assert_that(a, is_not(c))

        assert_that(c, is_(greater_than(a)))

        e = fudge.Fake().provides('find').returns(None)
        assert_that(SourcedID.createFromElement(e), is_(none()))
