#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
OAuthentication for LTI Integration

Using example flask OAuth2 Server

.. $Id$

"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

# try:
# 	from cStringIO import StringIO
# except ImportError:
# 	from StringIO import StringIO
# 
# import requests
# 
# from lxml import etree
# from lxml import objectify
# 
# from nti.common.string import to_unicode

# from requests_oauthlib import OAuth1

CLIENT_KEY = 'key'
CLIENT_SECRET = 'secret'
"""
oauth = OAuth(app)
#Note that the URLs here come from the OAuth Server, so maybe eventually NTI dataserver
remote = oauth.remote_app(
	'remote',
	consumer_key=CLIENT_KEY,
	consumer_secret=CLIENT_SECRET,
	base_url='http://127.0.0.1:5000/api/',
	request_token_url='http://127.0.0.1:5000/oauth/request_token',
	access_token_method='GET',
	access_token_url='http://127.0.0.1:5000/oauth/access_token',
	authorize_url='http://127.0.0.1:5000/oauth/authorize',
)
"""

"""
class OAuthService(object):
	def __init__(self):
		self.key = "key"
		self.secret = "secret"
"""
def authorized():
# 	url = 'http://127.0.0.1:5000/oauth/authorize'
# 	auth = OAuth1("", "secret", "", "")
	# remote.authorize(callback=url_for('authorized', _external=True))
	return None

def validate_request(request_vals):
	# print (request_vals)
	key = request_vals['oauth_consumer_key']
	# print (key)
	if (key[0] == CLIENT_KEY):
		return True
	else:
		return False

"""
nti_client = OAuth2Service( client_id='random_id',
	client_secret='random_secret',
	name='nti_client',
	authorize_url='',
	access_token_url='',
	base_url='')
"""
