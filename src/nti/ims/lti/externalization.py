#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, absolute_import, division

from nti.externalization.datastructures import InterfaceObjectIO

from nti.ims.lti.interfaces import IConfiguredTool

__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)


class _ConfiguredToolExternalizer(InterfaceObjectIO):

    _ext_iface_upper_bound = IConfiguredTool

    _excluded_out_ivars_ = ('config', 'secret')

    def toExternalObject(self, **kwargs):  # pylint: disable=arguments-differ
        context = self._ext_replacement()
        result = super(_ConfiguredToolExternalizer, self).toExternalObject(**kwargs)
        result['title'] = context.title
        result['description'] = context.description
        result['launch_url'] = context.launch_url
        result['secure_launch_url'] = context.secure_launch_url
        return result


class _ConfiguredToolExportExternalizer(InterfaceObjectIO):

    _ext_iface_upper_bound = IConfiguredTool

    def toExternalObject(self, **kwargs): # pylint: disable=arguments-differ
        context = self._ext_replacement()
        result = super(_ConfiguredToolExportExternalizer, self).toExternalObject(**kwargs)
        result['config'] = context.config.to_xml()  # Externalize the config as XML for parity with how it pickles
        return result