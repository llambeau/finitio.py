#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dress
----------------------------------

Tests for the `SetType` dress method
"""

import unittest

from tests.helpers import IntType
from finitio.types import SetType
from finitio.exceptions import DressError


class TestSetTypeDress(unittest.TestCase):

    def subject(self, arg):
        return SetType(IntType).dress(arg)

    def test_dresses_empty_arrays(self):
        self.assertEquals(self.subject([]), [])

    def test_dresses_non_empty_arrays(self):
        self.assertEquals(self.subject([1, 2, 3]), [1, 2, 3])

    def test_dresses_empty_sets(self):
        self.assertEquals(self.subject(set([])), [])

    def test_dresses_non_empty_sets(self):
        self.assertEquals(self.subject(set([1, 2, 3])), [1, 2, 3])

    def test_dresses_with_non_sets_or_arrays(self):
        with self.assertRaisesRegexp(DressError, 'set/list expected, got `1`'):
            self.subject(1)

    def test_dresses_complains_about_non_Int_in_array(self):
        with self.assertRaises(DressError):
            self.subject(set([1, "str", 2]))

    def test_dresses_complains_and_sets_root_cause(self):
        try:
            self.subject(set([1, "str", 2]))
        except DressError as err:
            self.assertEquals(err.root_cause().message,
                              "Invalid Integral: `str`")

    def test_dresses_of_array_with_duplicates_raises_exception(self):
        try:
            self.subject([1, 1, 2])
        except DressError as err:
            self.assertEquals(err.root_cause().message,
                              "Duplicate values: `1`")

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
