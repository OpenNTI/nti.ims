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

from zope.configuration.fields import GlobalObject

from nti.externalization.zcml import autoPackageExternalization

from nti.ims.qti.interfaces import IConcrete
from nti.ims.qti.basic.elements import QTIElement

def _item_predicate(item):
	implemented = getattr(item, '__implemented__', None)
	implemented = implemented.flattened() if implemented else ()
	result = bool(inspect.isclass(item) and issubclass(item, QTIElement) and \
				  item != QTIElement and IConcrete in implemented)
	return result

class IRegisterQTIElementsDirective(interface.Interface):
	module = GlobalObject(title="Module to scan for QTI elements to add",
						  required=True)

def registerQTIElements(_context, module):
	root_interfaces = []
	for name, item in inspect.getmembers(module, _item_predicate):
		root_iface = list(item.__implemented__.flattened())[0]
		__traceback_info__ = name, item, root_iface
		root_interfaces.append(root_iface)
	autoPackageExternalization(_context, root_interfaces, (module,))
