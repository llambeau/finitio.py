#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dress
----------------------------------

Tests for the `BuiltinType` dress method
"""

import unittest

from numbers import Number
from finitio.types import BuiltinType
from finitio.exceptions import DressError


class TestBuiltinTypeConstructor(unittest.TestCase):

    def subject(self, arg):
        return BuiltinType(Number).dress(arg)

    def test_is_robust_enough(self):
        with self.assertRaises(DressError):
            self.subject(None)

    def test_with_an_integer(self):
        self.assertEquals(self.subject(12), 12)

    def test_with_a_float(self):
        self.assertEquals(self.subject(3.14), 3.14)

    def test_with_a_str_it_raises_error(self):
        with self.assertRaisesRegexp(DressError,
                                     'Invalid Number: `Hello World`'):
            self.subject('Hello World')

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
