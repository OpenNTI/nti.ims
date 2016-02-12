#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id: tool_consumer.py 60147 2015-02-24 22:31:22Z carlos.sanchez $
this module is adapted from https://github.com/tophatmonocle/ims_lti_py
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from collections import defaultdict
from urllib2 import urlparse, unquote

import oauth2
import time
from .launch_params import LaunchParamsMixin
from .utils import generate_identifier
from .utils import InvalidLTIRequestError



class ToolConsumer(LaunchParamsMixin, object):

	def __init__(self, consumer_key, consumer_secret, launch_url, params={}):
		self.consumer_key = consumer_key
		self.consumer_secret = consumer_secret
		self.launch_url = launch_url
		super(ToolConsumer, self).__init__()
		self.process_params(params)

	def _params_update(self):
		return{
			'oauth_nonce' : str(generate_identifier()),
			'oauth_timestamp' : str(int(time.time())),
		}

	def generate_launch_data(self):
		params = self.to_params()
		if not params.get('lti_version', None):
			params['lti_version'] = 'LTI-1p0'
		if not params.get('lti_message_type', None):
			params['lti_message_type'] = 'basic-lti-launch-request'

		consumer = oauth2.Consumer(key=self.consumer_key,
								   secret=self.consumer_secret)

		params.update(self._params_update())
		params.update({'oauth_consumer_key' : consumer.key})

		uri = urlparse.urlparse(self.launch_url)
		if uri.query != '':
			for param in uri.query.split('&'):
				key, val = param.split('=')
				if params.get(key) == None:
					params[key] = str(val)

		request = oauth2.Request(method='POST',
								 url=self.launch_url,
								 parameters=params)

		signature_method = oauth2.SignatureMethod_HMAC_SHA1()
		request.sign_request(signature_method, consumer, None)

		return_params = {}
		for key in request:
			if request[key] == None:
				return_params[key] = None
			elif isinstance(request[key], list):
				return_params[key] = request.get_parameter(key)
			else:
				return_params[key] = unquote(request.get_parameter(key))
		return return_params






