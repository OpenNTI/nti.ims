#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from nti.common.iterables import isorted

from .utils import get_text
from .utils import get_fileobj

from .interfaces import STUDENT
from .interfaces import INSTRUCTOR
from .interfaces import STUDENT_ROLE
from .interfaces import INSTRUCTOR_ROLE

def to_legacy_role(role):
    if role:
        role = role.upper()
        if role == STUDENT:
            role = STUDENT_ROLE
        elif role == INSTRUCTOR:
            role = INSTRUCTOR_ROLE
    return role
