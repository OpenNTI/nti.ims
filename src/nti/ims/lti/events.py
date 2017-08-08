#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import component

from zope.lifecycleevent import IObjectModifiedEvent

from nti.ims.lti.interfaces import IToolConfig


@component.adapter(IToolConfig, IObjectModifiedEvent)
def config_modified(config, _):
    config.updateLastMod()
