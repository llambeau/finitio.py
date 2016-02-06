#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_dress_monad
----------------------------------

Tests for the `DressMonad` class.
"""

import unittest
from mock import MagicMock

from finitio.support import Monad


class TestMonad(unittest.TestCase):

    def setUp(self):
        self.world = {'foo': 'bar'}
        self.monad = Monad(self.world)

    def success(self, result):
        return self.monad.success(result)

    def failure(self, error):
        return self.monad.failure({}, error)

    def test_is_initially_successful_on_successful(self):
        self.assertEquals(self.success(12).is_success(), True)

    def test_is_not_initially_successful_on_failure(self):
        self.assertEquals(self.failure('error').is_success(), False)

    ''' describe success '''

    def test_success_preserves_the_world(self):
        self.assertEquals(self.success(12).world, self.world)

    ''' describe failure '''

    def test_failure_preserves_the_world(self):
        self.assertEquals(self.failure("error").world, self.world)

    ''' describe on_success '''

    def test_on_success_yields_the_block_and_returns_its_result(self):
        self.assertEquals(self.success(12).on_success(lambda x: 13), 13)

    def test_on_success_doesnt_yields_the_block_on_failure(self):
        callback = MagicMock()
        self.success(12).on_failure(callback)
        callback.assert_not_called()

    def test_on_success_should_return_itself_on_failure(self):
        f = self.failure("error")
        self.assertEquals(f.on_success(lambda x: x), f)

    ''' describe on_failure '''

    def test_on_failure_yields_the_block_and_returns_its_result(self):
        self.assertEquals(self.failure("error").on_failure(lambda x: 13), 13)

    def test_on_failure_doesnt_yields_the_block_on_success(self):
        callback = MagicMock()
        self.failure("error").on_success(callback)
        callback.assert_not_called()

    def test_on_failure_should_return_itself_on_success(self):
        f = self.success(12)
        self.assertEquals(f.on_failure(lambda x: x), f)

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
