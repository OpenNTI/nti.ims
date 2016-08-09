#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
OAuthentication for LTI Integration

OAuth Signing based on: https://groups.google.com/forum/#!searchin/edx-code/lti/edx-code/Ys7UJO2KcSw/tgnES3pesVQJ

.. $Id$

"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"
from oauthlib.oauth1.rfc5849 import signature
from oauthlib.oauth1.rfc5849.utils import escape
from oauthlib.oauth1.rfc5849.signature import collect_parameters
import base64
from hashlib import sha1
from uuid import uuid4
import time
import requests

logger = __import__('logging').getLogger(__name__)


key = u'key'
CLIENT_KEY = u'key'
CLIENT_SECRET = 'secret'

def send_grade(provider, outcome):

	#grades are always sent to the consumer request's "lis_outcome_service_url"
	post_to = provider.params['lis_outcome_service_url'][0]

	#body hash is required for a valid signature on request to consumer
	body_hash = (base64.b64encode(sha1(outcome).digest()).decode("utf-8"))

	oauth_args = [("oauth_body_hash", body_hash),("oauth_consumer_key", key),("oauth_nonce", uuid4().hex.decode('utf-8')),
        ("oauth_signature_method", u"HMAC-SHA1"),("oauth_timestamp", str(int(time.time())).decode('utf-8')), ("oauth_version", u"1.0")]

	params = signature.normalize_parameters(oauth_args)
	base_string = signature.construct_base_string("POST", post_to, params)

	#all of the consumers should use this signature type, but you can check the 
	#consumer's signature method in the parameters from their initial request.
	sig = signature.sign_hmac_sha1(base_string, "secret", "")

	oauth_header = (", ".join(['%s="%s"' % items for items in oauth_args]))
	oauth_header += ', oauth_signature="%s"' % escape(sig)
	headers = {'Content-Type': "application/xml",'Authorization': "OAuth %s" % oauth_header}
	return requests.post(post_to, headers=headers, data=outcome)


def validate_request(request_vals):
	# print (request_vals)
	key = request_vals['oauth_consumer_key']
	# print (key)
	if (key[0] == CLIENT_KEY):
		return True
	else:
		return False


