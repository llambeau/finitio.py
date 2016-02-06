#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_equality
----------------------------------

Tests for the `AnyType` __eq__ method
"""

import unittest

from finitio.types import AnyType


class TestAnyTypeEq(unittest.TestCase):

    _type = AnyType()
    _type2 = AnyType()

    def test_it_should_apply_structural_equality(self):
        self.assertEquals(self._type, self._type2)

    def test_it_should_be_a_total_function_with_null_for_non_types(self):
        self.assertNotEquals(self._type, 12)

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
