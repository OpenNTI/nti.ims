#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

from zope import interface

from zope.interface.common.mapping import IMapping
from zope.interface.common.sequence import IFiniteSequence

from nti.schema.field import Int
from nti.schema.field import Dict
from nti.schema.field import Number
from nti.schema.field import Object
from nti.schema.field import ValidTextLine
from nti.schema.field import IndexedIterable

#: Student role code
STUDENT_ROLE = u"01"

#: Instructor role code
INSTRUCTOR_ROLE = u"02"

#: Student
STUDENT = u'STUDENT'

#: Instructor
FACULTY = u"FACULTY"
INSTRUCTOR = u'INSTRUCTOR'

#: Active enrollment status
ACTIVE_STATUS = 1

#: Inactive enrollment status
INACTIVE_STATUS = 0

#: Classes
CLASSES = u'CLASSES'


class IElementCreatable(interface.Interface):

    def createFromElement(element):
        """
        return a instance of this object from an Element object
        """


class ISourcedID(IElementCreatable):
    id = ValidTextLine(title=u'Identifier', required=True)
    source = ValidTextLine(title=u'Source', required=False, default=u'SIS')


class ITimeFrame(IElementCreatable):
    start = Number(title=u'start time', required=False)
    end = Number(title=u'end time', required=False)


class IGroup(IElementCreatable):
    sourcedid = Object(ISourcedID, title=u'Source id', required=True)
    timeframe = Object(ITimeFrame, title=u'Time frame', required=False)
    description = ValidTextLine(title=u'Group description', required=False)
    type = ValidTextLine(title=u'Group type', required=False)
    level = ValidTextLine(title=u'Group level', required=False)


class IPerson(IElementCreatable):
    sourcedid = Object(ISourcedID, title=u'Source id', required=True)
    userid = ValidTextLine(title=u'user id', required=False)
    name = ValidTextLine(title=u'person name', required=False)
    email = ValidTextLine(title=u'person email', required=False)
    userrole = ValidTextLine(title=u'user role type',
                             required=False,
                             default=STUDENT_ROLE)


class IPersons(IMapping):

    def add(person):
        """
        add a person
        """

    def get_by_userid(userid):
        """
        return a IPerson w/ the specified userid
        """


class IRole(IElementCreatable):
    userid = ValidTextLine(title=u'User id', required=False)
    datasource = ValidTextLine(title=u'Data source', required=False)
    status = Int(title=u'Status id', required=True, default=ACTIVE_STATUS)
    roletype = ValidTextLine(title=u'role type',
                             required=True,
                             default=STUDENT_ROLE)


class IMember(IElementCreatable):
    sourcedid = Object(ISourcedID, title=u'source id', required=True)
    idtype = Int(title=u'Id type', required=False, default=1)
    role = Object(IRole, title=u'Source id', required=True)


class IMembership(IElementCreatable, IFiniteSequence):

    sourcedid = Object(ISourcedID, title=u'source id', required=True)
    members = IndexedIterable(title=u'The members.',
                              value_type=Object(IMember, title=u'A member'))

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

    def __iter__():
        """
        Return an iterator object.
        """


class IEnterprise(IElementCreatable):

    persons = Object(IPersons)

    groups = Dict(key_type=Object(ISourcedID),
                  value_type=Object(IGroup))

    memberships = Dict(key_type=Object(ISourcedID),
                       value_type=Object(IMembership))

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
