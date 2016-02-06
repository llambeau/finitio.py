#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_equality
----------------------------------

Tests for the `BuiltinType` low() method
"""

import unittest

from numbers import Number
from finitio.types import BuiltinType


class TestBuiltinTypeLow(unittest.TestCase):

    subject = BuiltinType(Number)

    def test_equals_itself(self):
        self.assertIs(self.subject.low(), self.subject)

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
