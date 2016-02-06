#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_equality
----------------------------------

Tests for the `AnyType` __repr__ method
"""

import unittest

from finitio.types import AnyType


class TestAnyTypeStr(unittest.TestCase):

    _type = AnyType()

    def test_it_gives_the_correct_repr(self):
        self.assertEquals(str(self._type), '.')


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
