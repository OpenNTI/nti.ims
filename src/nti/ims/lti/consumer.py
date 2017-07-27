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

from nti.ims.lti.interfaces import IConfiguredTool


@component.adapter(IRequest)
@interface.implementer(IConfiguredTool)
class ConfiguredTool(Persistent):

    def __init__(self, params):

        # Pop the non-config defined values
        self.key = params.pop('consumer_key')
        self.secret = params.pop('secret')

        # Store the params to populate the form for future editing
        # and viewing as ToolConfig isn't helpful for retrieval
        self.params = params
        self.title = params['title']
        self.description = params['description']

        # TODO some kind of hook in the request to determine if
        # ToolConfig.create_from_xml can be used
        self.config = PersistentToolConfig(params)


class PersistentToolConfig(Persistent, ToolConfig):

    def __init__(self, params):
        super(PersistentToolConfig, self).__init__(**params)
