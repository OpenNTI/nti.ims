#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import is_
from hamcrest import none
from hamcrest import is_not
from hamcrest import has_length
from hamcrest import assert_that
from hamcrest import has_property

import os
import unittest

from nti.ims.sis.enterprise import Enterprise

class TestOSU(unittest.TestCase):
		
	def _parse_1(self, source):
		path = source
		enterprise = Enterprise.parseFile(path)
		assert_that(enterprise, is_not(none()))
		assert_that(enterprise, has_property("persons", has_length(24)))
		p = enterprise.persons.get_by_userid('david.north')
		assert_that(p, is_not(none()))
		assert_that(p, has_property('userid', is_('david.north')))
		assert_that(p, has_property('userrole', is_('01')))
		assert_that(p, has_property('name', is_('David North')))
		assert_that(p, has_property('email', is_('david.north@oc.edu')))
		assert_that(p, has_property('sourcedid', has_property('source', is_('SIS'))))
		assert_that(p, has_property('sourcedid', has_property('id', is_('1004596'))))
		
		groups = list(enterprise.get_groups())
		assert_that(groups, has_length(1))
		group = enterprise.get_group(groups[0].sourcedid)
		assert_that(group, is_not(none()))
		assert_that(group, has_property('type', is_(none())))
		assert_that(group, has_property('level', is_(none())))
		assert_that(group, has_property('description', is_('Software Engr - Introduction 2015FA')))
		assert_that(group, has_property('sourcedid', has_property('source', is_('SIS'))))
		assert_that(group, has_property('sourcedid', has_property('id', is_('2015FA_CMSC-1313-01'))))
		assert_that(group, has_property('timeframe', has_property('end', is_(1450418400.0))))
		assert_that(group, has_property('timeframe', has_property('start', is_(1440997200.0))))

		memberships = list(enterprise.get_memberships())
		assert_that(memberships, has_length(1))
		membership = enterprise.get_membership(memberships[0].sourcedid)
		assert_that(membership, is_not(none()))
		assert_that(membership, has_length(24))
		assert_that(membership, has_property('sourcedid', has_property('source', is_('SIS'))))
		assert_that(membership, has_property('sourcedid', has_property('id', is_('2015FA_CMSC-1313-01'))))

		members = list(membership)
		assert_that(members, has_length(24))
		member = membership[0]
		assert_that(member, is_not(none()))
		assert_that(member, has_property('membership', is_(membership)))
		assert_that(member, has_property('sourcedid', has_property('source', is_('SIS'))))
		assert_that(member, has_property('sourcedid', has_property('id', is_('1328493'))))
		assert_that(member, has_property('role', has_property('roletype', is_('01'))))
		assert_that(member, has_property('role', has_property('status', is_(1))))
		assert_that(member, has_property('role', has_property('userid', is_('drew.knoles'))))
	
	def test_parse_1(self):
		path = os.path.join(os.path.dirname(__file__), 'oc_1.xml')
		self._parse_1(path)

	def _parse_2(self, source):
		path = source
		enterprise = Enterprise.parseFile(path)
		assert_that(enterprise, is_not(none()))
		assert_that(enterprise, has_property("persons", has_length(30)))
		p = enterprise.persons.get_by_userid('david.north@oc.edu')
		assert_that(p, is_not(none()))
		assert_that(p, has_property('userid', is_('david.north@oc.edu')))
		assert_that(p, has_property('userrole', is_('01')))
		assert_that(p, has_property('name', is_('David North')))
		assert_that(p, has_property('email', is_('david.north@oc.edu')))
		assert_that(p, has_property('sourcedid', has_property('source', is_('SIS'))))
		assert_that(p, has_property('sourcedid', has_property('id', is_('1004596'))))
		
		groups = list(enterprise.get_groups())
		assert_that(groups, has_length(1))
		group = enterprise.get_group(groups[0].sourcedid)
		assert_that(group, is_not(none()))
		assert_that(group, has_property('type', is_(none())))
		assert_that(group, has_property('level', is_(none())))
		assert_that(group, has_property('description', is_('Software Engr - Introduction 2015FA')))
		assert_that(group, has_property('sourcedid', has_property('source', is_('SIS'))))
		assert_that(group, has_property('sourcedid', has_property('id', is_('2015FA_CMSC-1313-01'))))
		assert_that(group, has_property('timeframe', has_property('end', is_(1450418400.0))))
		assert_that(group, has_property('timeframe', has_property('start', is_(1440997200.0))))

		memberships = list(enterprise.get_memberships())
		assert_that(memberships, has_length(1))
		membership = enterprise.get_membership(memberships[0].sourcedid)
		assert_that(membership, is_not(none()))
		assert_that(membership, has_length(30))
		assert_that(membership, has_property('sourcedid', has_property('source', is_('SIS'))))
		assert_that(membership, has_property('sourcedid', has_property('id', is_('2015FA_CMSC-1313-01'))))

		members = list(membership)
		assert_that(members, has_length(30))
		member = membership[0]
		assert_that(member, is_not(none()))
		assert_that(member, has_property('membership', is_(membership)))
		assert_that(member, has_property('sourcedid', has_property('source', is_('SIS'))))
		assert_that(member, has_property('sourcedid', has_property('id', is_('1328493'))))
		assert_that(member, has_property('role', has_property('roletype', is_('01'))))
		assert_that(member, has_property('role', has_property('status', is_(1))))
		assert_that(member, has_property('role', has_property('userid', is_('drew.knoles@eagles.oc.edu'))))

	def test_parse_2(self):
		path = os.path.join(os.path.dirname(__file__), 'oc_2.xml')
		self._parse_2(path)
