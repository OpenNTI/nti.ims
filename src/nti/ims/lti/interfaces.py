#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

from zope import interface

from nti.base.interfaces import ITitled

from nti.dataserver.interfaces import ITitledDescribedContent

from nti.schema.field import TextLine

class IOAuthConsumer(ITitled):

    key = TextLine(title=u'The consumer key',
                   required=True)

    secret = TextLine(title=u'The consumer secret',
                      required=True)

    title = TextLine(title=u'A descriptive title for this consumer',
                     required=True)


class IOAuthConsumers(interface.Interface):
    """
    A mapping type which stores IOAuthConsumer implementations
    by their key.
    """

    def __getitem__(key):
        """
        Returns the IOAuthConsumer for the given key
        """

    def __setitem__(key, consumer):
        """
        Sets the IOAuthConsumer for the given key
        """

    def __delitem__(key):
        """
        Removes the IOAuthConsumer for the given key
        """

class ITool(ITitledDescribedContent):
    """
    Describes a tool in the lti sense.  This works in conjunction.
    """

class IToolConfig(interface.Interface):
    """
    An object providing configuration information for launching a tool.
    This is typcially used to render an LTI Common Cartridge xml snippet
    for configuring the tool inside a consumer.
    """

class IToolConfigFactory(interface.Interface):
    """
    A callable that is capable of generating an IToolConfig.  These
    are typcially registered as adapters on ITool.
    """

    def __call__():
        pass

