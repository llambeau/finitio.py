#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_include
----------------------------------

Tests for the `BuiltinType` include method
"""

import unittest

from numbers import Number
from finitio.types import BuiltinType


class TestBuiltinTypeEq(unittest.TestCase):

    subject = BuiltinType(Number)

    def test_returns_false_when_not_included(self):
        self.assertEquals(self.subject.include('12'), False)

    def test_returns_true_when_included(self):
        self.assertEquals(self.subject.include(12), True)

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
