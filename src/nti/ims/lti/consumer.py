#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division

__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from lti.tool_config import ToolConfig

from persistent.persistence import Persistent

from pyramid.interfaces import IRequest

from slugify import Slugify

from zope import component
from zope import interface

from zope.container.interfaces import INameChooser

from nti.containers.containers import CaseInsensitiveLastModifiedBTreeContainer

from nti.ims.lti.interfaces import IConfiguredTool
from nti.ims.lti.interfaces import IConfiguredToolContainer
from nti.ims.lti.interfaces import IToolConfig


@component.adapter(IRequest)
@interface.implementer(IConfiguredTool)
class ConfiguredTool(Persistent):

    non_config_values = {'key', 'secret'}

    def __init__(self, **kwargs):

        for (key, value) in kwargs.items():
            setattr(self, key, value)
            if key in self.non_config_values:
                kwargs.pop(key)
        self.config = PersistentToolConfig(**kwargs)


@interface.implementer(IToolConfig)
class PersistentToolConfig(ToolConfig, Persistent):

    def __init__(self, **kwargs):
        super(PersistentToolConfig, self).__init__(**kwargs)

    def __setattr__(self, key, value):
        super(PersistentToolConfig, self).__setattr__(key, value)
        self._p_changed = 1

    def __delattr__(self, item):
        super(PersistentToolConfig, self).__delattr__(item)
        self._p_changed = 1


@interface.implementer(IConfiguredToolContainer)
class ConfiguredToolContainer(CaseInsensitiveLastModifiedBTreeContainer):

    def add_tool(self, tool):
        name = tool.title
        # TODO Won't adapt
        # name = INameChooser(self).chooseName(name, tool)
        slugger = Slugify()
        slugged_name = slugger(name)
        tool.__name__ = slugged_name

        self[slugged_name] = tool

    def delete_tool(self, tool):
        # If the name is passed instead of the tool
        name = getattr(tool, '__name__', tool)
        del self[name]

    def __getitem__(self, tool):
        name = getattr(tool, '__name__', tool)
        return super(ConfiguredToolContainer, self).__getitem__(name)
