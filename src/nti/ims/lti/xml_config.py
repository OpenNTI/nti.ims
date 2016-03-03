#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Adapted from https://github.com/tophatmonocle/ims_lti_py

.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

try:
	from cStringIO import StringIO
except ImportError:
	from StringIO import StringIO

from lxml import etree

from nti.common.string import to_unicode

NSMAP = {
	'blti'  : 'http://www.imsglobal.org/xsd/imsbasiclti_v1p0',
	'lticm' : 'http://www.imsglobal.org/xsd/imslticm_v1p0',
	'lticp' : 'http://www.imsglobal.org/xsd/imslticp_v1p0',
	'xsi' 	: 'http://www.w3.org/2001/XMLSchema-instance',
	'lticc' : 'http://www.imsglobal.org/xsd/imslticc_v1p0'
}

etree_parse = getattr(etree, "parse")
etree_fromstring = getattr(etree, "fromstring")

class LTIConfig(object):

	def __init__(self):
		self.ext_params = {}
		self.blti_params = {}
		self.custom_params = {}
		self.cartridge_params = {}

	def parse(self, xml_source):
		if not hasattr(xml_source, 'read'):
			source = StringIO(xml_source)
		tree = etree_parse(source)
		root = tree.getroot()
		self.createFromElement(root)

	def createFromElement(self, element):
		blti_prefix = NSMAP['blti']
		lticc_prefix = NSMAP['lticc']
		for node in element:
			if node.tag == '{%s}title' % (blti_prefix):
				self.blti_params['title'] = to_unicode(node.text)
			elif node.tag == '{%s}description' % (blti_prefix):
				self.blti_params['description'] = to_unicode(node.text)
			elif node.tag == '{%s}secure_launch_url' % (blti_prefix):
				self.blti_params['secure_launch_url'] = to_unicode(node.text)
			elif node.tag == '{%s}secure_icon' % (blti_prefix):
				self.blti_params['secure_icon'] = to_unicode(node.text)
			elif node.tag == '{%s}launch_url' % (blti_prefix):
				self.blti_params['launch_url'] = to_unicode(node.text)
			elif node.tag == '{%s}icon' % (blti_prefix):
				self.blti_params['icon'] = to_unicode(node.text)
			elif node.tag == '{%s}vendor' % (blti_prefix):
				self.process_vendor(node)
			elif node.tag == '{%s}custom' % (blti_prefix):
				self.process_custom_params(node)
			elif node.tag == '{%s}extensions' % (blti_prefix):
				platform = to_unicode(node.attrib['platform'])
				self.ext_params[platform] = self.process_ext_params(node)
			elif node.tag == '{%s}cartridge_bundle' % lticc_prefix:
				if 'identifierref' in node.attrib:
					self.cartridge_params['cartridge_bundle'] = to_unicode(node.attrib['identifierref'])
			elif node.tag == '{%s}cartridge_icon' % lticc_prefix:
				if 'identifierref' in node.attrib:
					self.cartridge_params['cartridge_icon'] = to_unicode(node.attrib['identifierref'])
			else:
				logger.warn('Unhandled node: %s', node.tag)

	def process_vendor(self, element):
		lticp_prefix = NSMAP['lticp']
		for node in element:
			if node.tag == '{%s}code' % lticp_prefix:
				self.blti_params['vendor_code'] = to_unicode(node.text)
			elif node.tag == '{%s}description' % lticp_prefix:
				self.blti_params['vendor_description'] = to_unicode(node.text)
			elif node.tag == '{%s}name' % lticp_prefix:
				self.blti_params['vendor_name'] = to_unicode(node.text)
			elif node.tag == '{%s}url' % lticp_prefix:
				self.blti_params['vendor_url'] = to_unicode(node.text)
			elif node.tag == '{%s}contact' % lticp_prefix:
				for child in node:
					if child.tag == '{%s}name' % lticp_prefix:
						self.blti_params['vendor_contact_name'] = to_unicode(node.text)
					elif child.tag == '{%s}email' % lticp_prefix:
						self.blti_params['vendor_contact_email'] = to_unicode(node.text)
			else:
				logger.warn('Unhandled vendor node: %s', node.tag)

	def process_custom_params(self, element):
		for node in element:
			self.custom_params[node.attrib['name']] = to_unicode(node.text)

	def process_ext_params(self, element):
		params = {}
		lticm_prefix = NSMAP['lticm']
		for node in element:
			if node.tag == '{%s}property' % lticm_prefix:
				if 'name' in node.attrib:
					params[node.attrib['name']] = to_unicode(node.text)
				else:
					logger.warn('Unhandled extension property')
			elif node.tag == '{%s}options' % lticm_prefix:
				options = {}
				opt_name = node.attrib['name']
				for child in node:
					if 'name' in child.attrib:
						options[child.attrib['name']] = to_unicode(node.text)
					else:
						logger.warn('Unhandled extension option')
				params[opt_name] = options
			else:
				logger.warn('Unhandled extension node %s', node.tag)
		return params
