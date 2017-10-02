#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import is_
from hamcrest import none
from hamcrest import has_length
from hamcrest import assert_that

from nti.testing.matchers import validly_provides
from nti.testing.matchers import verifiably_provides

import fudge
import unittest

from nti.ims.sis.person import DEFAULT_ROLE

from nti.ims.sis.person import Person
from nti.ims.sis.person import Persons

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
    
    def test_model(self):
        sid = SourcedID(source=u"SIS", id=u"ichigo")
        ichigo = Person(sourcedid=sid,
                        userid=u"ichigo",
                        name=u"Ichigo",
                        email=u"ichigo@bleach.org",
                        userrole=DEFAULT_ROLE)
        
        sid = SourcedID(source=u"SIS", id=u"aizen")
        aizen = Person(sourcedid=sid,
                        userid=u"aizen",
                        name=u"Aizen",
                        email=u"aizen@bleach.org",
                        userrole=DEFAULT_ROLE)
        assert_that(aizen.__lt__(ichigo), is_(True))
        assert_that(ichigo.__gt__(aizen), is_(True))
        
        e = fudge.Fake().provides('find').returns(None)
        assert_that(Person.createFromElement(e), is_(none()))

        persons = Persons()
        persons.add(aizen)
        assert_that(persons, has_length(1))
        del persons[sid]
        assert_that(persons, has_length(0))
