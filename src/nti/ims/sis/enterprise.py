#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from io import BytesIO

from lxml import etree

import six

from zope import interface

from nti.ims.sis.group import Group

from nti.ims.sis.interfaces import IEnterprise

from nti.ims.sis.membership import Membership

from nti.ims.sis.person import Person
from nti.ims.sis.person import Persons

from nti.ims.sis import get_fileobj

from nti.schema.fieldproperty import createDirectFieldProperties

from nti.schema.schema import SchemaConfigured

etree_parse = getattr(etree, 'parse')

logger = __import__('logging').getLogger(__name__)


@interface.implementer(IEnterprise)
class Enterprise(SchemaConfigured):
    createDirectFieldProperties(IEnterprise)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self,  *args, **kwargs)
        self.groups = {} if self.groups is None else self.groups
        self.persons = Persons() if self.persons is None else self.persons
        self.memberships = {} if self.memberships is None else self.memberships

    def add_group(self, group):
        if group is not None:
            self.groups[group.sourcedid] = group

    def get_group(self, groupid):
        return self.groups.get(groupid)

    def get_groups(self):
        return six.itervalues(self.groups)

    def add_membership(self, membership):
        if membership is not None:
            if membership.sourcedid in self.memberships:
                current = self.memberships[membership.sourcedid]
                current += membership  # merge
            else:
                self.memberships[membership.sourcedid] = membership

    def get_membership(self, groupid):
        return self.memberships.get(groupid)

    def get_all_members(self, transform=None):
        for membership in self.memberships.values():
            for member in membership:
                if transform is not None:
                    yield transform(member)
                else:
                    yield member

    def get_memberships(self):
        return six.itervalues(self.memberships)

    def get_person(self, sourceid):
        return self.persons.get(sourceid)

    def get_persons(self):
        return self.persons.values()

    @classmethod
    def createFromElement(cls, element):
        enterprise = Enterprise()
        for node in element.iterchildren():
            if node.tag == 'group':
                g = Group.createFromElement(node)
                enterprise.add_group(g)
            elif node.tag == 'person':
                p = Person.createFromElement(node)
                enterprise.persons.add(p)
            elif node.tag == 'membership':
                m = Membership.createFromElement(node)
                enterprise.add_membership(m)
        return enterprise

    @classmethod
    def _check(cls, enterprise):
        for m in enterprise.get_all_members():
            # set userid if mssing
            if m.userid is None:
                p = enterprise.get_person(m.sourcedid)
                if p is not None:
                    m.role.userid = p.userid
                else:
                    logger.warning("incomplete membership record %s", m)
        return enterprise

    @classmethod
    def parse(cls, source):
        if not hasattr(source, 'read'):
            source = BytesIO(source)
        tree = etree_parse(source)
        root = tree.getroot()
        result = cls.createFromElement(root)
        return cls._check(result) if result is not None else None

    @classmethod
    def parseFile(cls, source):
        fileobj = None
        try:
            fileobj = get_fileobj(source)
            result = cls.parse(fileobj)
            return result
        finally:
            if hasattr(fileobj, 'close'):
                fileobj.close()
