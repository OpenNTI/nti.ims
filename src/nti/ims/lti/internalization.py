#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division

from nti.externalization.datastructures import InterfaceObjectIO

from nti.ims.lti.consumer import PersistentToolConfig

from nti.ims.lti.interfaces import IConfiguredTool

__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)


class _ConfiguredToolImportUpdater(InterfaceObjectIO):

    _ext_iface_upper_bound = IConfiguredTool
    _excluded_in_ivars_ = 'config'

    def updateFromExternalObject(self, parsed, *args, **kwargs):
        config = PersistentToolConfig.create_from_xml(parsed['config'])
        ext_self = self._ext_replacement()
        self._ext_setattr(ext_self, 'config', config)
        result = super(_ConfiguredToolImportUpdater, self).updateFromExternalObject(parsed, *args, **kwargs)
        return result