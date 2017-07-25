#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division

__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from nti.base.interfaces import ITitled

from nti.schema.field import Dict
from nti.schema.field import HTTPURL
from nti.schema.field import TextLine


class IProviderTool(ITitled):
    """
    A provider tool utility
    """

    key = TextLine(title=u'The provider key',
                   required=True)

    secret = TextLine(title=u'The provider secret',
                      required=True)

    launch_url = HTTPURL(title=u'The launch url for a provider tool',
                         required=True)

    title = TextLine(title=u'A descriptive title for this provider tool',
                     required=True)

    # TODO a list/set may be a better option here
    required_params = Dict(title=u'A dict of required parameters for this provider tool',
                           description=u'A map of required parameters where the key is the parameter'
                                       u'and the value is a brief description'
                                       u'e.g {\'primary_user_id\': \'The primary user id\''
                                       u'     \'secondary_user_id\': \'The secondary user id\'',
                           required=True)

    def get_launch_request(params_map):
        """
        Launches the tool described in the utility
        The params_map must satisfy the required_params of the tool
        """
