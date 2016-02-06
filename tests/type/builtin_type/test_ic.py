#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_equality
----------------------------------

Tests for the `BuiltinType` information contract
"""

import unittest

from numbers import Number
from finitio.types import BuiltinType


class TestBuiltinTypeIC(unittest.TestCase):

    info = {
      'py_type': Number,
      'metadata': {'foo': 'bar'}
    }
    subject = BuiltinType.info(info)

    def test_it_dressed_as_expected(self):
        self.assertIsInstance(self.subject, BuiltinType)
        self.assertIs(self.subject.py_type, Number)
        self.assertEquals(self.subject.metadata, {'foo': 'bar'})

    def test_it_undresses_as_expected(self):
        self.assertEquals(self.subject.to_info(), self.info)


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
