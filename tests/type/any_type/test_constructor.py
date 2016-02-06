#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_constructor
----------------------------------

Tests for the `AnyType` constructor.
"""

import unittest

from finitio.types import AnyType


class TestBuiltinTypeConstructor(unittest.TestCase):

    subject = AnyType()

    def test_it_should_create_an_AnyType_instance(self):
        self.assertIsInstance(self.subject, AnyType)

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
