#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Adapted from https://github.com/tophatmonocle/ims_lti_py

.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

import ast

from collections import defaultdict

from nti.common.string import to_unicode

LAUNCH_DATA_PARAMS = [
	'lti_message_type',
	'lti_version',
	'resource_link_id',
	'resource_link_title',
	'resource_link_description',
	'user_id', #Uniquely identifies the user. This should not contain any identifying information for the user. 
	'user_image',
	'lis_person_name_given',
	'lis_person_name_family',
	'lis_person_name_full',
	'lis_person_contact_email_primary',
	'lis_person_sourcedid',
	'lis_result_sourcedid', #This param along with lis_outcome_service_url param must be defined in order to support grade return from the TP to the TC using the Basic Outcomes service
	'lis_outcome_service_url', #This is an endpoint implemented by the Tool Consumer for the purpose of receiving grading callbacks. The TP can expect that there is a one-to-one mapping between the lis_outcome_service_url and a particular oauth_consumer_key.
	'lis_course_section_sourcedid',
	'lis_course_offering_sourcedid',
	'roles',
	'role_scope_mentor',
	'context_id',
	'context_type',
	'context_title',
	'context_label',
	'launch_presentation_locale',
	'launch_presentation_document_target',
	'launch_presentation_css_url',
	'launch_presentation_width',
	'launch_presentation_height',
	'launch_presentation_return_url',
	'tool_consumer_info_product_family_code',
	'tool_consumer_info_version',
	'tool_consumer_instance_guid',
	'tool_consumer_instance_name',
	'tool_consumer_instance_description',
	'tool_consumer_instance_url',
	'tool_consumer_instance_contact_email'
]

OAUTH_PARAMS = [
	'oauth_consumer_key',
	'oauth_signature_method',
	'oauth_timestamp',
	'oauth_nonce',
	'oauth_version',
	'oauth_signature',
	'oauth_callback'
]

REQUIRED_PARAMS = [
	'lti_message_type',
	'lti_version',
	'resource_link_id',
]

class LaunchParamsMixin(object):

	def __init__(self):
		self.launch_params = LAUNCH_DATA_PARAMS + OAUTH_PARAMS
		for param in self.launch_params:
			setattr(self, param, None)
		self.ext_params = defaultdict(lambda: None)
		self.custom_params = defaultdict(lambda: None)

	def process_params(self, params):
		"""
		populate launch parameters from params dictionary
		"""
		items = params.items() if hasattr(params, "items") else ()
		for key, val in items:
			if key in self.launch_params and val is not None:
				if key == 'roles':
					if isinstance(val, (tuple, list, set)):
						self.roles = list(val)
					else:
						self.roles = val.split(',')
				else:
					value = self.process_param_value(val)
					setattr(self, key, value)
			elif 'custom_' in key:
				self.custom_params[key] = to_unicode(val)
			elif'ext_' in key:
				self.ext_params[key] = to_unicode(val)

	def process_param_value(self, value):
		if isinstance(value, list):
			if len(value) == 1:
				if not isinstance(value[0], str) and not isinstance(value[0], unicode):
					logger.info('Unhandled parameter list value')
					logger.info(value[0])
					value = to_unicode(value[0])
				else:
					value = value[0]
			else:
				logger.info('parameter value is a list and it has more than one item')
				logger.info(value)
		elif isinstance(value, str) or isinstance(value, unicode):
			value = to_unicode(value)
		else:
			logger.info('Unhandled parameter value')
			logger.info(value)
		return value

	def to_params(self):
		"""
		create a new dictionary of all launch data.
		"""
		params = {}
		for key in self.launch_params:
			if hasattr(self, key):
				params[key] = getattr(self, key)
		custom_params = dict(self.custom_params)
		params.update(custom_params)
		ext_params = dict(self.ext_params)
		params.update(ext_params)
		return params
