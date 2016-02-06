#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_equality
----------------------------------

Tests for the `BuiltinType` __repr__ method
"""

import unittest

from numbers import Number
from finitio.types import BuiltinType


class TestBuiltinTypeStr(unittest.TestCase):

    num_type = BuiltinType(Number)
    str_type = BuiltinType(str)

    def test_it_gives_the_correct_repr(self):
        self.assertEquals(str(self.num_type), '.Number')
        self.assertEquals(str(self.str_type), '.str')


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
