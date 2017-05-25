#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
.. $Id$
"""

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

import bz2
import six
import gzip
import codecs
import mimetypes

try:
    _unicode = unicode
except NameError:  # python 3
    def _unicode(s): return str(s)


def text_(s, encoding='utf-8', err='strict'):
    """
    Decode a byte sequence and unicode result
    """
    s = s.decode(encoding, err) if isinstance(s, bytes) else s
    return _unicode(s) if s is not None else None
unicode_ = to_unicode = text_


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
