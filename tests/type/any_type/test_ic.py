#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_equality
----------------------------------

Tests for the `AnyType` information contract
"""

import unittest

from finitio.types import AnyType


class TestAnyTypeIC(unittest.TestCase):

    info = {
      'metadata': {'foo': 'bar'}
    }
    subject = AnyType.info(info)

    def test_it_dressed_as_expected(self):
        self.assertIsInstance(self.subject, AnyType)
        self.assertEquals(self.subject.metadata, {'foo': 'bar'})

    def test_it_undresses_as_expected(self):
        self.assertEquals(self.subject.to_info(), self.info)


if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
