#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

from zope import interface

from zope.interface.common.sequence import IFiniteSequence

from dolmen.builtins import IDict
from dolmen.builtins import IIterable

from nti.schema.field import Int
from nti.schema.field import Dict
from nti.schema.field import Float
from nti.schema.field import Object
from nti.schema.field import ValidTextLine
from nti.schema.field import IndexedIterable

#: Student role code
STUDENT_ROLE = "01"

#: Instructor role code
INSTRUCTOR_ROLE = "02"

#: Student
STUDENT = 'STUDENT'

#: Instructor
FACULTY = INSTRUCTOR = 'FACULTY'

#: Active enrollment status
ACTIVE_STATUS = 1

#: Inactive enrollment status
INACTIVE_STATUS = 0

#: Classes
CLASSES = 'CLASSES'

class IElementCreatable(interface.Interface):

	def createFromElement(element):
		"""
		return a instance of this object from an Element object
		"""

class ISourcedID(IElementCreatable):
	id = ValidTextLine(title='Identifier', required=True)
	source = ValidTextLine(title='Source', required=False, default='SIS')

class ITimeFrame(IElementCreatable):
	start = Float(title='start time', required=False)
	end = Float(title='end time', required=False)

class IGroup(IElementCreatable):
	sourcedid = Object(ISourcedID, title='Source id', required=True)
	timeframe = Object(ITimeFrame, title='Time frame', required=False)
	description = ValidTextLine(title='Group description', required=False)
	type = ValidTextLine(title='Group type', required=False)
	level = ValidTextLine(title='Group level', required=False)

class IPerson(IElementCreatable):
	sourcedid = Object(ISourcedID, title='Source id', required=True)
	userid = ValidTextLine(title='user id', required=False)
	name = ValidTextLine(title='person name', required=False)
	email = ValidTextLine(title='person email', required=False)
	userrole = ValidTextLine(title='user role type', required=False, default=STUDENT_ROLE)

class IPersons(IDict):

	def add(person):
		"""
		add a person
		"""

	def get_by_userid(userid):
		"""
		return a IPerson w/ the specified userid
		"""

class IRole(IElementCreatable):
	userid = ValidTextLine(title='User id', required=False)
	datasource = ValidTextLine(title='Data source', required=False)
	status = Int(title='Status id', required=True, default=ACTIVE_STATUS)
	roletype = ValidTextLine(title='role type', required=True, default=STUDENT_ROLE)

class IMember(IElementCreatable):
	sourcedid = Object(ISourcedID, title='source id', required=True)
	idtype = Int(title='Id type', required=False, default=1)
	role = Object(IRole, title='Source id', required=True)

class IMembership(IElementCreatable, IIterable, IFiniteSequence):

	sourcedid = Object(ISourcedID, title='source id', required=True)
	members = IndexedIterable(title="The members.",
							  value_type=Object(IMember, title="A member"))

	def add(member):
		"""
		add a member
		"""

	def index(member):
		"""
		return the storage index for the specified member
		"""

	def __iadd__(other):
		"""
		merge with another membership
		"""

class IEnterprise(IElementCreatable):

	persons = Object(IPersons)
	groups = Dict(key_type=Object(ISourcedID), value_type=Object(IGroup))
	membership = Dict(key_type=Object(ISourcedID), value_type=Object(IMembership))

	def get_persons():
		"""
		return all IPerson objects in this object
		"""

	def add_group(group):
		"""
		add the specified group
		"""

	def get_group(sourcedid):
		"""
		return the group w/ the specifeid id
		"""

	def get_groups():
		"""
		return all groups
		"""

	def add_membership(membership):
		""""
		add the specified membership
		"""

	def get_membership(sourcedid):
		"""
		return the membership w/ the specifeid id
		"""

	def get_memberships():
		"""
		return all membership
		"""
