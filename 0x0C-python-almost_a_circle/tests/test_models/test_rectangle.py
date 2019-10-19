#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    def test_rectangle_noargs(self):
        self.assertRaises(TypeError, Rectangle)

    def test_rectangle_one_arg(self):
        self.assertRaises(TypeError, Rectangle, 1)

    def test_rectangle_instance(self):
        obj = Rectangle(1, 1)
        self.assertIsInstance(obj, Rectangle)

    def test_inherits_base(self):
        obj = Rectangle(1, 1)
        self.assertIsInstance(obj, Base)

    def test_required_attrs_exists(self):
        obj = Rectangle(3, 4)
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, '_Rectangle__width'))
        self.assertTrue(hasattr(obj, '_Rectangle__height'))
        self.assertTrue(hasattr(obj, '_Rectangle__x'))
        self.assertTrue(hasattr(obj, '_Rectangle__y'))

    def test_getters_setters(self):
        obj = Rectangle(1, 2)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        obj.width = 10
        obj.height = 20
        obj.x = 5
        obj.y = 6
        self.assertEqual(obj.width, 10)
        self.assertEqual(obj.height, 20)
        self.assertEqual(obj.x, 5)
        self.assertEqual(obj.y, 6)

    def test_rectangle_defaults(self):
        obj = Rectangle(1, 1)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 1)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

    def test_rectangle_type_validation(self):
        with self.assertRaises(TypeError) as context:
            obj = Rectangle('a', 2)
        self.assertIn('width must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj = Rectangle(2, {})
        self.assertIn('height must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj = Rectangle(1, 1, {'a': 1})
        self.assertIn('x must be an integer', str(context.exception))

        with self.assertRaises(TypeError) as context:
            obj = Rectangle(1, 1, 4, [31])
        self.assertIn('y must be an integer', str(context.exception))

    def test_rectangle_value_validation(self):
        with self.assertRaises(ValueError) as context:
            obj = Rectangle(0, 1)
        self.assertIn('width must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj = Rectangle(-20, 1)
        self.assertIn('width must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj = Rectangle(1, 0)
        self.assertIn('height must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj = Rectangle(1, -69)
        self.assertIn('height must be > 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj = Rectangle(1, 1, -30)
        self.assertIn('x must be >= 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            obj = Rectangle(1, 1, 1, -80)
        self.assertIn('y must be >= 0', str(context.exception))
