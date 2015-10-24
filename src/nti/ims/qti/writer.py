#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

from lxml import etree

ns_map = {'xmlns':"http://www.imsglobal.org/xsd/imsqti_v2p0"}

etree_Element = getattr(etree, 'Element')
etree_ElementTree = getattr(etree, 'ElementTree')

def _write_attribs(element, a_map):
	for k, v in a_map.items():
		if k and v is not None:
			element.set(unicode(k), unicode(v))

def write(item, target=None):

	def _process_element(item, write_ns=False):
		name = item._name
		if write_ns:
			element = etree_Element(name, nsmap=ns_map)
		else:
			element = etree_Element(name)

		attribs = item.get_attributes()
		_write_attribs(element, attribs)

		element.tail = item._tail
		element.text = item._text

		children = item.get_children()
		if item.is_finite_sequence:
			for c in item:
				pe = _process_element(c)
				element.append(pe)
		else:
			for k, v in children.items():
				if item.is_list(k):
					for c in v:
						if c is not None:
							pe = _process_element(c)
							element.append(pe)
				elif item.is_field(k) and v is not None:
					pe = _process_element(v)
					element.append(pe)
				else:
					logger.debug("Unrecognized element '%s'" % k)

		return element

	result = _process_element(item, True)
	if target is not None:
		tree = etree_ElementTree(result)
		tree.write(target)
	return result
