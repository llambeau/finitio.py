#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_type
----------------------------------

Tests for the `Type` class.
"""

import unittest

from finitio.types import Type, BuiltinType


class TestType(unittest.TestCase):

    info = {
        'builtin': BuiltinType.info({
            'py_type': str,
            'metadata': {
                'foo': 'bar'
            }
        })
    }

    def setUp(self):
        self.subject = Type.factor(self.info)

    def test_it_should_dress_as_expected(self):
        self.assertIsInstance(self.subject, Type)
        self.assertEquals(self.subject.py_type, str)
        self.assertEquals(self.subject.metadata, {'foo': 'bar'})

    def test_it_should_undress_as_expected(self):
        self.assertEquals(self.subject.to_factor(), self.info)

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
