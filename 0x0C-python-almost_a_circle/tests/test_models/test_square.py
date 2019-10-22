#!/usr/bin/python3
"""
Unittest for Square Size
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquareSize(unittest.TestCase):
        """Test Square Size Method"""
        def test_size(self):
            self.assertEqual(size(0), 0)
            self.assertEqual(size(1), 1)
            self.assertEqual(size(1.5), 1.5)
            self.assertEqual(size(1), 1)

        def test_value(self):
            self.assertRaises(ValueError, size, -1)

        def test_type(self):
            self.assertRaiseseRegex(TypeError, size, True)
            self.assertRaises(TypeError, size, False)
            self.assertRaises(TypeError, size, str)
            self.assertRaises(TypeError, size, [])
            self.assertRaises(TypeError, size, {})

