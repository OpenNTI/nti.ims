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

try:
    _unicode = unicode
except NameError:  # python 3
    _unicode = lambda s: s


def to_unicode(s, encoding='utf-8', err='strict'):
    """
    Decode a byte sequence and unicode result
    """
    s = s.decode(encoding, err) if isinstance(s, bytes) else s
    return unicode(s) if s is not None else None


def get_text(node):
    if node is not None and node.text:
        text = node.text
        text = to_unicode(text)
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
