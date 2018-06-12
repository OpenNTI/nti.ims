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
from nti.externalization.externalization import to_external_object

from zope import component
from zope import interface
from zope import lifecycleevent

from zope.cachedescriptors.property import readproperty

from zope.container.btree import BTreeContainer

from zope.container.contained import Contained

from zope.container.interfaces import INameChooser

from nti.base._compat import text_

from nti.base.mixins import CreatedAndModifiedTimeMixin

from nti.containers.containers import AbstractNTIIDSafeNameChooser

from nti.ntiids.common import generate_ntiid

from nti.dublincore.time_mixins import PersistentCreatedAndModifiedTimeObject

from nti.externalization.datastructures import InterfaceObjectIO

from nti.ims.lti.interfaces import IToolConfig
from nti.ims.lti.interfaces import IConfiguredTool
from nti.ims.lti.interfaces import IConfiguredToolContainer

from nti.schema.fieldproperty import createDirectFieldProperties

from nti.schema.schema import PermissiveSchemaConfigured as SchemaConfigured

logger = __import__('logging').getLogger(__name__)


@interface.implementer(IConfiguredTool)
class ConfiguredTool(SchemaConfigured, Contained, PersistentCreatedAndModifiedTimeObject):

    __external_can_create__ = True

    nttype = 'ConfiguredTool'

    mimeType = mime_type = 'application/vnd.nextthought.ims.consumer.configuredtool'

    createDirectFieldProperties(IConfiguredTool)

    def __init__(self, *args, **kwargs):
        SchemaConfigured.__init__(self, *args, **kwargs)
        PersistentCreatedAndModifiedTimeObject.__init__(self)

    @readproperty
    def ntiid(self):  # pylint: disable=method-hidden
        self.ntiid = generate_ntiid(nttype=self.nttype)
        return self.ntiid

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


class UnicodeForcingProperty(object):

    def __init__(self, value=None):
        self._value = value

    def __get__(self, instance, owner):
        if self._value is not None:
            return text_(self._value)

    def __set__(self, instance, value):
        self._value = value


class StringForcingProperty(object):

    def __init__(self, value=None):
        self._value = value

    def __get__(self, instance, owner):
        if self._value is not None:
            return str(self._value)

    def __set__(self, instance, value):
        self._value = value


@interface.implementer(IToolConfig)
class PersistentToolConfig(ToolConfig, PersistentCreatedAndModifiedTimeObject):

    __external_can_create__ = True

    title = UnicodeForcingProperty()
    description = UnicodeForcingProperty()
    launch_url = StringForcingProperty()
    secure_launch_url = StringForcingProperty()

    def __init__(self, **kwargs):
        #        # Parse the kwargs for tool config specific values
        self._kwargs = kwargs
        kwargs = {
            argname: kwargs[argname]
            for argname in kwargs if argname in tool_config.VALID_ATTRIBUTES
        }
        super(PersistentToolConfig, self).__init__(**kwargs)
        PersistentCreatedAndModifiedTimeObject.__init__(self)

    def set_custom_param(self, key, val):
        super(PersistentToolConfig, self).set_custom_param(key, val)
        # pylint: disable=attribute-defined-outside-init
        self._p_changed = 1
        lifecycleevent.modified(self)

    def set_ext_param(self, ext_key, param_key, val):
        super(PersistentToolConfig, self).set_ext_param(ext_key, param_key, val)
        # pylint: disable=attribute-defined-outside-init
        self._p_changed = 1
        lifecycleevent.modified(self)

    def set_ext_params(self, ext_key, ext_params):
        super(PersistentToolConfig, self).set_ext_params(ext_key, ext_params)
        # pylint: disable=attribute-defined-outside-init
        self._p_changed = 1
        lifecycleevent.modified(self)

    def __setstate__(self, state):
        assert state[0] == 1
        super(PersistentToolConfig, self).__init__()
        self.process_xml(state[1])
        self.createdTime = state[2]
        self.lastModified = state[3]

    def __getstate__(self):
        return 1, self.to_xml(), self.createdTime, self.lastModified

    def __getnewargs__(self):
        return (self._kwargs,)

    def to_xml(self):
        launch_url = getattr(self, 'launch_url', None)
        secure_launch_url = getattr(self, 'secure_launch_url', None)
        if launch_url and not secure_launch_url:
            self.secure_launch_url = launch_url
        elif secure_launch_url and not launch_url:
            self.launch_url = secure_launch_url
        return super(PersistentToolConfig, self).to_xml()

    @staticmethod
    def create_from_xml(xml):
        config = PersistentToolConfig()
        xml = str(xml)  # This must be a string, unicode will not work
        config.process_xml(xml)
        return config


@interface.implementer(IConfiguredToolContainer)
class ConfiguredToolContainer(BTreeContainer, CreatedAndModifiedTimeMixin):

    def _get_tool_key(self, tool):
        return getattr(tool, 'ntiid', tool)

    def add_tool(self, tool):
        self[tool.ntiid] = tool
        return tool

    def delete_tool(self, tool):
        key = self._get_tool_key(tool)
        try:
            del self[key]
            result = True
        except KeyError:  # pragma: no cover
            result = False
        return result

    def __getitem__(self, item):
        key = self._get_tool_key(item)
        return super(ConfiguredToolContainer, self).__getitem__(key)


@interface.implementer(INameChooser)
@component.adapter(IConfiguredToolContainer)
class _ConfiguredToolNameChooser(AbstractNTIIDSafeNameChooser):
    leaf_iface = IConfiguredToolContainer
