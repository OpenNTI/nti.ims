#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import re
from functools import total_ordering

from zope import interface

from nti.externalization.representation import WithRepr

from nti.ims.sis import get_text

from nti.ims.sis.interfaces import ISourcedID

from nti.schema.eqhash import EqHash

from nti.schema.fieldproperty import createDirectFieldProperties

from nti.schema.schema import SchemaConfigured

DEFAULT_SOURCE = ISourcedID['source'].default
CRN_TERM_PATTERN = re.compile(r"(.*)\.(.*)", re.UNICODE | re.IGNORECASE)

logger = __import__('logging').getLogger(__name__)


@WithRepr
@total_ordering
@EqHash('source', 'id')
@interface.implementer(ISourcedID)
class SourcedID(SchemaConfigured):
    createDirectFieldProperties(ISourcedID)

    id = None
    source = None

    @property
    def CRN(self):
        m = CRN_TERM_PATTERN.match(self.id or '')
        groups = m.groups() if m is not None else ()
        return groups[0] if groups else None

    @property
    def Term(self):
        m = CRN_TERM_PATTERN.match(self.id or '')
        groups = m.groups() if m is not None else ()
        return groups[1] if groups else None

    def __lt__(self, other):
        try:
            return (self.source, self.id) < (other.source, other.id)
        except AttributeError:  # pragma: no cover
            return NotImplemented

    def __gt__(self, other):
        try:
            return (self.source, self.id) > (other.source, other.id)
        except AttributeError:  # pragma: no cover
            return NotImplemented

    @classmethod
    def createFromElement(cls, element):
        source = element.find('source')
        source = get_text(source) or DEFAULT_SOURCE

        id_ = element.find('id')
        id_ = get_text(id_)

        result = SourcedID(source=source, id=id_) if source and id_ else None
        if result is None:
            logger.debug('Skipping sourceid node %r (%s, %s)', 
                         element, source, id_)
        return result
