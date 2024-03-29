#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from nti.ims.sis.interfaces import FACULTY
from nti.ims.sis.interfaces import STUDENT
from nti.ims.sis.interfaces import INSTRUCTOR
from nti.ims.sis.interfaces import STUDENT_ROLE
from nti.ims.sis.interfaces import INSTRUCTOR_ROLE

from nti.ims.sis.utils import get_text
from nti.ims.sis.utils import get_fileobj

logger = __import__('logging').getLogger(__name__)


def to_legacy_role(role):
    if role:
        role = role.upper()
        if role == STUDENT:
            role = STUDENT_ROLE
        elif role in (FACULTY, INSTRUCTOR):
            role = INSTRUCTOR_ROLE
    return role
