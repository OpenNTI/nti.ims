#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import is_
from hamcrest import assert_that
from hamcrest import has_property

from ims_lti_py.outcome_request import OutcomeRequest

import unittest

class TestLTI(unittest.TestCase):

	def test_outcome_request(self):	
		params= {'lis_result_sourcedid':u'98913544378c4022bc938edb57fe79a2:::dyJ86SiwwA9',
				 'consumer_key':'jisc.ac.uk',
				 'consumer_secret':'secret',
				 'message_identifier': u'53ac7390b65e5',
				 'lis_outcome_service_url': 'http://ltiapps.net/test/tc-outcomes.php'}	
		outcome = OutcomeRequest(opts=params)
		result = outcome.post_read_result()
		assert_that(result, has_property('severity', is_('status')))
		assert_that(result, has_property('code_major', is_('failure')))
