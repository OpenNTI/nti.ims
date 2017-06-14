#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import component
from zope import interface

from ims_lti_py.tool_config import ToolConfig

from .interfaces import IToolConfig

class ToolConfigFactory(object):

    def __init__(self, tool):
        self.tool = tool

    def __call__(self):
        config = ToolConfig()
        config.title = self.tool.title
        config.description = self.tool.description
        config.__name__ = self.tool.__name__
        interface.alsoProvides(config, IToolConfig)
        return config
