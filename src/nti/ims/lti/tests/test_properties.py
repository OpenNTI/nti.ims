#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import is_
from hamcrest import has_length
from hamcrest import assert_that

from zope import interface

from nti.ims.lti.interfaces import IToolConsumerCustomValues
from nti.ims.lti.interfaces import IToolConsumerLISProperties
from nti.ims.lti.interfaces import IToolConsumerUserProperties
from nti.ims.lti.interfaces import IToolConsumerFieldExtensions
from nti.ims.lti.interfaces import IToolConsumerContextProperties
from nti.ims.lti.interfaces import IToolConsumerMessageProperties
from nti.ims.lti.interfaces import IToolConsumerInstanceProperties
from nti.ims.lti.interfaces import IToolConsumerPresentationProperties

import nti.testing.base


@interface.implementer(IToolConsumerUserProperties)
class FakeToolConsumerUserProperties(object):

    user_id = 'fake1'

    user_image = 'http://www.fake.com/test'

    role = ['test', 'fake']


@interface.implementer(IToolConsumerMessageProperties)
class FakeToolConsumerMessageProperties(object):

    message_type = 'fake'

    version = 111

    resource_link_id = 'fake_resource'

    resource_link_title = 'fake resource title'

    resource_link_desc = 'fake resource description'


@interface.implementer(IToolConsumerLISProperties)
class FakeToolConsumerLISProperties(object):

    lis_person_name_given = 'Test'

    lis_person_name_family = 'Name'

    lis_person_name_full = 'Test Name'

    lis_person_contact_email_primary = 'name@test.com'

    role_scope_mentor = ['fake1', 'test2']


@interface.implementer(IToolConsumerContextProperties)
class FakeToolConsumerContextProperties(object):

    context_id = 'test'

    context_type = ['fake', 'fake1']

    context_title = 'fake title'

    context_label = 'fake label'


@interface.implementer(IToolConsumerPresentationProperties)
class FakeToolConsumerPresentationProperties(object):

    presentation_locale = 'us'

    presentation_target = 'iframe'

    presentation_css_url = 'http://www.example.com'

    presentation_width = 123

    presentation_height = 456

    presentation_return_url = 'http://www.examplereturn.com'


@interface.implementer(IToolConsumerInstanceProperties)
class FakeToolConsumerInstanceProperties(object):

    tc_info_product_family_code = 'test'

    tc_info_version = '1.2.3'

    tc_instance_guid = 'fake'

    tc_instance_name = 'fake name'

    tc_instance_description = 'fake description'

    tc_instance_url = 'http://www.fakeurl.com'

    tc_instance_contact_email = 'fake@test.com'


@interface.implementer(IToolConsumerFieldExtensions)
class FakeToolConsumerFieldExtensions(object):

    field_extensions = {'fake': 0}


@interface.implementer(IToolConsumerCustomValues)
class FakeToolConsumerCustomValues(object):

    custom_values = {'fake': 1}


class TestConfigFactory(nti.testing.base.ConfiguringTestBase):

    def test_basic_attributes(self):

        user = FakeToolConsumerUserProperties()
        message = FakeToolConsumerMessageProperties()
        lis = FakeToolConsumerLISProperties()
        context = FakeToolConsumerContextProperties()
        pres = FakeToolConsumerPresentationProperties()
        inst = FakeToolConsumerInstanceProperties()
        field = FakeToolConsumerFieldExtensions()
        custom = FakeToolConsumerCustomValues()

        assert_that(user.user_id, is_(user.user_id))
        assert_that(user.user_image, is_(user.user_image))
        assert_that(user.role, has_length(2))

        assert_that(context.context_type, is_(context.context_type))
        assert_that(context.context_type, has_length(2))
        assert_that(context.context_type[0], is_(context.context_type[0]))

        assert_that(pres.presentation_target, is_(pres.presentation_target))

        assert_that(pres.presentation_width, is_(123))

        assert_that(custom.custom_values['fake'],
                    is_(custom.custom_values['fake']))

        assert_that(field.field_extensions['fake'],
                    is_(field.field_extensions['fake']))

        assert_that(inst.tc_info_product_family_code,
                    is_(inst.tc_info_product_family_code))

        assert_that(lis.lis_person_contact_email_primary,
                    is_(lis.lis_person_contact_email_primary))

        assert_that(message.message_type, is_(message.message_type))
