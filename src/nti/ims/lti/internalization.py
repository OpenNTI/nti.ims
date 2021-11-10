#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from zope import interface

from nti.base._compat import bytes_
from nti.base._compat import text_

from nti.externalization.datastructures import InterfaceObjectIO

from nti.externalization.internalization import update_from_external_object

from nti.ims.lti import SUPPORTED_LTI_EXTENSIONS

from nti.ims.lti.consumer import LTIExtension
from nti.ims.lti.consumer import PersistentToolConfig

from nti.ims.lti.interfaces import IConfiguredTool
from nti.ims.lti.interfaces import IDeepLinking
from nti.ims.lti.interfaces import IExternalToolLinkSelection

logger = __import__('logging').getLogger(__name__)


class _ConfiguredToolImportUpdater(InterfaceObjectIO):

    _ext_iface_upper_bound = IConfiguredTool

    # We are creating these from an import and we want to preserve
    # their old id so we can find them later on in the container
    # to update the ExternalToolAsset
    def _ext_accept_external_id(self, unused_ext_self, parsed):
        if 'config_xml' in parsed:  # This is the import case
            return True
        return False

    def _get_extensions(self, config):
        extensions = []
        for (platform_key, param_keys) in SUPPORTED_LTI_EXTENSIONS.items():
            for param_key in param_keys:
                params = config.get_ext_param(platform_key, param_key)
                if params:
                    extension = LTIExtension(platform_key=platform_key, param_key=param_key)
                    # These extensions are byte arrays and must be converted into a text type
                    # to properly internalize
                    params = {key: text_(value) for (key, value) in params.items()}
                    update_from_external_object(extension, params)
                    # Mark the extension type
                    # XXX: Ordering this after the extension has went through internalization is important
                    # as marker interfaces don't play nicely with the interface derivation mechanism
                    if params.get('message_type') == 'ContentItemSelectionRequest':
                        interface.alsoProvides(extension, IDeepLinking)
                    else:
                        interface.alsoProvides(extension, IExternalToolLinkSelection)
                    extensions.append(extension)
        return extensions

    def updateFromExternalObject(self, parsed, *args, **kwargs):
        config = parsed.get(u'config')  # This will only be None in the import case, in which we define below
        if 'config_xml' in parsed:  # This is the import case
            config = PersistentToolConfig.create_from_xml(bytes_(parsed['config_xml']))
            ext_self = self._ext_replacement()
            self._ext_setattr(ext_self, 'config', config)
            self._excluded_in_ivars_ = frozenset(('config',))
            # We previously checked to see if this tool was deleted here, but we have moved that
            # up into the container internalizer so that these objects are fully created when
            # we decorate conditional interfaces
        extensions = self._get_extensions(config)
        parsed['extensions'] = extensions
        return super(_ConfiguredToolImportUpdater, self).updateFromExternalObject(parsed, *args, **kwargs)
