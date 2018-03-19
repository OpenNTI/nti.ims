#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

# pylint: disable=protected-access,too-many-public-methods

from hamcrest import is_
from hamcrest import none
from hamcrest import assert_that

import unittest
from io import BytesIO

from nti.ims.sis.utils import get_fileobj
from nti.ims.sis.utils import parse_mktime

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

    def test_parse_maketime(self):
        assert_that(parse_mktime('2015-08-31'), is_(1440979200))
        assert_that(parse_mktime('2015-12-18'), is_(1450396800))
