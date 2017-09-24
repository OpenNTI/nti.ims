#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import bz2
import six
import gzip
import codecs
import mimetypes

from nti.base._compat import text_

logger = __import__('logging').getLogger(__name__)


def get_text(node):
    if node is not None and node.text:
        text = node.text
        text = text_(text)
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
            fileobj = codecs.open(source, "r", "utf-8")
        return fileobj
    return None
