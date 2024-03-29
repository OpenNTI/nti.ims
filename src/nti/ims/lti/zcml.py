#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# pylint: disable=inherit-non-class

from base64 import b64decode

from functools import partial

from zope import interface

from zope.component.zcml import utility

from zope.schema import TextLine

from nti.base._compat import text_

from nti.common.cypher import get_plaintext

from nti.ims.lti.interfaces import IOAuthConsumer

from nti.ims.lti.oauth import OAuthConsumer

CYPHER_PASSPHRASE = b64decode('ZWlueXlhc3JiYnd5YkYzR0xOTXIyNGhyTFFvcEx3')

logger = __import__('logging').getLogger(__name__)


class IRegisterOAuthConsumer(interface.Interface):

    key = TextLine(title=u"The consumer key", required=True)

    secret = TextLine(title=u"The consumer secret as cypher",
                      required=True)

    title = TextLine(title=u"A descriptive title for the consumer",
                     required=True)


def registerConsumer(_context, key, secret, title):
    # this is really just security by obscurity here...
    secret = get_plaintext(secret, passphrase=CYPHER_PASSPHRASE)
    factory = partial(OAuthConsumer,
                      key=text_(key),
                      secret=text_(secret),
                      title=text_(title))
    utility(_context, provides=IOAuthConsumer, factory=factory, name=key)
