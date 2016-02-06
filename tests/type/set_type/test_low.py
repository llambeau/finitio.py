#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_equality
----------------------------------


Tests for the `SetType` low() method
"""

import unittest

from finitio.types import SetType, BuiltinType, Type

builtin_string = BuiltinType(str)


class TestSetTypeLow(unittest.TestCase):

    class HighType(Type):
        def low(self):
            return builtin_string

    subject = SetType(HighType(""))

    def test_equals_itself(self):
        expected = SetType(builtin_string)
        self.assertEqual(self.subject.low(), expected)

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
