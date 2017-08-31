#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from lti import tool_config

from lti.tool_config import ToolConfig

from zope import component
from zope import interface
from zope import lifecycleevent

from zope.cachedescriptors.property import readproperty

from zope.container.btree import BTreeContainer

from zope.container.contained import Contained

from zope.container.interfaces import INameChooser

from persistent import Persistent

from nti.base.mixins import CreatedAndModifiedTimeMixin

from nti.containers.containers import AbstractNTIIDSafeNameChooser

from nti.dublincore.time_mixins import PersistentCreatedAndModifiedTimeObject

from nti.ims.lti.interfaces import IToolConfig
from nti.ims.lti.interfaces import IConfiguredTool
from nti.ims.lti.interfaces import IConfiguredToolContainer

from nti.schema.fieldproperty import createDirectFieldProperties

from nti.schema.schema import PermissiveSchemaConfigured as SchemaConfigured

logger = __import__('logging').getLogger(__name__)


@interface.implementer(IConfiguredTool)
class ConfiguredTool(SchemaConfigured, Contained, PersistentCreatedAndModifiedTimeObject):

    __external_can_create__ = True

    mimeType = mime_type = 'application/vnd.nextthought.ims.consumer.configuredtool'

    createDirectFieldProperties(IConfiguredTool)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)
        PersistentCreatedAndModifiedTimeObject.__init__(self)

    @readproperty
    def title(self):
        if self.config is not None:
            return self.config.title

    @readproperty
    def description(self):
        if self.config is not None:
            return self.config.description

    @readproperty
    def launch_url(self):
        if self.config is not None:
            return self.config.launch_url

    @readproperty
    def secure_launch_url(self):
        if self.config is not None:
            return self.config.secure_launch_url


@interface.implementer(IToolConfig)
class PersistentToolConfig(ToolConfig, PersistentCreatedAndModifiedTimeObject):

    __external_can_create__ = True

    def __init__(self, **kwargs):
        # Parse the kwargs for tool config specific values
        self._kwargs = kwargs
        kwargs = {argname: kwargs[argname]
                  for argname in kwargs if argname in tool_config.VALID_ATTRIBUTES}
        super(PersistentToolConfig, self).__init__(**kwargs)
        PersistentCreatedAndModifiedTimeObject.__init__(self)

    def set_custom_param(self, key, val):
        super(PersistentToolConfig, self).set_custom_param(key, val)
        self._p_changed = 1
        lifecycleevent.modified(self)

    def set_ext_param(self, ext_key, param_key, val):
        super(PersistentToolConfig, self).set_ext_param(ext_key, param_key, val)
        self._p_changed = 1
        lifecycleevent.modified(self)

    def set_ext_params(self, ext_key, ext_params):
        super(PersistentToolConfig, self).set_ext_params(ext_key, ext_params)
        self._p_changed = 1
        lifecycleevent.modified(self)

    def __setstate__(self, state):
        assert state[0] == 1
        self.process_xml(state[1])
        self.createdTime = state[2]
        self.lastModified = state[3]

    def __getstate__(self):
        return 1, self.to_xml(), self.createdTime, self.lastModified

    def __getnewargs__(self):
        return (self._kwargs,)

    @staticmethod
    def create_from_xml(xml):
        config = PersistentToolConfig()
        config.process_xml(xml)
        return config


@interface.implementer(IConfiguredToolContainer)
class ConfiguredToolContainer(BTreeContainer, CreatedAndModifiedTimeMixin):

    def add_tool(self, tool):
        name = INameChooser(self).chooseName(tool.title, tool)
        tool.__name__ = name

        self[name] = tool
        return tool

    def delete_tool(self, tool):
        # If the name is passed instead of the tool
        name = getattr(tool, '__name__', tool)
        del self[name]

    def __getitem__(self, tool):
        name = getattr(tool, '__name__', tool)
        return super(ConfiguredToolContainer, self).__getitem__(name)


@interface.implementer(INameChooser)
@component.adapter(IConfiguredToolContainer)
class _ConfiguredToolNameChooser(AbstractNTIIDSafeNameChooser):
    leaf_iface = IConfiguredToolContainer
