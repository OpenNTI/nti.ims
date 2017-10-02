#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import time
import isodate
from functools import total_ordering

from zope import interface

from nti.base._compat import text_

from nti.externalization.datetime import datetime_from_string

from nti.externalization.representation import WithRepr

from nti.ims.sis import get_text

from nti.ims.sis.interfaces import IGroup
from nti.ims.sis.interfaces import ITimeFrame

from nti.ims.sis.sourcedid import SourcedID

from nti.property.property import alias

from nti.schema.eqhash import EqHash

from nti.schema.field import SchemaConfigured

from nti.schema.fieldproperty import createDirectFieldProperties

from nti.schema.interfaces import InvalidValue

logger = __import__('logging').getLogger(__name__)


@WithRepr
@EqHash('start', 'end')
@interface.implementer(ITimeFrame)
class TimeFrame(SchemaConfigured):
    createDirectFieldProperties(ITimeFrame)

    end = None
    start = None

    @classmethod
    def _mktime(cls, node):
        value = get_text(node)
        if value:
            try:
                datetime = datetime_from_string(value)
            except (InvalidValue, ValueError):
                datetime = isodate.parse_date(value)
            return time.mktime(datetime.timetuple())

    @classmethod
    def createFromElement(cls, element):
        start = cls._mktime(element.find('begin'))
        end = cls._mktime(element.find('end'))
        if start is not None or end is not None:
            result = TimeFrame(start=start, end=end)
            return result
        logger.debug('Skipping timeframe node %r (%s, %s)',
                     element, start, end)
        return None


@WithRepr
@total_ordering
@EqHash('sourcedid')
@interface.implementer(IGroup)
class Group(SchemaConfigured):
    createDirectFieldProperties(IGroup)

    sourcedid = None
    id = alias('sourcedid')

    def __lt__(self, other):
        try:
            return self.sourcedid < other.sourcedid
        except AttributeError:  # pragma: no cover
            return NotImplemented

    @classmethod
    def createFromElement(cls, element):
        sid = element.find('sourcedid')
        sid = SourcedID.createFromElement(sid) if sid is not None else None

        description = element.find('description')
        if description is not None:
            long_desc = get_text(description.find('long'))
            short_desc = get_text(description.find('short'))
            description = long_desc if long_desc else short_desc

        type_ = level = None
        grouptype = element.find('grouptype')
        if grouptype is not None:
            typevalue = grouptype.find('typevalue')
            type_ = get_text(typevalue)
            if typevalue is not None:
                level = text_(typevalue.get('level') or '')

        timeframe = element.find('timeframe')
        if timeframe is not None:
            timeframe = TimeFrame.createFromElement(timeframe)

        result = None
        if sid is not None:
            result = Group(type=type_,
                           level=level,
                           sourcedid=sid,
                           timeframe=timeframe,
                           description=description)

        if result is None:
            logger.debug('Skipping group node (%s, %s)', element, sid)
        return result
