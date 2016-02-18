#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

import os

import unittest

from lxml import etree

etree_fromstring = getattr(etree, "fromstring")

class TestToolConsumer(unittest.TestCase):

	@classmethod
	def _load_xml(cls, name):
		path = os.path.join(os.path.dirname(__file__), name)
		with open(path, "r") as f:
			content = f.read()
			if isinstance(content, bytes):
				content = unicode(content, 'utf-8')
		return etree_fromstring(content)
	
	def test_parse_xml(self):
		# TODO: fix the following line before calling LTIConfig
		self._load_xml('cartridge_basiclti_link.xml')
