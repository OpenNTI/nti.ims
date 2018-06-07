#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from nti.dataserver.interfaces import IDeletedObjectPlaceholder

from nti.externalization.datastructures import InterfaceObjectIO

from nti.ims.lti.consumer import PersistentToolConfig

from nti.ims.lti.interfaces import IConfiguredTool

__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)


class _ConfiguredToolImportUpdater(InterfaceObjectIO):

    _ext_iface_upper_bound = IConfiguredTool

    def updateFromExternalObject(self, parsed, *args, **kwargs):
        if 'config_xml' in parsed:  # This is the import case
            from IPython.core.debugger import Tracer;Tracer()()
            config = PersistentToolConfig.create_from_xml(parsed['config_xml'])
            ext_self = self._ext_replacement()
            self._ext_setattr(ext_self, 'config', config)
            self._excluded_in_ivars_ = 'config'
            if parsed['deleted']:
                ext_self.alsoProvides(IDeletedObjectPlaceholder)
        result = super(_ConfiguredToolImportUpdater, self).updateFromExternalObject(parsed, *args, **kwargs)
        return result