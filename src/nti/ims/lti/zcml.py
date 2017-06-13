#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

import base64

from functools import partial

from zope import interface
from zope import schema

from zope.component.zcml import utility
from zope.configuration import fields

from nti.base._compat import text_

from nti.utils.cypher import get_plaintext

from .interfaces import IOAuthConsumer
from .oauth import OAuthConsumer

CYPHER_PASSPHRASE = base64.b64decode('ZWlueXlhc3JiYnd5YkYzR0xOTXIyNGhyTFFvcEx3')

class IRegisterOAuthConsumer(interface.Interface):
	key = fields.TextLine(title=u"The consumer key", required=True)
	secret = fields.TextLine(title=u"The consumer secret as cypher", required=True)
	title = fields.TextLine(title=u"A descriptive title for the consumer", required=True)

def registerConsumer(_context, key, secret, title):
	secret = get_plaintext(secret, passphrase=CYPHER_PASSPHRASE) #this is really just security by obscurity here...
	factory = partial(OAuthConsumer, key=text_(key), secret=text_(secret), title=text_(title))
	utility(_context, provides=IOAuthConsumer, factory=factory, name=key)

