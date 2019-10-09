#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])
    """

    def test_max_end(self):
        self.assertEqual(max_integer([1, 5, 8, 9]), 9)

    def test_max_beginning(self):
        self.assertEqual(max_integer([9, 5, 8, 1]), 9)

    def test_max_middle(self):
        self.assertEqual(max_integer([8, 5, 9, 1, 0]), 9)

    def test_max_OneNumber(self):
        self.assertEqual(max_integer([9, 5, 8, -1]), 9)

    def test_max_onlyNegative(self):
        self.assertEqual(max_integer([-9, -5, -8, -1]), -1)

    def test_max_oneElement(self):
        self.assertEqual(max_integer([9]), 9)

    def test_max_listEmpty(self):
        self.assertEqual(max_integer(), None)
