#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

import os

import unittest

from hamcrest import assert_that 
from hamcrest import greater_than
from hamcrest import has_key

from nti.ims.lti.xml_config import LTIConfig

class TestToolConsumer(unittest.TestCase):

	@classmethod
	def _load_xml(cls, name):
		path = os.path.join(os.path.dirname(__file__), name)
		with open(path, "r") as f:
			content = f.read()
			if isinstance(content, bytes):
				content = unicode(content, 'utf-8')
		return content
	
	def test_parse_xml(self):
		xml_str = self._load_xml('cartridge_basiclti_link_1.xml')
		
		lti_config = LTIConfig()
		lti_config.parse(xml_str)

		assert_that(len(lti_config.blti_params), greater_than(0))
		assert_that(len(lti_config.custom_params), greater_than(0))
		assert_that(len(lti_config.ext_params), greater_than(0))
		assert_that(len(lti_config.cartridge_params), greater_than(0))

		assert_that(lti_config.blti_params, has_key('title'))
		assert_that(lti_config.blti_params, has_key('description'))
		assert_that(lti_config.blti_params, has_key('launch_url'))
		assert_that(lti_config.blti_params, has_key('secure_launch_url'))
		assert_that(lti_config.blti_params, has_key('icon'))
		assert_that(lti_config.blti_params, has_key('secure_icon'))
		assert_that(lti_config.blti_params, has_key('vendor_code'))
		assert_that(lti_config.blti_params, has_key('vendor_name'))
		assert_that(lti_config.blti_params, has_key('vendor_description'))
		assert_that(lti_config.blti_params, has_key('vendor_url'))
		assert_that(lti_config.blti_params, has_key('vendor_contact_email'))

		assert_that(lti_config.custom_params, has_key('keyname'))

		assert_that(lti_config.ext_params, has_key('my.lms.com'))

		assert_that(lti_config.cartridge_params, has_key('cartridge_bundle'))
		assert_that(lti_config.cartridge_params, has_key('cartridge_icon'))