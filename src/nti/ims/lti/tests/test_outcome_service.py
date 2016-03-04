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

from nti.ims.lti.outcome_service import OutcomeRequest
from nti.ims.lti.outcome_service import OutcomeResponse

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

	def test_generate_response_xml_replace_result(self):
		xml = self._load_xml('replace_result_request.xml')
		outcome_response = OutcomeResponse()
		outcome_response.parse(xml)
		imsx_version = 'V1.0'
		code_major_type = 'success'
		severity_type = 'status'
		message_identifier = 4560
		description = 'Score for 3124567 is now 0.92'
		_ = outcome_response.generate_response_xml(
										imsx_version,
										code_major_type,
										severity_type,
										message_identifier,
										description=description,
										language='en',
										score=None)

	def test_generate_response_xml_read_result(self):
		xml = self._load_xml('read_result_request.xml')
		outcome_response = OutcomeResponse()
		outcome_response.parse(xml)
		imsx_version = 'V1.0'
		code_major_type = 'success'
		severity_type = 'status'
		message_identifier = 1313355158804
		description = 'Result read'
		score = 0.91
		_ = outcome_response.generate_response_xml(
										imsx_version,
										code_major_type,
										severity_type,
										message_identifier,
										description=description,
										language='en',
										score=score)

	def test_generate_response_xml_delete_result(self):
		xml = self._load_xml('delete_result_request.xml')
		outcome_response = OutcomeResponse()
		outcome_response.parse(xml)
		imsx_version = 'V1.0'
		code_major_type = 'success'
		severity_type = 'status'
		message_identifier = 4560
		_ = outcome_response.generate_response_xml(
										imsx_version,
										code_major_type,
										severity_type,
										message_identifier,
										description=None,
										language='en',
										score=None)

def create_outcome_request_accessors():
	accessors = {}
	accessors['lis_outcome_service_url'] = 'http://www.imsglobal.org/developers/LTI/test/v1p1/common/tool_consumer_outcome.php?b64=MTIzNDU6OjpzZWNyZXQ'
	accessors['lis_result_sourcedid'] = 'feb-123-456-2929::28883'
	accessors['consumer_key'] = '123456'
	accessors['consumer_secret'] = 'secret_123456'
	accessors['message_identifier'] = 999999123
	return accessors

class TestOutcomeRequest(unittest.TestCase):

	def test_generate_request_xml_replace_result(self):
		accessors = create_outcome_request_accessors()
		outcome_service_type = 'replaceResult'
		outcome_request = OutcomeRequest(accessors['lis_outcome_service_url'],
										 accessors['lis_result_sourcedid'] ,
										 accessors['consumer_key'],
										 accessors['consumer_secret'],
										 outcome_service_type,
										 accessors['message_identifier'],
								  		)
		outcome_request.score = 0.92
		_ = outcome_request.generate_request_xml()

	def test_generate_request_xml_read_result(self):
		accessors = create_outcome_request_accessors()
		outcome_service_type = 'readResult'
		outcome_request = OutcomeRequest(accessors['lis_outcome_service_url'],
										 accessors['lis_result_sourcedid'] ,
										 accessors['consumer_key'],
										 accessors['consumer_secret'],
										 outcome_service_type,
										 accessors['message_identifier'],
								  		)
		outcome_request.score = None
		_ = outcome_request.generate_request_xml()

	def test_generate_request_xml_delete_result(self):
		accessors = create_outcome_request_accessors()
		outcome_service_type = 'deleteResult'
		outcome_request = OutcomeRequest(accessors['lis_outcome_service_url'],
										 accessors['lis_result_sourcedid'] ,
										 accessors['consumer_key'],
										 accessors['consumer_secret'],
										 outcome_service_type,
										 accessors['message_identifier'],
								  		)
		outcome_request.score = None
		_ = outcome_request.generate_request_xml()
