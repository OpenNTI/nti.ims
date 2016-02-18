#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import has_item
from hamcrest import assert_that

import unittest
from nti.ims.lti.xml_config import LTIConfig

import textwrap
from lxml import etree
xml_str = textwrap.dedent("""<?xml version="1.0" encoding="UTF-8"?>
	<cartridge_basiclti_link xmlns="http://www.imsglobal.org/xsd/imslticc_v1p0" xmlns:blti="http://www.imsglobal.org/xsd/imsbasiclti_v1p0" xmlns:lticm="http://www.imsglobal.org/xsd/imslticm_v1p0" xmlns:lticp="http://www.imsglobal.org/xsd/imslticp_v1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imslticc_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticc_v1p0.xsd  http://www.imsglobal.org/xsd/imsbasiclti_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imsbasiclti_v1p0.xsd  http://www.imsglobal.org/xsd/imslticm_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticm_v1p0.xsd  http://www.imsglobal.org/xsd/imslticp_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticp_v1p0.xsd">
	   <blti:title>Grade Book</blti:title>
	   <blti:description>Grade Book with many column types</blti:description>
	   <blti:custom>
	      <lticm:property name="keyname">value</lticm:property>
	   </blti:custom>
	   <blti:extensions platform="my.lms.com">
	      <lticm:property name="keyname">value</lticm:property>
	   </blti:extensions>
	   <blti:launch_url>url to the basiclti launch URL</blti:launch_url>
	   <blti:secure_launch_url>secure url to the basiclti launch URL</blti:secure_launch_url>
	   <blti:icon>url to an icon for this tool (optional)</blti:icon>
	   <blti:secure_icon>secure url to an icon for this tool (optional)&gt;</blti:secure_icon>
	   <blti:vendor>
	      <lticp:code>vendor.com</lticp:code>
	      <lticp:name>vendor.name</lticp:name>
	      <lticp:description>This is a vendor of learning tools.</lticp:description>
	      <lticp:url>http://www.vendor.com/</lticp:url>
	      <lticp:contact>
	         <lticp:email>support@vendor.com</lticp:email>
	      </lticp:contact>
	   </blti:vendor>
	   <cartridge_bundle identifierref="BLTI001_Bundle" />
	   <cartridge_icon identifierref="BLTI001_Icon" />
	</cartridge_basiclti_link>
	""")

xml_str2 = '<?xml version="1.0" encoding="UTF-8"?>\n\t<cartridge_basiclti_link xmlns="http://www.imsglobal.org/xsd/imslticc_v1p0" xmlns:blti="http://www.imsglobal.org/xsd/imsbasiclti_v1p0" xmlns:lticm="http://www.imsglobal.org/xsd/imslticm_v1p0" xmlns:lticp="http://www.imsglobal.org/xsd/imslticp_v1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imslticc_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticc_v1p0.xsd  http://www.imsglobal.org/xsd/imsbasiclti_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imsbasiclti_v1p0.xsd  http://www.imsglobal.org/xsd/imslticm_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticm_v1p0.xsd  http://www.imsglobal.org/xsd/imslticp_v1p0 http://www.imsglobal.org/xsd/lti/ltiv1p0/imslticp_v1p0.xsd">\n\t   <blti:title>Grade Book</blti:title>\n\t   <blti:description>Grade Book with many column types</blti:description>\n\t   <blti:custom>\n\t      <lticm:property name="keyname">value</lticm:property>\n\t   </blti:custom>\n\t   <blti:extensions platform="my.lms.com">\n\t      <lticm:property name="keyname">value</lticm:property>\n\t   </blti:extensions>\n\t   <blti:launch_url>url to the basiclti launch URL</blti:launch_url>\n\t   <blti:secure_launch_url>secure url to the basiclti launch URL</blti:secure_launch_url>\n\t   <blti:icon>url to an icon for this tool (optional)</blti:icon>\n\t   <blti:secure_icon>secure url to an icon for this tool (optional)&gt;</blti:secure_icon>\n\t   <blti:vendor>\n\t      <lticp:code>vendor.com</lticp:code>\n\t      <lticp:name>vendor.name</lticp:name>\n\t      <lticp:description>This is a vendor of learning tools.</lticp:description>\n\t      <lticp:url>http://www.vendor.com/</lticp:url>\n\t      <lticp:contact>\n\t         <lticp:email>support@vendor.com</lticp:email>\n\t      </lticp:contact>\n\t   </blti:vendor>\n\t   <cartridge_bundle identifierref="BLTI001_Bundle" />\n\t   <cartridge_icon identifierref="BLTI001_Icon" />\n\t</cartridge_basiclti_link>\n'

class TestToolConsumer(unittest.TestCase):

	def test_parse_xml(self):
		#TODO : fix the following line before calling LTIConfig
		root = etree.fromstring(xml_str)