#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division

from nti.app.externalization.view_mixins import ModeledContentUploadRequestUtilsMixin

__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from lti.tool_config import ToolConfig

from persistent.persistence import Persistent

from slugify import Slugify

from zope import interface

from zope.container.contained import Contained

from zope.container.interfaces import INameChooser

from nti.containers.containers import CaseInsensitiveLastModifiedBTreeContainer

from nti.ims.lti.interfaces import IConfiguredTool
from nti.ims.lti.interfaces import IToolConfig


@interface.implementer(IConfiguredTool)
class ConfiguredTool(Persistent, Contained):

    non_config_values = {'consumer_key', 'secret'}

    def __init__(self, _v_request):

        from IPython.core.debugger import Tracer;Tracer()()

        _v_kwargs = dict(_v_request.params)

        for (key, value) in _v_kwargs.items():
            setattr(self, key, value)
            if key in self.non_config_values:
                _v_kwargs.pop(key)
        self.config = PersistentToolConfig(**_v_kwargs)


@interface.implementer(IToolConfig)
class PersistentToolConfig(ToolConfig, Persistent):

    def __init__(self, **kwargs):
        super(PersistentToolConfig, self).__init__(**kwargs)

    def set_custom_param(self, key, val):
        super(PersistentToolConfig, self).set_custom_param(key, val)
        self._p_changed = 1

    def set_ext_param(self, ext_key, param_key, val):
        super(PersistentToolConfig, self).set_ext_param(ext_key, param_key, val)
        self._p_changed = 1

    def set_ext_params(self, ext_key, ext_params):
        super(PersistentToolConfig, self).set_ext_params(ext_key, ext_params)
        self._p_changed = 1


class ConfiguredToolContainer(CaseInsensitiveLastModifiedBTreeContainer):

    def add_tool(self, tool):
        slugger = Slugify()
        name = slugger(tool.title)
        name = INameChooser(self).chooseName(name, tool)
        tool.__name__ = name

        self[name] = tool

    def delete_tool(self, tool):
        # If the name is passed instead of the tool
        name = getattr(tool, '__name__', tool)
        del self[name]

    def __getitem__(self, tool):
        name = getattr(tool, '__name__', tool)
        return super(ConfiguredToolContainer, self).__getitem__(name)

    def edit_tool(self, tool):
        pass
