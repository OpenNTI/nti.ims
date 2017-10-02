#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# disable: accessing protected members, too many methods
# pylint: disable=W0212,R0904

from hamcrest import is_
from hamcrest import none
from hamcrest import assert_that

import unittest
from io import BytesIO

from nti.ims.sis.utils import get_fileobj

from nti.ims.tests import SharedConfiguringTestLayer


class TestUtils(unittest.TestCase):

    layer = SharedConfiguringTestLayer

    def test_get_fileobj(self):
        source = BytesIO()
        assert_that(get_fileobj(source), is_(source))
        
        source = 'a.bz2'
        with self.assertRaises(IOError):
            get_fileobj(source)
            
        source = object()
        assert_that(get_fileobj(source), is_(none()))