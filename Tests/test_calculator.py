# TDD

import unittest
from Tests.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_adding(self):
        calc = Calculator()
        self.assertEqual(calc.adding(2, 3), 5)
        self.assertEqual(calc.adding(-1, 1), 0)

    def test_dividing(self):
        calc = Calculator()
        self.assertEqual(calc.dividing(10, 2), 5)
        self.assertEqual(calc.dividing(-6, 3), -2)

    def test_dividing_by_zero(self):
        calc = Calculator()
        with self.assertRaises(ZeroDivisionError):
            calc.dividing(10, 0)
