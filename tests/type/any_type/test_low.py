#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_equality
----------------------------------

Tests for the `AnyType` low() method
"""

import unittest

from finitio.types import AnyType


class TestAnyTypeLow(unittest.TestCase):

    subject = AnyType()

    def test_equals_itself(self):
        self.assertIs(self.subject.low(), self.subject)

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
