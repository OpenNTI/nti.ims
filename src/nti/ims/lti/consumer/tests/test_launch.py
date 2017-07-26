#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division

__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from hamcrest import assert_that
from hamcrest import is_

from nti.ims.lti.consumer.launch import ProviderToolFactory

class TestProviderToolFactory(object):

    def test_params(self):

        key = u'testkey'
        secret = u'testsecret'
        launch_url = 'http://test.com'
        title = u'Test Tool'
        required_params = {u'primary_user_id': u'A TestID',
                           u'secondary_user_id': u'A TestUniversityID',
                           u'return_url': u'The return url for the tool'}

        factory = ProviderToolFactory(key=key,
                                      secret=secret,
                                      launch_url=launch_url,
                                      title=title,
                                      required_params=required_params)

        assert_that(factory.key, is_(key))
        assert_that(factory.secret, is_(secret))
        assert_that(factory.launch_url, is_(launch_url))
        assert_that(factory.title, is_(title))
        assert_that(factory.required_params, is_(required_params))




