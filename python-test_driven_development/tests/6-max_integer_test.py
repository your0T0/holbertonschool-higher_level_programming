#!/usr/bin/python3
"""
Unittest for max_integer
"""

import unittest
max_integer = _import_('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_single_element(self):
        self.assertEqual(max_integer([99]), 99)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_multiple_max(self):
        self.assertEqual(max_integer([1, 3, 3, 2]), 3)

    def test_unordered(self):
        self.assertEqual(max_integer([4, 1, 7, 6]), 7)

    def test_floats(self):
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)
