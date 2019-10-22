#!/usr/bin/python3
"""
Unittesting for Class - Base
models/base.py
"""

import sys
import unittest
from models.base import Base

class BaseTest(unittest.TestCase):
    """Class Base unittests"""


    def test_incrementation(self):
        """sees if object id increments """     
        Base._Base__nb_objects = 0

        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base()
        self.assertEqual(b3.id, 3)

    def test_direct_inputs(self):
        """checks for various valid inputs """
        Base._Base__nb_objects = 0

        b_zero = Base()
        self.assertEqual(b_zero.id, 1)

        b_int = Base(12)
        self.assertEqual(b_int.id, 12)

        b_neg_int = Base(-12)
        self.assertEqual(b_neg_int.id, -12)
