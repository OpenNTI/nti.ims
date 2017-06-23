#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface

from lti.tool_config import ToolConfig

from nti.ims.lti.interfaces import IToolConfig


class ToolConfigFactory(object):

    def __init__(self, tool):
        self.tool = tool

    def __call__(self):
        config = ToolConfig()
        config.title = self.tool.title
        config.__name__ = self.tool.__name__
        config.description = self.tool.description
        interface.alsoProvides(config, IToolConfig)
        return config
