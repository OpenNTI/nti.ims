#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Based on IMS Global Learning Tools Interoperability® Outcomes Management
http://www.imsglobal.org/specs/ltiomv1p0/specification
It is used to post grades back from other learning tools to the Tool Consumer

.. $Id: outcome_services.py 83134 2016-02-18 17:39:30Z carlos.sanchez $
"""
from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

try:
	from cStringIO import StringIO
except ImportError:
	from StringIO import StringIO

from lxml import objectify

from nti.common.string import to_unicode

NSMAP  = {
	'imsx_POXEnvelopeResponse' : 'http://www.imsglobal.org/services/ltiv1p1/xsd/imsoms_v1p0',
	'imsx_POXEnvelopeRequest'  : 'http://www.imsglobal.org/services/ltiv1p1/xsd/imsoms_v1p0'
}

CODE_MAJOR = ['success', 'processing', 'failure', 'unsupported']
SEVERITY_TYPE = ['status', 'warning', 'error']

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
		self.message_identifier = imsx_POXHeader.\
							 	  imsx_POXRequestHeaderInfo.\
							 	  imsx_messageIdentifier


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
		except:
			pass

class OutcomeRequest(object):
	"""
	Mainly used by Tool Provider 
	TODO :  -  script to check if launch params from TC has 'lis_outcome_service_url' and 'lis_result_sourcedid'
			-  script to generate xml sent to TC. A sourcedGUID provided in the 'lis_result_sourcedid' launch parameters.
			-  script to sign the request using OAuth 1.0 body signing.
			-  script to issue an HTTP POST request to the lis_outcome_service_url specified in the launch request that include the signed OAuth Authorization header
	"""
	pass
	


