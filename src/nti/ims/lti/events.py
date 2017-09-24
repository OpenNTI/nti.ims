#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from zope import component

from zope.lifecycleevent import IObjectModifiedEvent

from nti.ims.lti.interfaces import IToolConfig

logger = __import__('logging').getLogger(__name__)


@component.adapter(IToolConfig, IObjectModifiedEvent)
def config_modified(config, _):
    config.updateLastMod()
