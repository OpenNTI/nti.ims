#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# pylint: disable=inherit-non-class

from zope import interface

from zope.container.constraints import contains
from zope.container.interfaces import IContainer

from zope.location.interfaces import IContained

from nti.base.interfaces import ITitled
from nti.base.interfaces import ITitledDescribed

from nti.schema.field import Dict
from nti.schema.field import Int
from nti.schema.field import List
from nti.schema.field import Number
from nti.schema.field import Object
from nti.schema.field import HTTPURL
from nti.schema.field import Text
from nti.schema.field import TextLine
from nti.schema.field import DateTime
from nti.schema.field import Float


class IOAuthConsumer(ITitled):

    key = TextLine(title=u'The consumer key',
                   required=True)

    secret = TextLine(title=u'The consumer secret',
                      required=True)

    title = TextLine(title=u'A descriptive title for this consumer',
                     required=True)


class IOAuthConsumers(interface.Interface):
    """
    A mapping type which stores IOAuthConsumer implementations
    by their key.
    """

    def __getitem__(key):
        """
        Returns the IOAuthConsumer for the given key
        """

    def __setitem__(key, consumer):
        """
        Sets the IOAuthConsumer for the given key
        """

    def __delitem__(key):
        """
        Removes the IOAuthConsumer for the given key
        """


class ITool(ITitledDescribed):
    """
    Describes a tool in the lti sense.  This works in conjunction.
    """


class IToolConfig(interface.Interface):
    """
    An object providing configuration information for launching a tool.
    This is typically used to render an LTI Common Cartridge xml snippet
    for configuring the tool inside a consumer.
    """

    title = TextLine(title=u'The title for the Tool Config',
                     required=True)

    description = Text(title=u'The description for the Tool Config',
                       required=False)

    launch_url = HTTPURL(title=u'A URL for launching an LTI Tool',
                         required=True)

    secure_launch_url = HTTPURL(title=u'A secure URL for launching an LTI Tool',
                                required=False)

    icon = HTTPURL(title=u'The icon for the lti tool',
                   required=False)


class IToolConfigFactory(interface.Interface):
    """
    A callable that is capable of generating an IToolConfig.  These
    are typically registered as adapters on ITool.
    """

    def __call__():
        """
        Returns an IToolConfig object.
        """


class IToolConfigBuilder(interface.Interface):
    """
    A subscriber interface to configure IToolConfig
    for specific tools
    """

    def configure(config):
        """
        Configures the IToolConfig
        :return IToolConfig
        """


class IToolConsumerUserProperties(interface.Interface):

    user_id = TextLine(title=u'A unique identifier for the user',
                       required=False)

    user_image = HTTPURL(title=u'A URL to a user image',
                         required=False)

    role = List(title=u'A list of URN values for roles',
                required=False)


class IToolConsumerMessageProperties(interface.Interface):

    message_type = TextLine(title=u'The type of LTI message',
                            required=True)

    version = Number(title=u'The LTI version being used',
                     required=True)

    resource_link_id = TextLine(title=u'A unique resource identifier',
                                required=True)

    resource_link_title = TextLine(title=u'A title for the resource',
                                   required=False)

    resource_link_desc = TextLine(title=u'A description for the resource',
                                  required=False)


class IToolConsumerLISProperties(interface.Interface):

    lis_person_name_given = TextLine(title=u'The given name of the user',
                                     required=False)

    lis_person_name_family = TextLine(title=u'The family name of the user',
                                      required=False)

    lis_person_name_full = TextLine(title=u'The full name of the user',
                                    required=False)

    lis_person_contact_email_primary = TextLine(title=u'The email address of the user',
                                                required=False)

    role_scope_mentor = List(title=u'A list of user_id values the current user can access as a mentor',
                             required=False)


class IToolConsumerContextProperties(interface.Interface):

    context_id = TextLine(title=u'A opaque identifier that uniquely identifies the context that contains the link'
                                u'being launched',
                          required=False)

    context_type = List(title=u'A list of URN values that identify the context of the content',
                        required=False)

    context_title = TextLine(title=u'The title of the context',
                             required=False)

    context_label = TextLine(title=u'The label for the context -- intended to fit in a table',
                             required=False)


class IToolConsumerPresentationProperties(interface.Interface):

    presentation_locale = TextLine(title=u'The BCP-47 language, country, and variant tag',
                                   required=False)

    presentation_target = TextLine(title=u'The kind of browser window/frame where the provider is being launched'
                                         u' from (iframe, window, or frame',
                                   required=False)

    presentation_css_url = HTTPURL(title=u'A URL to a LMS specific CSS file',
                                   required=False)

    presentation_width = Number(title=u'The width of the window or frame where the content will be displayed',
                                required=False)

    presentation_height = Number(title=u'The height of the window or frame where the content will be displayed',
                                 required=False)

    presentation_return_url = HTTPURL(title=u'The URL the provider can redirect the user back to the consumer '
                                            u'interface',
                                      required=False)


