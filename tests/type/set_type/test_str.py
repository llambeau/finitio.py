#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_equality
----------------------------------

Tests for the `SetType` __repr__ method
"""

import unittest

from tests.helpers import NumType, StrType
from finitio.types import SetType, AnyType


class TestSetTypeStr(unittest.TestCase):

    set_num = SetType(NumType)
    set_str = SetType(StrType)
    set_any = SetType(AnyType())

    def test_it_gives_the_correct_repr(self):
        self.assertEquals(str(self.set_num), '{.Number}')
        self.assertEquals(str(self.set_str), '{.str}')
        self.assertEquals(str(self.set_any), '{.}')


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
