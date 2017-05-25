#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import is_
from hamcrest import is_in
from hamcrest import has_length
from hamcrest import assert_that
from hamcrest import has_property

from nti.testing.matchers import validly_provides
from nti.testing.matchers import verifiably_provides

import unittest

from nti.ims.sis.membership import STUDENT_ROLE
from nti.ims.sis.membership import ACTIVE_STATUS

from nti.ims.sis.membership import Role
from nti.ims.sis.membership import Member
from nti.ims.sis.membership import Membership

from nti.ims.sis.interfaces import IRole
from nti.ims.sis.interfaces import IMember
from nti.ims.sis.interfaces import IMembership

from nti.ims.sis.sourcedid import SourcedID

from nti.ims.tests import SharedConfiguringTestLayer


class TestMembership(unittest.TestCase):

    layer = SharedConfiguringTestLayer

    def test_interface(self):
        role = Role(userid=u"ichigo",
                    datasource=u"sis",
                    status=ACTIVE_STATUS,
                    roletype=STUDENT_ROLE)
        assert_that(role, validly_provides(IRole))
        assert_that(role, verifiably_provides(IRole))

        sid = SourcedID(source=u"SIS", id=u"112133307")
        member = Member(sourcedid=sid,
                        idtype=1,
                        role=role)
        assert_that(member, validly_provides(IMember))
        assert_that(member, verifiably_provides(IMember))

        assert_that(member, has_property('userid', is_("ichigo")))
        assert_that(member, has_property('is_active', is_(True)))
        assert_that(member, has_property('is_student', is_(True)))
        assert_that(member, has_property('is_instructor', is_(False)))
        assert_that(member, has_property('status', is_(ACTIVE_STATUS)))
        assert_that(member, has_property('roletype', is_(STUDENT_ROLE)))

        mid = SourcedID(source=u"SIS", id=u"112133307")
        membership = Membership(sourcedid=mid)
        assert_that(membership, validly_provides(IMembership))
        assert_that(membership, verifiably_provides(IMembership))

        membership.add(member)
        assert_that(membership, has_length(1))
        assert_that(list(membership), has_length(1))
        assert_that(membership.index(member), is_(0))
        assert_that(membership[0], is_(member))

        assert_that(member, is_in(membership))
        assert_that(member, has_property('__parent__', is_(membership)))

        del membership[0]
        assert_that(membership, has_length(0))

        membership += membership
        assert_that(membership, has_length(0))
