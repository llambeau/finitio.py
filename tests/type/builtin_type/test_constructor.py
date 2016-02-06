#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_constructor
----------------------------------

Tests for the `BuiltinType` constructor.
"""

import unittest

from finitio.types import BuiltinType


class TestBuiltinTypeConstructor(unittest.TestCase):

    subject = BuiltinType(str)

    def test_it_should_set_instance_variables(self):
        self.assertEquals(self.subject.py_type, str)

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
