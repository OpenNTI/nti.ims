#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

from zope import interface

from nti.base.interfaces import ITitled

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
