#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
sheldon.smith
7/17/17

"""

from __future__ import print_function, absolute_import, division

__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface

from lti import ToolProvider

from nti.ims.lti.interfaces import IToolConsumerInstanceBuilder



@interface.implementer(IToolConsumerInstanceBuilder)
class LaunchRequestParser(object):

    def build(self, launch_request):

        # unpack the request

        request = ToolProvider.from_unpacked_request(None,
                                                     launch_request.URL,
                                                     launch_request.params,
                                                     launch_request.headers)



