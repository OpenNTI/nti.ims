#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from functools import total_ordering

from zope import interface

from zope.location.interfaces import IContained

from zope.proxy import ProxyBase

from nti.externalization.proxy import removeAllProxies

from nti.externalization.representation import WithRepr

from nti.ims.sis import get_text
from nti.ims.sis import to_legacy_role

from nti.ims.sis.interfaces import IRole
from nti.ims.sis.interfaces import IMember
from nti.ims.sis.interfaces import IMembership
from nti.ims.sis.interfaces import STUDENT_ROLE
from nti.ims.sis.interfaces import ACTIVE_STATUS
from nti.ims.sis.interfaces import INACTIVE_STATUS
from nti.ims.sis.interfaces import INSTRUCTOR_ROLE

from nti.ims.sis.sourcedid import SourcedID

from nti.ims.sis.utils import text_

from nti.property.property import alias

from nti.schema.eqhash import EqHash

from nti.schema.field import SchemaConfigured

from nti.schema.fieldproperty import createDirectFieldProperties

DEFAULT_ID_TYPE = IMember['idtype'].default


@WithRepr
@total_ordering
@interface.implementer(IRole)
@EqHash('status', 'roletype', 'userid')
class Role(SchemaConfigured):
    createDirectFieldProperties(IRole)

    status = None
    userid = None
    roletype = None

    @property
    def is_student(self):
        return self.roletype == STUDENT_ROLE
    isStudent = is_student

    @property
    def is_instructor(self):
        return self.roletype == INSTRUCTOR_ROLE
    isInstructor = is_instructor

    def __lt__(self, other):
        try:
            return (self.userid, self.status) < (other.userid, other.status)
        except AttributeError:  # pragma: no cover
            return NotImplemented

    def __gt__(self, other):
        try:
            return (self.userid, self.status) > (other.userid, other.status)
        except AttributeError:  # pragma: no cover
            return NotImplemented

    @classmethod
    def createFromElement(cls, element):
        roletype = to_legacy_role(element.get('roletype', STUDENT_ROLE))
        roletype = text_(roletype)

        userid = element.find('userid')
        userid = get_text(userid)

        status = get_text(element.find('status'))
        status = int(status) if status else ACTIVE_STATUS

        datasource = element.find('datasource')
        datasource = get_text(datasource)

        result = Role(userid=userid, 
                      status=status,
                      roletype=roletype, 
                      datasource=datasource)
        return result


@WithRepr
@total_ordering
@interface.implementer(IMember, IContained)
@EqHash('sourcedid', 'idtype', 'role')
class Member(SchemaConfigured):
    createDirectFieldProperties(IMember)

    __name__ = None
    __parent__ = None

    role = None
    idtype = None
    sourcedid = None

    id = alias('sourcedid')
    membership = alias('__parent__')

    @property
    def is_student(self):
        return self.role.is_student if self.role is not None else False
    isStudent = is_student

    @property
    def is_instructor(self):
        return self.role.is_instructor if self.role is not None else False
    isInstructor = is_instructor

    @property
    def status(self):
        return self.role.status if self.role is not None else INACTIVE_STATUS

    @property
    def roletype(self):
        return self.role.roletype if self.role is not None else None

    @property
    def is_active(self):
        return self.role.status == ACTIVE_STATUS if self.role is not None else False
    isActive = is_active

    @property
    def userid(self):
        return self.role.userid if self.role is not None else None
    userId = userid

    def __lt__(self, other):
        try:
            return (self.sourcedid, self.status) < (other.sourcedid, other.status)
        except AttributeError:  # pragma: no cover
            return NotImplemented

    def __gt__(self, other):
        try:
            return (self.sourcedid, self.status) > (other.sourcedid, other.status)
        except AttributeError:  # pragma: no cover
            return NotImplemented

    @classmethod
    def createFromElement(cls, element):
        sid = element.find('sourcedid')
        sid = SourcedID.createFromElement(sid) if sid is not None else None

        idtype = get_text(element.find('idtype'))
        idtype = int(idtype) if idtype else DEFAULT_ID_TYPE

        role = element.find('role')
        role = Role.createFromElement(role) if role is not None else None

        if sid is not None and role is not None:
            result = Member(role=role, 
                            sourcedid=sid,
                            idtype=idtype)
        else:
            result = None

        if result is None:
            logger.debug('Skipping member node %r (%s, %s)', 
                         element, sid, role)
        return result


@total_ordering
class _MemberProxy(ProxyBase):

    course_id = property(lambda s: s.__dict__.get('_course_id'),
                         lambda s, v: s.__dict__.__setitem__('_course_id', v))

    CourseID = alias('course_id')

    def __new__(cls, base, course_id):
        return ProxyBase.__new__(cls, base)

    def __init__(self, base, course_id):
        ProxyBase.__init__(self, base)
        self.course_id = course_id

    def __lt__(self, other):
        try:
            return (self.course_id, self.sourcedid, self.status) < (other.course_id, other.sourcedid, other.status)
        except AttributeError:  # pragma: no cover
            return NotImplemented

    def __gt__(self, other):
        try:
            return (self.course_id, self.sourcedid, self.status) > (other.course_id, other.sourcedid, other.status)
        except AttributeError:  # pragma: no cover
            return NotImplemented


@interface.implementer(IMembership)
class Membership(SchemaConfigured):
    createDirectFieldProperties(IMembership)

    sourcedid = None
    id = alias('sourcedid')
    
    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self,  *args, **kwargs)
        self.members = [] if self.members is None else self.members
        self._v_cache = set()

    def add(self, member):
        if member is not None:
            member.__parent__ = self
            self.members.append(member)
            self._v_cache.add(member)
    append = add

    def __iadd__(self, other):
        assert IMembership.providedBy(other)
        assert not other.sourcedid or other.sourcedid == self.sourcedid

        for member in other.members:
            member = removeAllProxies(member)
            if member not in self._v_cache:
                self.add(member)

        return self

    def __iter__(self):
        for member in self.members:
            yield _MemberProxy(member, self.sourcedid)

    def __len__(self):
        return len(self.members)

    def __getitem__(self, index):
        result = self.members[index]
        return _MemberProxy(result, self.sourcedid)

    def __delitem__(self, index):
        member = self.members[index]
        self._v_cache.remove(member)
        del self.members[index]

    def __contains__(self, member):
        return member in self._v_cache

    def index(self, member):
        return self.members.index(member)

    @classmethod
    def createFromElement(cls, element):
        result = Membership()
        for e in element.iterchildren():
            if e.tag == "sourcedid":
                sid = SourcedID.createFromElement(e)
                result.sourcedid = sid
            elif e.tag == "member":
                member = Member.createFromElement(e)
                result.add(member)
        return result
