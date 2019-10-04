#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_list_ints(self):
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(nums), 5)

    def test_tuple_ints(self):
        nums = (1, 2, 3, 4, 5)
        self.assertEqual(max_integer(nums), 5)

    def test_repeated_ints(self):
        nums = [1, 2, 3, 3, 3]
        self.assertEqual(max_integer(nums), 3)

    def test_one_element_list(self):
        nums = [6]
        self.assertEqual(max_integer(nums), 6)

    def test_empty_list(self):
        nums = []
        self.assertIsNone(max_integer(nums))

    def test_no_param(self):
        self.assertIsNone(max_integer())

    def test_string(self):
        name = 'hola'
        self.assertEqual(ord(max_integer(name)), 111)

    def test_dictionary(self):
        dic = {'a': 1}
        self.assertRaises(KeyError, max_integer, dic)

    def test_set(self):
        a_set = {3, 4}
        self.assertRaises(TypeError, max_integer, a_set)

    def test_mixed_tuple(self):
        a_tuple = (1, 'niggas', 3)
        self.assertRaises(TypeError, max_integer, a_tuple)

    def test_mixed_list(self):
        mixed_lst = [1, 3.4, 'a', (3+2j), [3, 3], (1, )]
        self.assertRaises(TypeError, max_integer, mixed_lst)
