#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division

__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from lti import tool_config

from lti.tool_config import ToolConfig

from persistent import Persistent

from slugify import Slugify

from xml.etree import ElementTree as ET

from zope import component
from zope import interface

from zope.cachedescriptors.property import readproperty

from zope.container.btree import BTreeContainer

from zope.container.contained import Contained

from zope.container.interfaces import INameChooser

from nti.base.mixins import CreatedAndModifiedTimeMixin

from nti.containers.containers import AbstractNTIIDSafeNameChooser

from nti.externalization.datastructures import InterfaceObjectIO

from nti.externalization.interfaces import IInternalObjectUpdater

from nti.ims.lti.interfaces import IConfiguredTool
from nti.ims.lti.interfaces import IConfiguredToolContainer
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

    @readproperty
    def title(self):
        return self.config.title

    @readproperty
    def description(self):
        return self.config.description

    @readproperty
    def launch_url(self):
        return self.config.launch_url

    @readproperty
    def secure_launch_url(self):
        return self.config.secure_launch_url


@interface.implementer(IToolConfig)
class PersistentToolConfig(ToolConfig, Persistent, CreatedAndModifiedTimeMixin):

    __external_can_create__ = True

    def __init__(self, kwargs):
        # Parse the kwargs for tool config specific values
        kwargs = {argname: kwargs[argname] for argname in kwargs if argname in tool_config.VALID_ATTRIBUTES}

        super(PersistentToolConfig, self).__init__(**kwargs)
        Persistent.__init__(self)

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
        self.process_xml(state[1])


class ConfiguredToolContainer(BTreeContainer, CreatedAndModifiedTimeMixin):

    def add_tool(self, tool):
        slugger = Slugify()
        name = slugger(tool.title)
        name = _ConfiguredToolNameChooser(self).chooseName(name, tool)
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
        self.delete_tool(tool.__name__)
        self[tool.__name__] = tool


@component.adapter(IConfiguredTool)
@interface.implementer(IInternalObjectUpdater)
class ConfiguredToolInternalizer(InterfaceObjectIO):

    _ext_iface_upper_bound = IConfiguredTool

    def updateFromExternalObject(self, parsed, *args, **kwargs):
        config = _create_persistent_tool_config(parsed)
        super(ConfiguredToolInternalizer, self).updateFromExternalObject(parsed, *args, **kwargs)
        self._ext_self.config = config


def _create_persistent_tool_config(parsed):
    field_storage = parsed['xml_file']
    # Create from xml if uploaded
    if parsed['xml_file'] is not u'':

        file = field_storage.file
        xml_tree = ET.parse(file)
        root = xml_tree.getroot()
        xml_string = ET.tostring(root)

        pconfig = PersistentToolConfig(dict())
        pconfig.process_xml(xml_string)
        return pconfig
    return PersistentToolConfig(parsed)

@component.adapter(IConfiguredToolContainer)
@interface.implementer(INameChooser)
class _ConfiguredToolNameChooser(AbstractNTIIDSafeNameChooser):

    leaf_iface = IConfiguredToolContainer
