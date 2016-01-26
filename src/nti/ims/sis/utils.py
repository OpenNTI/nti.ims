#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, unicode_literals, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

import bz2
import six
import gzip
import mimetypes

from nti.common.string import safestr

def get_text(node):
	if node is not None and node.text:
		text = node.text
		text = safestr(text)
		return text
	return None

def get_fileobj(source):
	if hasattr(source, 'read'):
		return source
	elif isinstance(source, six.string_types):
		mimetype = mimetypes.guess_type(source)
		if mimetype[1] == 'gzip':
			fileobj = gzip.GzipFile(source)
		elif mimetype[1] == 'bzip2':
			fileobj = bz2.BZ2File(source)
		else:
			fileobj = open(source)
		return fileobj
	return None
