#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import has_item
from hamcrest import assert_that
from hamcrest import equal_to

import unittest

import os
import json


from nti.ims.lti.tool_provider import ToolProvider


def load_json(fname):
	path = os.path.join(os.path.dirname(__file__), fname)
	with open(path, "r") as f:
		content = f.read()
		if isinstance(content, bytes):
			content = unicode(content, 'utf-8')
	return content

def create_params(fname):
	content = load_json(fname)
	params = json.loads(content)
	return params

class TestToolProvider(unittest.TestCase):

	def test_launch_parameters_from_moodle(self):
		params = create_params('moodle_request_values_sample.json')
		consumer_key = 'key'
		consumer_secret = 'secret'
		TP = ToolProvider(consumer_key, consumer_secret, params)

		assert_that(hasattr(TP, 'lti_version'), equal_to(True))
		assert_that(hasattr(TP, 'lti_message_type'), equal_to(True))

		assert_that(hasattr(TP, 'oauth_signature'), equal_to(True))
		assert_that(hasattr(TP, 'oauth_nonce'), equal_to(True))
		assert_that(hasattr(TP, 'oauth_timestamp'), equal_to(True))
		assert_that(hasattr(TP, 'oauth_signature_method'), equal_to(True))
		assert_that(hasattr(TP, 'oauth_version'), equal_to(True))
		assert_that(hasattr(TP, 'oauth_consumer_key'), equal_to(True))
		assert_that(hasattr(TP, 'oauth_callback'), equal_to(True))

		assert_that(hasattr(TP, 'lis_outcome_service_url'), equal_to(True))
		assert_that(hasattr(TP, 'lis_result_sourcedid'), equal_to(True))
		assert_that(hasattr(TP, 'lis_person_name_family'), equal_to(True))
		assert_that(hasattr(TP, 'lis_person_contact_email_primary'), equal_to(True))
		assert_that(hasattr(TP, 'lis_person_name_given'), equal_to(True))
		assert_that(hasattr(TP, 'lis_person_name_full'), equal_to(True))

		assert_that(hasattr(TP, 'context_label'), equal_to(True))
		assert_that(hasattr(TP, 'context_title'), equal_to(True))
		assert_that(hasattr(TP, 'context_id'), equal_to(True))
		assert_that(hasattr(TP, 'context_type'), equal_to(True))

		assert_that(hasattr(TP, 'resource_link_id'), equal_to(True))
		assert_that(hasattr(TP, 'resource_link_title'), equal_to(True))

		assert_that(hasattr(TP, 'roles'), equal_to(True))

		assert_that(hasattr(TP, 'tool_consumer_info_version'), equal_to(True))
		assert_that(hasattr(TP, 'tool_consumer_instance_guid'), equal_to(True))
		assert_that(hasattr(TP, 'tool_consumer_instance_description'), equal_to(True))
		assert_that(hasattr(TP, 'tool_consumer_instance_name'), equal_to(True))
		assert_that(hasattr(TP, 'tool_consumer_info_product_family_code'), equal_to(True))
	
		assert_that(hasattr(TP, 'launch_presentation_locale'), equal_to(True))
		assert_that(hasattr(TP, 'launch_presentation_return_url'), equal_to(True))
		assert_that(hasattr(TP, 'launch_presentation_document_target'), equal_to(True))
		
		assert_that(hasattr(TP, 'ext_params'), equal_to(True))
		
		assert_that(TP.oauth_consumer_key, equal_to(consumer_key))

	def test_generated_outcome_service_request_for_moodle(self):
		params = create_params('moodle_request_values_sample.json')
		consumer_key = 'key'
		consumer_secret = 'secret'
		TP = ToolProvider(consumer_key, consumer_secret, params)

		assert_that(TP.lis_outcome_service_url, equal_to(u'http://localhost:8888/moodle31/mod/lti/service.php'))
		assert_that(TP.lis_result_sourcedid, equal_to(u'{"data":{"instanceid":"2","userid":"2","typeid":null,"launchid":1559272422},"hash":"cab2467ffa02f501386f24f3dcbe71999d30fde4ebc707afb4962152c432394a"}'))

		outcome_request_xml = TP.generate_outcome_request_xml()
		print(outcome_request_xml)
		
	def test_launch_parameters_from_edx(self):
		params = create_params('edx_request_values_sample.json')
		consumer_key = 'key'
		consumer_secret = 'secret'
		TP = ToolProvider(consumer_key, consumer_secret, params)
		assert_that(TP.lti_version, equal_to("LTI-1p0"))
		assert_that(TP.oauth_nonce, equal_to("104958806078703881061467622028"))
		assert_that(TP.lis_result_sourcedid, equal_to("course-v1%3AedX%2BDemoX%2BDemo_Course:-bf3da14a2fc2474382b9ac80ef1fd431:student"))
		assert_that(TP.context_id, equal_to("course-v1:edX+DemoX+Demo_Course"))
		assert_that(TP.oauth_signature_method, equal_to("HMAC-SHA1"))
		assert_that(TP.oauth_version, equal_to("1.0"))
		assert_that(TP.oauth_signature, equal_to("F8Pm3Qs4nhxQwyuK1f5/GVxpA9w="))
		assert_that(TP.lti_message_type, equal_to("basic-lti-launch-request"))
		assert_that(TP.resource_link_id, equal_to("-bf3da14a2fc2474382b9ac80ef1fd431"))
		assert_that(TP.user_id, equal_to("student"))
		assert_that(TP.roles, equal_to(["Instructor"]))
		assert_that(TP.oauth_consumer_key, equal_to("key"))
		assert_that(TP.oauth_timestamp, equal_to("1467622028"))
		assert_that(TP.lis_outcome_service_url, equal_to("/preview/xblock/block-v1:edX+DemoX+Demo_Course+type@lti_consumer+block@bf3da14a2fc2474382b9ac80ef1fd431/handler/outcome_service_handler"))
		assert_that(TP.oauth_callback, equal_to("about:blank"))
		
		
		
