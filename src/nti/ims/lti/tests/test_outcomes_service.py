#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904
from hamcrest import has_key
from hamcrest import equal_to
from hamcrest import assert_that

import os

import unittest

from nti.ims.lti.outcomes_service import OutcomeResponse

class TestOutcomeResponse(unittest.TestCase):

	@classmethod
	def _load_xml(cls, name):
		path = os.path.join(os.path.dirname(__file__), name)
		with open(path, "r") as f:
			content = f.read()
			if isinstance(content, bytes):
				content = unicode(content, 'utf-8')
		return content

	def test_parse_replace_result_xml(self):
		xml = self._load_xml('replace_result_request.xml')
		outcome_response = OutcomeResponse()
		outcome_response.parse(xml)
		assert_that(outcome_response.message_identifier, equal_to(999999123))
		assert_that(outcome_response.outcome_service_type, equal_to('replaceResult'))
		assert_that(outcome_response.result_record, has_key('score'))
		assert_that(outcome_response.result_record['score'], equal_to(0.92))
		assert_that(outcome_response.result_record, has_key('sourcedGUID'))
		assert_that(outcome_response.result_record['sourcedGUID'], equal_to(u'3124567'))

	def test_parse_read_result_xml(self):
		xml = self._load_xml('read_result_request.xml')
		outcome_response = OutcomeResponse()
		outcome_response.parse(xml)
		assert_that(outcome_response.message_identifier, equal_to(999999123))
		assert_that(outcome_response.outcome_service_type, equal_to('readResult'))
		assert_that(outcome_response.result_record, has_key('sourcedGUID'))
		assert_that(outcome_response.result_record['sourcedGUID'], equal_to(u'3124567'))

	def test_parse_delete_result_xml(self):
		xml = self._load_xml('delete_result_request.xml')
		outcome_response = OutcomeResponse()
		outcome_response.parse(xml)
		assert_that(outcome_response.message_identifier, equal_to(999999123))
		assert_that(outcome_response.outcome_service_type, equal_to('deleteResult'))
		assert_that(outcome_response.result_record, has_key('sourcedGUID'))
		assert_that(outcome_response.result_record['sourcedGUID'], equal_to(u'3124567'))