class IToolConsumerInstanceProperties(interface.Interface):

    tc_info_product_family_code = TextLine(title=u'The product name of the consumer',
                                           required=False)

    tc_info_version = TextLine(title=u'The version of the consumer',
                               required=False)

    tc_instance_guid = TextLine(title=u'A unique identifier for the consumer instance',
                                required=False)

    tc_instance_name = TextLine(title=u'The name of the consumer instance (likely the school name)',
                                required=False)

    tc_instance_description = TextLine(title=u'A description of the consumer instance',
                                       required=False)

    tc_instance_url = HTTPURL(title=u'The URL of the consumer instance',
                              required=False)

    tc_instance_contact_email = TextLine(title=u'An email contact for the consumer instance',
                                         required=False)


class IToolConsumerFieldExtensions(interface.Interface):

    field_extensions = Dict(title=u'A dictionary of consumer specific '
                            u'launch message extensions')


class IToolConsumerCustomValues(interface.Interface):

    custom_values = Dict(title=u'A dictionary of consumer specific '
                         u'custom values')


class IToolConsumerInstanceBuilder(interface.Interface):

    def build(launch_request):
        """
        Builds and returns a tool consumer instance
        """


class IConfiguredTool(IContained):

    consumer_key = TextLine(title=u'The provider key',
                            required=True)

    secret = TextLine(title=u'The provider secret',
                      required=True)

    config = Object(IToolConfig,
                    required=True)

    selection_width = Int(title=u'The iframe width for resource selection',
                             required=False)

    selection_height = Int(title=u'The iframe height for resource selection',
                              required=False)


class IConfiguredToolContainer(IContainer):

    contains(IConfiguredTool)

    def add_tool(tool):
        """
        add a configuration tool
        """

    def delete_tool(tool):
        """
        remove the specified configuration tool
        """


class IDeepLinking(interface.Interface):
    """
    A marker interface for IConfiguredTool indicating that the tool is using Deep Linking
    https://www.imsglobal.org/specs/lticiv1p0-intro
    """


class IExternalToolLinkSelection(interface.Interface):
    """
    A marker interface for IConfiguredTool indicating that the tool is using Canvas ExternalToolLinkSelection
    https://canvas.instructure.com/doc/api/file.link_selection_tools.html
    """


class IOutcomeService(interface.Interface):
    """
    Provides a mechanism for recording, fetching, and removing lti
    launch outcomes for a user. This is based on LTI `Basic Outcome Service`.
    Adaptable from a `IResultSourcedId`.

    https://www.imsglobal.org/spec/lti-bo/v1p1#basic-outcome-service
    """

    def set_score(score):
        """
        Set the score. Score must be a numeric float in the
        range [0.0, 1,0].

        https://www.imsglobal.org/spec/lti-bo/v1p1#replaceresult
        """

    def get_score():
        """
        Get the score for the provided principal.
        If a score has not been set, None is returned.
        """

    def remove_score():
        """
        Delete the score.
        """


class IResultSourcedId(interface.Interface):
    """
    An identifier that uniquely represents a user and lti resource for
    the LTI Basic Outcome Service.

    https://www.imsglobal.org/spec/lti-bo/v1p1#replaceresult

    When processing an outcome service action, this can be adapted to
    an IOutcomeService and something adapting to IPrincipal.
    """

    lis_result_sourcedid = TextLine(title=u'LIS Result Identifier',
                                    required=True)


class IOutcomeResponse(interface.Interface):
    """
    An outcome service response to be returned to users of the service
    """


class IOutcomeRequest(interface.Interface):
    """
    Represents a request to be made to the outcome service.
    """
    result_id = Object(IResultSourcedId,
                       title=u'The result id this request is for',
                       required=True)

    def __call__():
        """
        Invoke the request returning an IOutcomeResponse.
        Subinterfaces may choose to return more specific interfaces
        """


class IOutcomeReadRequest(IOutcomeRequest):
    """
    A request to read a value from the outcome service.
    """


class IOutcomeReplaceRequest(IOutcomeRequest):
    """
    A request to replace a value in the outcome service.
    """
    score_val = Float(title=u'The score',
                      required=False,
                      min=0.0,
                      max=1.0)


class IOutcomeDeleteRequest(IOutcomeRequest):
    """
    A request to delete a value from the outcome service.
    """


class ILTIUserLaunchStats(interface.Interface):
    """
    An adapter interface providing LTI launch statistics.
    """

    LaunchCount = Int(title=u'The number of LTI launches',
                      default=0,
                      required=True)

    LastLaunchDate = DateTime(title=u'The last launch date',
                              required=False)
