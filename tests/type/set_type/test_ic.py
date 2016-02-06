#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_equality
----------------------------------

Tests for the `SetType` information contract
"""

import unittest

from tests.helpers import IntType
from finitio.types import SetType


class TestSetTypeIC(unittest.TestCase):

    info = {
      'element_type': IntType,
      'metadata': {'foo': 'bar'}
    }
    subject = SetType.info(info)

    def test_it_dressed_as_expected(self):
        self.assertIsInstance(self.subject, SetType)
        self.assertIs(self.subject.element_type, IntType)
        self.assertEquals(self.subject.metadata, {'foo': 'bar'})

    def test_it_undresses_as_expected(self):
        self.assertEquals(self.subject.to_info(), self.info)


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
