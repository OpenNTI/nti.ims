#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division

__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from zope import interface

from nti.base.interfaces import ITitled

from nti.schema.field import HTTPURL
from nti.schema.field import TextLine


class IOAuthProvider(ITitled):
    """
    The OAuth information for a Tool Provider
    """

    key = TextLine(title=u'The provider key',
                   required=True)

    secret = TextLine(title=u'The provider secret',
                      required=True)

    title = TextLine(title=u'A descriptive title for this provider',
                     required=True)


class IOAuthProviders(interface.Interface):
    """
    A mapping type which stores IOAuthProvider implementations
    by their key
    """

    def __getitem__(key):
        """
        Returns the IOAuthProvider for the given key
        """

    def __setitem__(key, provider):
        """
        Sets the IOAuthProvider for the given key
        """

    def __delitem__(key):
        """
        Removes the IOAuthProvider for the given key
        """


class IProviderTool(interface.Interface):
    """
    Describes a provider tool in the lti sense
    """

    launch_url = HTTPURL(title=u'The launch url for a provider tool',
                         required=True)

    title = TextLine(title=u'A descriptive title for this provider tool',
                     required=True)


class IOnConsumerLaunchRequestListener(interface.Interface):
    """
    Provides any launch time parameters
    """

    def set_user_info():
        """
        Provides user info for a launch request
        """

    def set_user_permissions():
        """
        Provides any specific user permissions for a launch request
        """

    def set_user_privacy_attributes():
        """
        Provides any privacy info for protected user attributes
        """

    def set_result_url():
        """
        Provides a url for returning results
        """