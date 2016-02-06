#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_include
----------------------------------

Tests for the `SetType` include method
"""

import unittest

from tests.helpers import StrType
from finitio.types import SetType


class TestSetTypeInclude(unittest.TestCase):

    subject = SetType(StrType)

    def test_included_on_empty_array_is_true(self):
        self.assertEquals(self.subject.include([]), True)

    def test_included_on_empty_set_is_true(self):
        self.assertEquals(self.subject.include(set([])), True)

    def test_included_on_wrong_value_fails(self):
        self.assertEquals(self.subject.include("string"), False)
        self.assertEquals(self.subject.include(1), False)
        self.assertEquals(self.subject.include({}), False)

    def test_with_array_of_wrong_types_fails(self):
        self.assertEquals(self.subject.include([1, 2, 3]), False)

    def test_with_set_of_wrong_types_fails(self):
        self.assertEquals(self.subject.include(set([1, 2, 3])), False)

    def test_with_duplicate_fails(self):
        self.assertEquals(self.subject.include([1, 2, 3, 3]), False)


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
