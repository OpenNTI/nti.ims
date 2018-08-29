#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from nti.base._compat import bytes_

from nti.externalization.datastructures import InterfaceObjectIO

from nti.ims.lti.consumer import PersistentToolConfig

from nti.ims.lti.interfaces import IConfiguredTool

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

    def updateFromExternalObject(self, parsed, *args, **kwargs):
        if 'config_xml' in parsed:  # This is the import case
            config = PersistentToolConfig.create_from_xml(bytes_(parsed['config_xml']))
            ext_self = self._ext_replacement()
            self._ext_setattr(ext_self, 'config', config)
            self._excluded_in_ivars_ = frozenset(('config',))
            # We previously checked to see if this tool was deleted here, but we have moved that
            # up into the container internalizer so that these objects are fully created when
            # we decorate conditional interfaces
        return super(_ConfiguredToolImportUpdater, self).updateFromExternalObject(parsed, *args, **kwargs)
