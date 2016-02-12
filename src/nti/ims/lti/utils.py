#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from uuid import uuid1

def generate_identifier():
	return str(uuid1())

class LTIException(Exception):
	pass

class InvalidLTIConfigError(LTIException):

	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)

class InvalidLTIRequestError(LTIException):

	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)
