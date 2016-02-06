#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dress
----------------------------------

Tests for the `AnyType` dress method
"""

import unittest

from finitio.types import AnyType


class TestAnyTypeConstructor(unittest.TestCase):

    def subject(self, arg):
        return AnyType().dress(arg)

    def test_with_an_integer(self):
        self.assertEquals(self.subject(12), 12)

    def test_with_a_float(self):
        self.assertEquals(self.subject(3.14), 3.14)

    def test_with_a_string(self):
        self.assertEquals(self.subject(3.14), 3.14)

    def test_with_a_custom_object(self):
        class MyCustomClass:
            pass
        obj = MyCustomClass()
        self.assertEquals(self.subject(obj), obj)

    def test_with_none(self):
        self.assertEquals(self.subject(None), None)

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
