#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Directives to be used in ZCML; helpers for registering QTI elements.

.. $Id$
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

import inspect

from zope import interface
from zope.configuration import fields
from zope.dottedname.resolve import resolve

from nti.externalization.zcml import autoPackageExternalization

from .basic.elements import QTIElement

from . import interfaces as qti_interfaces

def _item_predicate(item):
	implemented = getattr(item, '__implemented__', None)
	implemented = implemented.flattened() if implemented else ()
	return  inspect.isclass(item) and issubclass(item, QTIElement) and item != QTIElement and \
			qti_interfaces.IConcrete in implemented

class IRegisterQTIElementsDirective(interface.Interface):
	module = fields.GlobalObject(title="Module to scan for QTI elements to add", required=True)

def registerQTIElements(_context, module):
	for name, item in inspect.getmembers(module, _item_predicate):
		__traceback_info__ = name, item
		module = resolve(item.__module__)
		io_interface = list(item.__implemented__.flattened())[0]
		autoPackageExternalization(_context, (io_interface,), (module,))

