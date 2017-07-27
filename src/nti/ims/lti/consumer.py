#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division

__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from lti.tool_config import ToolConfig

from persistent.persistence import Persistent

from pyramid.interfaces import IRequest

from zope import component
from zope import interface

from nti.containers.containers import CaseInsensitiveLastModifiedBTreeContainer

from nti.ims.lti.interfaces import IConfiguredTool
from nti.ims.lti.interfaces import IConfiguredToolContainer
from nti.ims.lti.interfaces import IToolConfig


@component.adapter(IRequest)
@interface.implementer(IConfiguredTool)
class ConfiguredTool(Persistent):

    non_config_values = {'key', 'secret'}

    def __init__(self, **kwargs):

        for (key, value) in kwargs:
            if key in self.non_config_values:
                setattr(self, key, value)
                kwargs.pop(key)

        # TODO some kind of hook in the request to determine if
        # ToolConfig.create_from_xml can be used
        self.config = PersistentToolConfig(kwargs)


@interface.implementer(IToolConfig)
class PersistentToolConfig(ToolConfig, Persistent):

    def __init__(self, params):
        super(PersistentToolConfig, self).__init__(**params)


@interface.implementer(IConfiguredToolContainer)
class ConfiguredToolContainer(CaseInsensitiveLastModifiedBTreeContainer):

    def add_tool(self, tool):
        self[tool.title] = tool

    def edit_tool(self, tool):
        self[tool.title] = tool

    def delete_tool(self, title):
        del self[title]

    def get_tool(self, title):
        try:
            return self[title]
        except KeyError:
            return None
