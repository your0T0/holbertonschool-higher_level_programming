#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = _import_('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        self.assertEqual(max_integer([1, 4, 2, 3]), 4)

    def test_one_negative(self):
        self.assertEqual(max_integer([-1, 0, 1]), 1)

    def test_only_negatives(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_list_of_one(self):
        self.assertEqual(max_integer([99]), 99)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_strings(self):
        self.assertEqual(max_integer("Python"), "y")

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["a", "abc", "ab"]), "abc")
