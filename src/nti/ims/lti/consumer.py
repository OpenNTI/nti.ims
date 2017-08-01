#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division

__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from lti import tool_config

from lti.tool_config import ToolConfig

from persistent import Persistent

from slugify import Slugify

from zope import interface

from zope.container.btree import BTreeContainer

from zope.container.contained import Contained

from zope.container.interfaces import INameChooser

from nti.base.mixins import CreatedAndModifiedTimeMixin

from nti.ims.lti.interfaces import IConfiguredTool
from nti.ims.lti.interfaces import IToolConfig

from nti.schema.fieldproperty import createDirectFieldProperties

from nti.schema.schema import PermissiveSchemaConfigured as SchemaConfigured


@interface.implementer(IConfiguredTool)
class ConfiguredTool(SchemaConfigured, Persistent, Contained, CreatedAndModifiedTimeMixin):

    __external_can_create__ = True

    mimeType = mime_type = u'application/vnd.nextthought.ims.consumer.configuredtool'

    createDirectFieldProperties(IConfiguredTool)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)
        Persistent.__init__(self)


@interface.implementer(IToolConfig)
class PersistentToolConfig(ToolConfig, Persistent, CreatedAndModifiedTimeMixin):

    def __init__(self, kwargs):
        kwargs = self._validate_kwargs(kwargs)
        super(PersistentToolConfig, self).__init__(**kwargs)
        Persistent.__init__(self)

    def _validate_kwargs(self, kwargs):
        result = dict()
        for kwarg in kwargs:
            if kwarg in tool_config.VALID_ATTRIBUTES:
                result[kwarg] = kwargs[kwarg]
        return result

    def set_custom_param(self, key, val):
        super(PersistentToolConfig, self).set_custom_param(key, val)
        self._p_changed = 1
        self.updateLastMod()

    def set_ext_param(self, ext_key, param_key, val):
        super(PersistentToolConfig, self).set_ext_param(ext_key, param_key, val)
        self._p_changed = 1
        self.updateLastMod()

    def set_ext_params(self, ext_key, ext_params):
        super(PersistentToolConfig, self).set_ext_params(ext_key, ext_params)
        self._p_changed = 1
        self.updateLastMod()

    def __getstate__(self):
        return 1, self.to_xml()

    def __setstate__(self, state):
        assert state[0] == 1
        self.create_from_xml(state[1])


class ConfiguredToolContainer(BTreeContainer, CreatedAndModifiedTimeMixin):

    def add_tool(self, tool):
        slugger = Slugify()
        name = slugger(tool.title)
        name = INameChooser(self).chooseName(name, tool)
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

    def edit_tool(self, tool):
        pass
