import unittest
from math_expression3 import continued_fraction

class TestContinuedFraction(unittest.TestCase):

    def test_base_case(self):
        """Test the base case where depth is 0."""
        self.assertEqual(continued_fraction(2, 0), 2)

    def test_single_depth(self):
        """Test the case where depth is 1."""
        self.assertAlmostEqual(continued_fraction(2, 1), 2 + 1 / 2, places=7)

    def test_multiple_depth(self):
        """Test the case where depth is greater than 1."""
        self.assertAlmostEqual(continued_fraction(2, 2), 2 + 1 / (2 + 1 / 2), places=7)
        self.assertAlmostEqual(continued_fraction(2, 3), 2 + 1 / (2 + 1 / (2 + 1 / 2)), places=7)

    def test_large_depth(self):
        """Test the function with a larger depth."""
        result = continued_fraction(2, 10)
        self.assertIsInstance(result, float)

if __name__ == "__main__":
    unittest.main()
