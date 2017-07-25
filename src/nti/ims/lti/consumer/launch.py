#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division

__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from lti.tool_outbound import ToolOutbound

from zope import interface

from nti.ims.lti.consumer.interfaces import IProviderTool

from nti.schema.field import SchemaConfigured

from nti.schema.fieldproperty import createDirectFieldProperties


NTI_PARAM_MAPPING = {u'firstname':          u'lis_person_name_given',
                     u'lastname':           u'lis_person_name_family',
                     u'fullname':           u'lis_person_name_full',
                     u'primary_id':         u'lis_person_sourcedid',
                     u'email':              u'lis_person_contact_email_primary',
                     u'user_image':         u'user_image',
                     u'roles':              u'roles',
                     u'locale':             u'launch_presentation_locale',
                     u'target':             u'launch_presentation_document_target',
                     u'return_url':         u'launch_presentation_return_url',
                     u'version':            u'tool_consumer_info_version',
                     u'organization':       u'tool_consumer_instance_guid', # this needs a better name
                     u'school':             u'tool_consumer_instance_name',
                     u'school_description': u'tool_consumer_instance_description',
                     u'school_url':         u'tool_consumer_instance_url',
                     u'school_admin':       u'tool_consumer_instance_contact_email',
                     u'course_name':        u'context_title',
                     u'course_number':      u'context_label'}


@interface.implementer(IProviderTool)
class ProviderToolFactory(SchemaConfigured):
    createDirectFieldProperties(IProviderTool)

    def get_launch_request(self, params_map):

        self._check_required_params(params_map)

        launch_params = {}

        for param in params_map:
            lti_param_name = NTI_PARAM_MAPPING[param]
            launch_params[lti_param_name] = params_map[param]

        # TODO guessing there is a library used for this
        unique_id = scramble(params_map[u'primary_id'])
        unique_context = scramble(u'random')
        unique_resource = scramble(u'resource')

        launch_params[u'user_id'] = unique_id
        launch_params[u'context_id'] = unique_context
        launch_params[u'resource_link_id'] = unique_resource

        tool = ToolOutbound(self.consumer_key,
                            self.consumer_secret,
                            launch_params,
                            self.launch_url)

        launch_request = tool.generate_launch_request()

        return launch_request

    def _check_required_params(self, params_map):

        for required_field in self.required_params:
            # TODO this would be better as a specific exception class
            if required_field not in params_map:
                raise Exception

