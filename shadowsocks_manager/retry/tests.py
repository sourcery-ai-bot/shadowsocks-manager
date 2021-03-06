# -*- coding: utf-8 -*-

# py2.7 and py3 compatibility imports
from __future__ import unicode_literals
from __future__ import absolute_import

from unittest import TestCase

from . import retry

# Create your tests here.
class RetryTestCase(TestCase):
    def test(self):
        self.assertTrue(self.call_retryee(n=1, count=0))
        self.assertTrue(self.call_retryee(n=4, count=3))
        self.assertFalse(self.call_retryee(n=2, count=0))
        self.assertFalse(self.call_retryee(n=5, count=3))

    def call_retryee(self, n, count):
        """
        Set the decorator @retry(count=count) on retryee(). Call the retryee(n=n).
        """
        # reset the global counter before calling retryee()
        self.RETRYING = 0

        @retry(count=count, delay=0.1)
        def retryee(n):
            """
            Return True on the Nth time call of this function, return False on otherwise.
            """
            self.RETRYING += 1
            return self.RETRYING == n

        return retryee(n)
