#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_equality
----------------------------------

Tests for the `SetType` __eq__ method
"""

import unittest

from tests.helpers import StrType, NumType
from finitio.types import SetType


class TestSetTypeEq(unittest.TestCase):

    _type = SetType(NumType)
    _type2 = SetType(NumType)
    _type3 = SetType(StrType)

    def test_it_should_apply_structural_equality(self):
        self.assertEquals(self._type, self._type2)

    def test_it_should_distinguish_different_types(self):
        self.assertNotEquals(self._type, self._type3)

    def test_it_should_be_a_total_function_with_null_for_non_types(self):
        self.assertNotEquals(self._type, 12)

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
