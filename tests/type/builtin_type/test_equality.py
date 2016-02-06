#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_equality
----------------------------------

Tests for the `BuiltinType` __eq__ method
"""

import unittest

from numbers import Number
from finitio.types import BuiltinType


class TestBuiltinTypeEq(unittest.TestCase):

    num_type = BuiltinType(Number)
    num_type2 = BuiltinType(Number)
    str_type = BuiltinType(str)

    def test_it_should_apply_structural_equality(self):
        self.assertEquals(self.num_type, self.num_type2)

    def test_it_should_distinguish_different_types(self):
        self.assertNotEquals(self.num_type, self.str_type)

    def test_it_should_be_a_total_function_with_null_for_non_types(self):
        self.assertNotEquals(self.num_type, 12)

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
