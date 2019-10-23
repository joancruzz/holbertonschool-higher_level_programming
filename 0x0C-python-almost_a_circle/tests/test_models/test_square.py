#!/usr/bin/python3
"""Unittest for Square"""
import unittest
import sys
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO


class TestSquare(unittest.TestCase):
    """Square class test"""

    def setUp(self):
        """Resets nb_objects"""
        Base._Base__nb_objects = 0

    def test_id(self):
        """Prints id"""
        r1 = Square(4)
        self.assertEqual(r1.id, 1)

        r2 = Square(2)
        self.assertEqual(r2.id, 2)

        r3 = Square(9, 0, 0, 13)
        self.assertEqual(r3.id, 13)
        self.assertTrue(type(r3), Square)

    def test_all_param(self):
        """Passing all parameters"""
        r1 = Square(1, 2, 3, 4)

    def test_all_negative(self):
        """Passing all negative"""
        with self.assertRaises(ValueError):
            r1 = Square(-1)
        with self.assertRaises(ValueError):
            r1 = Square(1, -1, 2, 3)
        with self.assertRaises(ValueError):
            r1 = Square(1, 2, -3)

    def test_all_zero(self):
        """zero"""
        with self.assertRaises(ValueError):
            r1 = Square(0)

    def test_string(self):
        """string"""
        with self.assertRaises(TypeError):
            r1 = Square("string")
        with self.assertRaises(TypeError):
            r1 = Square(1, "2")
        with self.assertRaises(TypeError):
            r1 = Square(1, 2, "3")

    def test_no_param(self):
        """empty"""
        with self.assertRaises(TypeError):
            r1 = Square()
      
    def test_excess_param(self):
        """Extra parameters"""
        with self.assertRaises(TypeError):
            r1 = Square(1, 2, 3, 4, 1, 3)

    def test_float(self):
        """Float"""
        with self.assertRaises(TypeError):
            r1 = Square(1.2)
                                                          
    def test_NaN(self):
        """NaN"""
        with self.assertRaises(TypeError):
            r1 = Square(float("nan"))

    def test_inf(self):
        """inf parameter"""
        with self.assertRaises(TypeError):
            r1 = Square(float("inf"))
                      
    def test_unknown(self):
        """unknown"""
        with self.assertRaises(NameError):
            r1 = Square(a)

    def test_None(self):
        """None"""
        with self.assertRaises(TypeError):
            r1 = Square(None)

    def test_area(self):
        """Print area"""
        r1 = Square(10)
        self.assertTrue(type(r1), Square)

    def test_display(self):
        """rectangle output"""
        output = StringIO()
        sys.stdout = output
        r1 = Square(2)
        r1.display()
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "##\n##\n"

    def test_str(self):
        """__str__"""
        output = StringIO()
        sys.stdout = output
        r1 = Square(4, 1, 2, 13)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Square] (13) 1/2 - 4\n"

    def test_display_x_y(self):
        """rectangle with x and y"""
        output = StringIO()
        sys.stdout = output
        r2 = Square(2, 1, 0)
        r2.display()
        sys.stdout = sys.__stdout__
        assert output.getvalue() == " ##\n ##\n"

    def test_update(self):
        """update"""
        output = StringIO()
        sys.stdout = output
        r1 = Square(10, 10, 10)
        r1.update(89)
        r1.update(89, 2)
        r1.update(89, 2, 3)
        r1.update(89, 2, 3, 4)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Square] (89) 3/4 - 2\n"

    def test_update_extra(self):
        """Update with extra parameters"""
        output = StringIO()
        sys.stdout = output
        r1 = Square(10, 10, 10)
        r1.update(89, 3, 4, 5, 6)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Square] (89) 4/5 - 3\n"

    def test_update_no_param(self):
        """Update with no parameters"""
        output = StringIO()
        sys.stdout = output
        r1 = Square(10, 10, 10)
        r1.update()
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Square] (1) 10/10 - 10\n"

    def test_kwargs(self):
        """kwargs"""
        output = StringIO()
        sys.stdout = output
        r1 = Square(2, 2, 2)
        r1.update(x=1, size=2, y=3)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Square] (1) 1/3 - 2\n"

    def test_kwargs_extra_keys(self):
        """kwargs normal behavior"""
        output = StringIO()
        sys.stdout = output
        r1 = Square(2, 2, 2, 2)
        r1.update(id=1, x=1, size=2, y=3, banu=89)
        print(r1)
        sys.stdout = sys.__stdout__
        assert output.getvalue() == "[Square] (1) 1/3 - 2\n"

    def test_to_dictionary(self):
        """to dictionary"""
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        self.assertEqual(s1_dictionary, {'id': 1, 'x': 2, 'size': 10, 'y': 1})
        self.assertTrue(type(s1_dictionary), dict)

    def test_save_to_file_None2(self):
        """JSON string None"""
        Square.save_to_file(None)
        with open("Square.json") as file:
            self.assertEqual(file.read(), "[]")


if __name__ == '__main__':
    unittest.main()
