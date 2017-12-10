#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from functools import total_ordering

from zope import interface

from nti.externalization.representation import WithRepr

from nti.ims.sis import get_text
from nti.ims.sis import to_legacy_role

from nti.ims.sis.interfaces import IPerson
from nti.ims.sis.interfaces import IPersons

from nti.ims.sis.sourcedid import SourcedID

from nti.property.property import alias

from nti.schema.eqhash import EqHash

from nti.schema.field import SchemaConfigured

from nti.schema.fieldproperty import createDirectFieldProperties

DEFAULT_ROLE = IPerson['userrole'].default

logger = __import__('logging').getLogger(__name__)


@WithRepr
@total_ordering
@EqHash('sourcedid')
@interface.implementer(IPerson)
class Person(SchemaConfigured):
    createDirectFieldProperties(IPerson)

    userid = None
    userrole = None
    sourcedid = None
    id = alias('sourcedid')

    def __lt__(self, other):
        try:
            return self.sourcedid < other.sourcedid
        except AttributeError:  # pragma: no cover
            return NotImplemented

    def __gt__(self, other):
        try:
            return self.sourcedid > other.sourcedid
        except AttributeError:  # pragma: no cover
            return NotImplemented

    @classmethod
    def createFromElement(cls, element):
        sid = element.find('sourcedid')
        sid = SourcedID.createFromElement(sid) if sid is not None else None

        userid = element.find('userid')
        userid = get_text(userid)

        name = u''
        e_name = element.find('name')
        if e_name is not None:
            fn = e_name.find('fn')
            if fn is not None:
                name = get_text(fn)
            else:
                n = e_name.find('n')
                given = get_text(n.find('given')) if n is not None else None
                family = get_text(n.find('family')) if n is not None else None
                if given and family:
                    name = u"%s %s" % (given.title(), family.title())
        if not name:
            logger.warning("No name specified for person %s", sid)

        email = element.find('email')
        email = get_text(email)

        userrole = None
        extension = element.find('extension')
        if extension is not None:
            userrole = get_text(extension.find('userrole'))
            userrole = to_legacy_role(userrole)
        else:
            userrole = DEFAULT_ROLE

        if sid is not None:
            result = Person(sourcedid=sid,
                            userid=userid,
                            name=name,
                            email=email,
                            userrole=userrole)
        else:
            result = None

        if result is None:
            logger.debug('Skipping person node %r (%s)', element, sid)
        return result


@interface.implementer(IPersons)
class Persons(dict):

    def __init__(self):
        super(Persons, self).__init__()
        self.by_userid = {}

    def add(self, person):
        if person is not None:
            self[person.sourcedid] = person
            self.by_userid[person.userid] = person

    def get_by_userid(self, userid):
        return self.by_userid.get(userid)

    def __delitem__(self, key):
        result = self[key]
        dict.__delitem__(self, key)
        if result is not None:
            self.by_userid.pop(result.userid)
        return result
