#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904
import unittest
from hamcrest import assert_that
from hamcrest import has_item

from nti.ims.lti.tool_consumer import ToolConsumer


def create_params():
	return {
		'lti_message_type'  : 'basic-lti-launch-request',
		'lti_version'       : 'LTI-1p0',
		'resource_link_id'	: '88391-e1919-bb3456',
		'resource_link_title' : 'My Weekly Wiki',
		'resource_link_description' : 'A weekly blog.',
		'user_id' : '0ae836b9-7fc9-4060-006f-27b2066ac545',
		'user_image' : None,
		'lis_person_name_given' : 'John',
		'lis_person_name_family' : 'Doe',
		'lis_person_name_full' : 'John Doe',
		'lis_person_contact_email_primary' : 'john.doe@school.edu',
		'lis_person_sourcedid': 'school.edu:user',
		'lis_result_sourcedid' : 'feb-123-456-2929::28883',
		'lis_outcome_service_url' : 'http://www.imsglobal.org/developers/LTI/test/v1p1/common/tool_consumer_outcome.php?b64=MTIzNDU6OjpzZWNyZXQ',
		'lis_course_section_sourcedid' : 'school.edu:SI182-001-F08',
		'lis_course_offering_sourcedid' : 'school.edu:SI182-F08',
		'roles' : ['Instructor'],
		'role_scope_mentor' : ['f5b2cc6c-8c5c-24e8-75cc-fac504df920f'],
		'context_id' : '8213060-006f-27b2066ac545',
		'context_type' : 'CourseSection',
		'context_title' : 'Design of Personal Environments',
		'context_label' : 'SI182',
		'launch_presentation_locale' : 'en-US',
		'launch_presentation_document_target' : 'iframe',
		'launch_presentation_css_url' : 'http://www.imsglobal.org/developers/LTI/test/v1p1/lms.css',
		'launch_presentation_width' : 320,
		'launch_presentation_height' : 240,
		'launch_presentation_return_url' : 'http://lmsng.school.edu/portal/123/page/988/',
		'tool_consumer_info_product_family_code' : 'desire2learn',
		'tool_consumer_info_version' : '9.2.4',
		'tool_consumer_instance_guid' : 'lmsng.school.edu',
		'tool_consumer_instance_name' : 'SchoolU',
		'tool_consumer_instance_description' : 'University of School (LMSng)',
		'tool_consumer_instance_url' : 'http://lmsng.school.edu',
		'tool_consumer_instance_contact_email' : 'System.Admin@school.edu ',
		'custom_review_chapter' : '1.2.56',
	}

class TestToolConsumer(unittest.TestCase):
	
	def test_launch_data(self):
		params = create_params()
		consumer_key = '123456'
		consumer_secret = 'secret_123456'

		#The launch_url contains the URL to which the LTI Launch is to be sent
		launch_url = 'http://dr-chuck.com/ims/php-simple/tool.php'

		tc = ToolConsumer(consumer_key, consumer_secret, launch_url, params)
		launch_data = tc.generate_launch_data()
		assert_that(launch_data, has_item('oauth_consumer_key'))
		assert_that(launch_data, has_item('oauth_signature_method'))
		assert_that(launch_data, has_item('oauth_timestamp'))
		assert_that(launch_data, has_item('oauth_nonce'))
		assert_that(launch_data, has_item('oauth_version'))
		assert_that(launch_data, has_item('oauth_signature'))
		assert_that(launch_data, has_item('oauth_callback'))
		assert_that(launch_data, has_item('lti_version'))
		assert_that(launch_data, has_item('lti_message_type'))

		