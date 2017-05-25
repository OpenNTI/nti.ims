#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import assert_that

from nti.testing.matchers import validly_provides
from nti.testing.matchers import verifiably_provides

import unittest

from nti.ims.sis.person import DEFAULT_ROLE

from nti.ims.sis.person import Person

from nti.ims.sis.interfaces import IPerson

from nti.ims.sis.sourcedid import SourcedID

from nti.ims.tests import SharedConfiguringTestLayer


class TestPerson(unittest.TestCase):
    
    layer = SharedConfiguringTestLayer
    
    def test_interface(self):
        sid = SourcedID(source=u"SIS", id=u"112133307")
        person = Person(sourcedid=sid,
                        userid=u"maletas",
                        name=u"Ichigo",
                        email=u"ichigo@bleach.org",
                        userrole=DEFAULT_ROLE)
        assert_that(person, validly_provides(IPerson))
        assert_that(person, verifiably_provides(IPerson))