#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_include
----------------------------------

Tests for the `AnyType` include method
"""

import unittest

from finitio.types import AnyType


class TestAnyTypeEq(unittest.TestCase):

    subject = AnyType()

    def test_returns_true_when_included(self):
        self.assertEquals(self.subject.include('12'), True)
        self.assertEquals(self.subject.include(12), True)
        self.assertEquals(self.subject.include(12.4), True)
        self.assertEquals(self.subject.include(True), True)
        self.assertEquals(self.subject.include(None), True)


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
