#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_constructor
----------------------------------

Tests for the `SetType` constructor.
"""

import unittest

from finitio.types import SetType
from tests.helpers import IntType


class TestSetTypeConstructor(unittest.TestCase):

    subject = SetType(IntType)

    def test_it_should_be_an_instanceof_SetType(self):
        self.assertIsInstance(self.subject, SetType)

    def test_it_should_set_instance_variables(self):
        self.assertEquals(self.subject.element_type, IntType)

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
