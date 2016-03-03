#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Based on IMS Global Learning Tools Interoperability® Outcomes Management
http://www.imsglobal.org/specs/ltiomv1p0/specification
It is used to post grades back from other learning tools to the Tool Consumer

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
from lxml import objectify

from nti.common.string import to_unicode

NSMAP = {
	'imsx_POXEnvelopeResponse' : 'http://www.imsglobal.org/services/ltiv1p1/xsd/imsoms_v1p0',
	'imsx_POXEnvelopeRequest'  : 'http://www.imsglobal.org/services/ltiv1p1/xsd/imsoms_v1p0'
}

CODE_MAJOR = ['success', 'processing', 'failure', 'unsupported']
SEVERITY_TYPE = ['status', 'warning', 'error']

etree_element = getattr(etree, "Element")
etree_tostring = getattr(etree, "tostring")
etree_sub_element = getattr(etree, "SubElement")

objectify_parse = getattr(objectify, "parse")

class OutcomeResponse(object):
	"""
	Mainly used by Tool Consumer.
	TC needs to implement 'lis_outcome_service_url' endpoint for the purpose of receiving grading callbacks from TP
	LTI Outcome Management Service specification version 1.0 (updated Jan 2015) describes three types of outcome services : replaceResult, readResult and deleteResult
	TC parse request from TP and send response back to TP.

	TODO :
	- decide if TC will support all the outcome services (replaceResult, readResult and deleteResult)
	"""

	def __init__(self):
		self.outcome_service_type = None

	def parse(self, xml_source):
		"""
		process Plain Old XML received from TP
		"""
		if not hasattr(xml_source, 'read'):
			source = StringIO(xml_source)

		tree = objectify_parse(source)
		root = tree.getroot()

		self.request_ns = NSMAP['imsx_POXEnvelopeRequest']
		if root.tag == '{%s}imsx_POXEnvelopeRequest' % self.request_ns:
			for node in root.getchildren():
				if node.tag == '{%s}imsx_POXHeader' % self.request_ns :
					self.process_imsx_pox_request_header(node)
				elif node.tag == '{%s}imsx_POXBody' % self.request_ns:
					self.process_imsx_pox_body(node)

	def process_imsx_pox_request_header(self, imsx_POXHeader):
		try:
			self.message_identifier = imsx_POXHeader.\
								 	  imsx_POXRequestHeaderInfo.\
								 	  imsx_messageIdentifier
			self.imsx_version = imsx_POXHeader.\
								imsx_POXRequestHeaderInfo.\
								imsx_version
		except AttributeError:
			pass

	def process_imsx_pox_body(self, element):
		node = element.getchildren()[0]
		self.result_record = {}
		if node.tag == '{%s}replaceResultRequest' % self.request_ns:
			self.outcome_service_type = 'replaceResult'
		elif node.tag == '{%s}readResultRequest' % self.request_ns:
			self.outcome_service_type = 'readResult'
		elif node.tag == '{%s}deleteResultRequest' % self.request_ns:
			self.outcome_service_type = 'deleteResult'
		else:
			logger.warn('Unrecognized outcome service type : %s', node.tag)
		self.process_result_record(node)

	def process_result_record(self, element):
		try:
			if self.outcome_service_type is not None:
				if self.outcome_service_type == 'replaceResult':
					self.result_record['score'] = element.resultRecord.result.resultScore.textString
				self.result_record['sourcedGUID'] = to_unicode(element.resultRecord.sourcedGUID.sourcedId)
		except Exception:
			pass

	def generate_response_xml(self,
							  imsx_version,
							  code_major_type,
							  severity_type,
							  message_identifier,
							  description=None,
							  language='en',
							  score=None):
		"""
		generate response xml that will be sent back to TP
		"""
		self.code_major_type = code_major_type
		self.severity_type = severity_type
		self.response_message_identifier = message_identifier
		self.description = description
		self.language = language
		self.score = score

		if self.imsx_version == imsx_version:
			response_ns = NSMAP['imsx_POXEnvelopeResponse']
			root = etree_element('imsx_POXEnvelopeResponse', xmlns=response_ns)
			root = self.set_response_pox_header(root)
			root = self.set_response_pox_body(root)

		return '<?xml version="1.0" encoding="UTF-8"?>' + etree_tostring(root)

	def set_response_pox_header(self, root):
		header = etree_sub_element(root, 'imsx_POXHeader')
		header_info = etree_sub_element(header, 'imsx_POXResponseHeaderInfo')

		version = etree_sub_element(header_info, 'imsx_version')
		version.text = to_unicode(self.imsx_version)

		message_identifier = etree_sub_element(header_info, 'imsx_messageIdentifier')
		message_identifier.text = to_unicode(self.response_message_identifier)

		header_info = self.set_response_status_info(header_info)
		return root

	def set_response_status_info(self, header_info):
		status_info = etree_sub_element(header_info, 'imsx_statusInfo')
		code_major = etree_sub_element(status_info, 'imsx_codeMajor')
		if self.code_major_type in CODE_MAJOR:
			code_major.text = to_unicode(self.code_major_type)

		severity = etree_sub_element(status_info, 'imsx_severity')
		if self.severity_type in SEVERITY_TYPE:
			severity.text = to_unicode(self.severity_type)

		if self.description is not None:
			description = etree_sub_element(status_info, 'imsx_description')
			description.text = to_unicode(self.description)

		message_ref_identifier = etree_sub_element(status_info, 'imsx_messageRefIdentifier')
		message_ref_identifier.text = to_unicode(self.message_identifier)

		operation_ref_identifier = etree_sub_element(status_info, 'imsx_operationRefIdentifier')
		operation_ref_identifier.text = to_unicode(self.outcome_service_type)
		return header_info

	def set_response_pox_body(self, root):
		body = etree_sub_element(root, 'imsx_POXBody')
		if self.outcome_service_type == 'replaceResult':
			outcome_response = etree_sub_element(body, 'replaceResultResponse')
		elif self.outcome_service_type == 'readResult':
			outcome_response = etree_sub_element(body, 'readResultResponse')
			result = etree_sub_element(outcome_response, 'result')
			result_score = etree_sub_element(result, 'resultScore')
			language = etree_sub_element(result_score, 'language')
			language.text = to_unicode(self.language)
			text_string = etree_sub_element(result_score, 'textString')
			text_string.text = to_unicode(self.score)
		elif self.outcome_service_type == 'deleteResult':
			outcome_response = etree_sub_element(body, 'deleteResultResponse')
		return root

class OutcomeRequest(object):
	"""
	Mainly used by Tool Provider
	TODO:  -  script to check if launch params from TC has 'lis_outcome_service_url' and 'lis_result_sourcedid'
		   -  script to generate xml sent to TC. A sourcedGUID provided in the 'lis_result_sourcedid' launch parameters.
		   -  script to sign the request using OAuth 1.0 body signing.
		   -  script to issue an HTTP POST request to the lis_outcome_service_url specified in the launch request that include the signed OAuth Authorization header
	"""
	pass
