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

from nti.ims.lti.tool_provider import ToolProvider

def create_params_moodle():
	return {'ext_lms': [u'moodle-2'], 'lis_result_sourcedid': [u'{"data":{"instanceid":"2","userid":"2","typeid":null,"launchid":163267342},"hash":"5dc2f4a7d91147c714e79c74fc3c0f40f0b3e79758e36d5a24907a874c8b0d3d"}'], 'context_id': [u'2'], 'tool_consumer_info_version': [u'2016052300.04'], 'tool_consumer_instance_guid': [u'localhost'], 'oauth_signature': [u'm1j3JLAAEC9KysnUrGqIvaCF8KM='], 'context_label': [u'About'], 'lti_message_type': [u'basic-lti-launch-request'], 'ext_user_username': [u'admin'], 'lis_person_name_full': [u'- Admin -'], 'context_title': [u'About Moodle4Mac'], 'user_id': [u'2'], 'tool_consumer_instance_description': [u'Moodle 3.1'], 'oauth_consumer_key': [u'key'], 'launch_presentation_locale': [u'en'], 'lis_outcome_service_url': [u'http://localhost:8888/moodle31/mod/lti/service.php'], 'resource_link_title': [u'NTI_LTI'], 'oauth_callback': [u'about:blank'], 'lis_person_name_family': [u'-'], 'oauth_nonce': [u'80f8a04db6526007ff614c0aeb6f321c'], 'oauth_timestamp': [u'1467096170'], 'oauth_signature_method': [u'HMAC-SHA1'], 'oauth_version': [u'1.0'], 'lis_person_contact_email_primary': [u'admin@localhost'], 'tool_consumer_instance_name': [u'Moodle 3.1'], 'resource_link_id': [u'2'], 'tool_consumer_info_product_family_code': [u'moodle'], 'roles': [u'Instructor,urn:lti:sysrole:ims/lis/Administrator,urn:lti:instrole:ims/lis/Administrator'], 'context_type': [u'CourseSection'], 'lti_version': [u'LTI-1p0'], 'lis_person_name_given': [u'- Admin'], 'launch_presentation_return_url': [u'http://localhost:8888/moodle31/mod/lti/return.php?course=2&launch_container=3&instanceid=2&sesskey=ZLRo9M4mJd'], 'launch_presentation_document_target': [u'iframe']}

class TestToolProvider(unittest.TestCase):

	def test_launch_parameters_from_moodle(self):
		params = create_params_moodle()
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
		
		#assert_that(hasattr(TP, 'ext_user_username'), equal_to(True))
		#assert_that(hasattr(TP, 'userid'), equal_to(True))
		#assert_that(hasattr(TP, 'ext_lms'), equal_to(True))
		
		
		
		
		
		
		
