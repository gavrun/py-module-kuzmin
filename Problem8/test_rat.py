import unittest
import math 

# ratnum.py and ratpoly.py must be available over PYTHONPATH
from ratnum import RatNum
from ratpoly import RatPoly

class TestRatNum(unittest.TestCase):

    def test_init_and_reduction(self):
        self.assertEqual(RatNum(1, 2), RatNum(1, 2), "1/2")
        self.assertEqual(RatNum(2, 4), RatNum(1, 2), "2/4 reduces to 1/2")
        self.assertEqual(RatNum(0, 5), RatNum(0, 1), "0/5 reduces to 0/1")
        self.assertEqual(RatNum(3, 1), RatNum(3), "3/1 is 3")
        self.assertEqual(RatNum(-1, 2), RatNum(-1, 2), "-1/2")
        self.assertEqual(RatNum(1, -2), RatNum(-1, 2), "1/-2 reduces to -1/2")
        self.assertEqual(RatNum(-2, -4), RatNum(1, 2), "-2/-4 reduces to 1/2")
        self.assertEqual(RatNum(0, 1), RatNum(0), "0/1 is 0")

    def test_nan(self):
        nan1 = RatNum(0, 0)
        nan2 = RatNum(10, 0) 
        r_1_2 = RatNum(1, 2)
        self.assertTrue(nan1.is_nan(), "0/0 is NaN")
        self.assertTrue(nan2.is_nan(), "10/0 is NaN")
        self.assertFalse(r_1_2.is_nan(), "1/2 is not NaN")
        self.assertEqual(nan1, RatNum(0,0), "NaN equality")

    def test_is_positive_negative(self):
        r_pos = RatNum(1, 2)
        r_neg = RatNum(-1, 2)
        r_zero = RatNum(0)
        r_nan = RatNum(0, 0)

        self.assertTrue(r_pos.is_positive())
        self.assertFalse(r_pos.is_negative())

        self.assertFalse(r_neg.is_positive())
        self.assertTrue(r_neg.is_negative())

        self.assertFalse(r_zero.is_positive())
        self.assertFalse(r_zero.is_negative())

        self.assertFalse(r_nan.is_positive(), "NaN is not positive")
        self.assertFalse(r_nan.is_negative(), "NaN is not negative")

    def test_float_value(self):
        self.assertEqual(RatNum(1, 2).float_value(), 0.5)
        self.assertEqual(RatNum(3, 1).float_value(), 3.0)
        self.assertEqual(RatNum(-5, 2).float_value(), -2.5)
        self.assertTrue(math.isnan(RatNum(0, 0).float_value()), "NaN float_value is math.nan")

    def test_int_value(self):
        self.assertEqual(RatNum(5, 2).int_value(), 2, "5/2 int_value is 2")
        self.assertEqual(RatNum(1, 3).int_value(), 0, "1/3 int_value is 0")
        self.assertEqual(RatNum(-5, 2).int_value(), -2, "-5/2 int_value is -2")
        self.assertEqual(RatNum(0, 0).int_value(), 0, "NaN int_value is 0")

    def test_negation(self):
        self.assertEqual(-RatNum(1, 2), RatNum(-1, 2))
        self.assertEqual(-RatNum(-1, 2), RatNum(1, 2))
        self.assertEqual(-RatNum(0, 0), RatNum(0, 0), "Negation of NaN is NaN")

    def test_addition(self):
        r1_2 = RatNum(1, 2)
        r1_3 = RatNum(1, 3)
        r_nan = RatNum(0, 0)
        self.assertEqual(r1_2 + r1_3, RatNum(5, 6))
        self.assertEqual(r1_2 + r_nan, r_nan, "Add with NaN")
        self.assertEqual(r_nan + r1_2, r_nan, "NaN add with RatNum")

    def test_subtraction(self):
        r1_2 = RatNum(1, 2)
        r1_3 = RatNum(1, 3)
        r_nan = RatNum(0, 0)
        self.assertEqual(r1_2 - r1_3, RatNum(1, 6))
        self.assertEqual(r1_2 - r_nan, r_nan, "Sub with NaN")

    def test_multiplication(self):
        r1_2 = RatNum(1, 2)
        r2_3 = RatNum(2, 3)
        r_zero = RatNum(0)
        r_nan = RatNum(0, 0)
        self.assertEqual(r1_2 * r2_3, RatNum(1, 3))
        self.assertEqual(r1_2 * r_zero, r_zero)
        self.assertEqual(r1_2 * r_nan, r_nan, "Mul with NaN")

    def test_division(self):
        r1_2 = RatNum(1, 2)
        r2_3 = RatNum(2, 3)
        r_zero = RatNum(0)
        r_nan = RatNum(0, 0)
        self.assertEqual(r1_2 / r2_3, RatNum(3, 4))
        self.assertEqual(r1_2 / r_nan, r_nan, "Div by NaN")
        self.assertEqual(r_nan / r1_2, r_nan, "NaN div by RatNum")
        self.assertEqual(r1_2 / r_zero, r_nan, "Div by zero is NaN")

    def test_compare_to(self):
        r1_2 = RatNum(1, 2)
        r1_3 = RatNum(1, 3)
        r_nan = RatNum(0, 0)
        self.assertEqual(r1_2.compare_to(r1_3), 1)
        self.assertEqual(r1_3.compare_to(r1_2), -1)
        self.assertEqual(r1_2.compare_to(RatNum(2,4)), 0) # 1/2 == 2/4
        self.assertEqual(r_nan.compare_to(r_nan), 0, "NaN compareTo NaN")
        self.assertEqual(r1_2.compare_to(r_nan), -1, "RatNum compareTo NaN")
        self.assertEqual(r_nan.compare_to(r1_2), 1, "NaN compareTo RatNum")

    def test_gcd(self):
        r6_5 = RatNum(6, 5)
        r9_2 = RatNum(9, 2)
        r_nan = RatNum(0,0)
        self.assertEqual(r6_5.gcd(r9_2), math.gcd(6,9))
        self.assertEqual(r6_5.gcd(r_nan), 0, "GCD with NaN")
        self.assertEqual(r_nan.gcd(r9_2), 0, "NaN GCD with RatNum")

    def test_equality_and_hash(self):
        r1 = RatNum(1, 2)
        r2 = RatNum(1, 2)
        r3 = RatNum(2, 4) # Equal to r1, r2
        r4 = RatNum(1, 3)
        nan1 = RatNum(0,0)
        nan2 = RatNum(0,0)

        self.assertEqual(r1, r2)
        self.assertEqual(r1, r3)
        self.assertNotEqual(r1, r4)
        self.assertEqual(nan1, nan2)
        self.assertNotEqual(r1, nan1)

        self.assertEqual(hash(r1), hash(r2))
        self.assertEqual(hash(r1), hash(r3))
        self.assertNotEqual(hash(r1), hash(r4), "Hashes of non-equal numbers should ideally differ")
        self.assertEqual(hash(nan1), hash(nan2))

    def test_string_representation(self):
        self.assertEqual(str(RatNum(1, 2)), "1/2")
        self.assertEqual(str(RatNum(2, 1)), "2")
        self.assertEqual(str(RatNum(0, 1)), "0")
        self.assertEqual(str(RatNum(-3, 4)), "-3/4")
        self.assertEqual(str(RatNum(0, 0)), "NaN")


class TestRatPoly(unittest.TestCase):

    def setUp(self):
        self.R0 = RatNum(0)
        self.R1 = RatNum(1)
        self.R2 = RatNum(2)
        self.R1_2 = RatNum(1, 2)
        self.Rm1 = RatNum(-1)
        self.RNaN = RatNum(0, 0)

        self.ZeroPoly = RatPoly()
        self.NaNPoly = RatPoly({0: self.RNaN}) # Canonical NaN polynomial
        self.ConstPoly = RatPoly({0: self.R2}) # 2
        self.Poly1 = RatPoly({0: self.R1, 1: self.R2}) # 2*x + 1
        self.Poly2 = RatPoly({1: self.R1_2, 2: self.R1}) # x^2 + 1/2*x

    def test_init(self):
        self.assertEqual(RatPoly(), self.ZeroPoly, "Default constructor is zero poly")
        self.assertEqual(RatPoly({0: self.R0}), self.ZeroPoly, "Poly with 0 coeff is zero poly")
        p = RatPoly({0: self.R1, 1: self.R2, 3: self.R0}) # 2*x + 1
        self.assertEqual(p.get_coeff(3), self.R0, "Zero coefficient should be removed")
        self.assertEqual(p.degree(), 1, "Degree after removing zero coeff")
        self.assertEqual(RatPoly({1: self.RNaN, 0: self.R1}), self.NaNPoly, "NaN coeff makes poly NaN")

    def test_is_nan(self):
        self.assertTrue(self.NaNPoly.is_nan())
        self.assertFalse(self.ZeroPoly.is_nan())
        self.assertFalse(self.Poly1.is_nan())

    def test_degree(self):
        self.assertEqual(self.ZeroPoly.degree(), 0, "Degree of zero poly")
        self.assertEqual(self.ConstPoly.degree(), 0, "Degree of const poly")
        self.assertEqual(self.Poly1.degree(), 1, "Degree of 2*x + 1")
        self.assertEqual(self.Poly2.degree(), 2, "Degree of x^2 + 1/2*x")
        self.assertEqual(self.NaNPoly.degree(), 0, "Degree of NaN poly")

    def test_get_coeff(self):
        self.assertEqual(self.Poly1.get_coeff(1), self.R2)
        self.assertEqual(self.Poly1.get_coeff(0), self.R1)
        self.assertEqual(self.Poly1.get_coeff(5), self.R0, "Coeff of non-existent degree is 0")
        self.assertEqual(self.NaNPoly.get_coeff(0), self.RNaN, "NaNPoly coeff 0")
        self.assertEqual(self.NaNPoly.get_coeff(1), self.R0, "NaNPoly coeff non-0")
        self.assertEqual(self.Poly1.get_coeff(-1), self.R0, "Coeff of negative degree")


    def test_scale_coeff(self):
        scaled = self.Poly1.scale_coeff(self.R1_2) # (2*x+1) * 1/2 = x + 1/2
        expected = RatPoly({0: self.R1_2, 1: self.R1})
        self.assertEqual(scaled, expected)
        self.assertEqual(self.Poly1.scale_coeff(self.R0), self.ZeroPoly, "Scale by zero")
        self.assertEqual(self.Poly1.scale_coeff(self.RNaN), self.NaNPoly, "Scale by NaN")
        self.assertEqual(self.NaNPoly.scale_coeff(self.R2), self.NaNPoly, "Scale NaN poly")
        with self.assertRaises(TypeError):
            self.Poly1.scale_coeff(2) # Must be RatNum

    def test_negation(self):
        neg_poly1 = -self.Poly1 # -(2*x+1) = -2*x - 1
        expected = RatPoly({0: self.Rm1, 1: RatNum(-2)})
        self.assertEqual(neg_poly1, expected)
        self.assertEqual(-self.ZeroPoly, self.ZeroPoly)
        self.assertEqual(-self.NaNPoly, self.NaNPoly)

    def test_addition(self):
        # (2*x+1) + (x^2+1/2*x) = x^2 + 2.5*x + 1
        sum_poly = self.Poly1 + self.Poly2
        expected = RatPoly({0: self.R1, 1: RatNum(5,2), 2: self.R1})
        self.assertEqual(sum_poly, expected)
        self.assertEqual(self.Poly1 + self.ZeroPoly, self.Poly1)
        self.assertEqual(self.Poly1 + self.NaNPoly, self.NaNPoly)
        self.assertEqual(self.NaNPoly + self.Poly1, self.NaNPoly)
        with self.assertRaises(TypeError):
            self.Poly1 + 2

    def test_subtraction(self):
        # (2*x+1) - (x^2+1/2*x) = -x^2 + 1.5*x + 1
        diff_poly = self.Poly1 - self.Poly2
        expected = RatPoly({0: self.R1, 1: RatNum(3,2), 2: self.Rm1})
        self.assertEqual(diff_poly, expected)
        self.assertEqual(self.Poly1 - self.ZeroPoly, self.Poly1)
        self.assertEqual(self.Poly1 - self.NaNPoly, self.NaNPoly)
        self.assertEqual(self.NaNPoly - self.Poly1, self.NaNPoly)
        # P - P = 0
        self.assertEqual(self.Poly1 - self.Poly1, self.ZeroPoly)
        with self.assertRaises(TypeError):
            self.Poly1 - 2

    def test_multiplication(self):
        # (2*x+1) * 2 (RatNum) = 4*x + 2
        mul_by_ratnum = self.Poly1 * self.R2
        expected_ratnum_mul = RatPoly({0: self.R2, 1: RatNum(4)})
        self.assertEqual(mul_by_ratnum, expected_ratnum_mul)

        # (x+1) * (x-1) = x^2 - 1
        p_x_plus_1 = RatPoly({0: self.R1, 1: self.R1})
        p_x_minus_1 = RatPoly({0: self.Rm1, 1: self.R1})
        prod = p_x_plus_1 * p_x_minus_1
        expected_prod = RatPoly({0: self.Rm1, 2: self.R1})
        self.assertEqual(prod, expected_prod)

        self.assertEqual(self.Poly1 * self.ZeroPoly, self.ZeroPoly)
        self.assertEqual(self.Poly1 * self.NaNPoly, self.NaNPoly)
        self.assertEqual(self.NaNPoly * self.Poly1, self.NaNPoly)
        self.assertEqual(self.Poly1 * self.RNaN, self.NaNPoly, "Poly * RatNum NaN")
        with self.assertRaises(TypeError):
            self.Poly1 * "string"

    def test_eval(self):
        # Poly1 = 2*x + 1
        self.assertEqual(self.Poly1.eval(self.R0), self.R1, "P(0)") # 2*0+1 = 1
        self.assertEqual(self.Poly1.eval(self.R1), RatNum(3), "P(1)") # 2*1+1 = 3
        self.assertEqual(self.Poly1.eval(self.R1_2), self.R2, "P(1/2)") # 2*(1/2)+1 = 2
        self.assertEqual(self.Poly1.eval(self.RNaN), self.RNaN, "P(NaN)")
        self.assertEqual(self.NaNPoly.eval(self.R1), self.RNaN, "NaNPoly eval")
        self.assertEqual(self.ZeroPoly.eval(self.R1_2), self.R0, "ZeroPoly eval")
        with self.assertRaises(TypeError):
            self.Poly1.eval(1) # Must be RatNum

    def test_differentiate(self):
        # d/dx (2*x+1) = 2
        self.assertEqual(self.Poly1.differentiate(), self.ConstPoly)
        # d/dx (x^2 + 1/2*x) = 2*x + 1/2
        deriv_poly2 = self.Poly2.differentiate()
        expected_deriv_poly2 = RatPoly({0: self.R1_2, 1: self.R2})
        self.assertEqual(deriv_poly2, expected_deriv_poly2)
        self.assertEqual(self.ConstPoly.differentiate(), self.ZeroPoly, "d/dx (const) = 0")
        self.assertEqual(self.ZeroPoly.differentiate(), self.ZeroPoly, "d/dx (0) = 0")
        self.assertEqual(self.NaNPoly.differentiate(), self.NaNPoly, "d/dx (NaN) = NaN")

    def test_anti_differentiate(self):
        # ∫ (2) dx = 2*x + C
        ad_const = self.ConstPoly.anti_differentiate(self.R1) # C=1
        expected_ad_const = RatPoly({0: self.R1, 1: self.R2}) # 2*x + 1
        self.assertEqual(ad_const, expected_ad_const)

        # ∫ (2*x+1) dx = x^2 + x + C
        ad_poly1 = self.Poly1.anti_differentiate(self.R1_2) # C=1/2
        expected_ad_poly1 = RatPoly({0: self.R1_2, 1: self.R1, 2: self.R1}) # x^2+x+1/2
        self.assertEqual(ad_poly1, expected_ad_poly1)

        self.assertEqual(self.ZeroPoly.anti_differentiate(self.R2), self.ConstPoly, "∫ 0 dx = C")
        self.assertEqual(self.NaNPoly.anti_differentiate(self.R1), self.NaNPoly, "∫ NaN dx")
        self.assertEqual(self.Poly1.anti_differentiate(self.RNaN), self.NaNPoly, "∫ P dx with C=NaN")
        with self.assertRaises(TypeError):
            self.Poly1.anti_differentiate(1) # C must be RatNum

    def test_integrate(self):
        # ∫_0^1 (2*x+1) dx = [x^2+x]_0^1 = (1+1) - (0) = 2
        self.assertEqual(self.Poly1.integrate(self.R0, self.R1), self.R2)
        # ∫_1^1 (2*x+1) dx = 0
        self.assertEqual(self.Poly1.integrate(self.R1, self.R1), self.R0)
        # ∫_0^1 (2) dx = [2x]_0^1 = 2
        self.assertEqual(self.ConstPoly.integrate(self.R0, self.R1), self.R2)

        self.assertEqual(self.ZeroPoly.integrate(self.R0, self.R1), self.R0)
        self.assertEqual(self.NaNPoly.integrate(self.R0, self.R1), self.RNaN)
        self.assertEqual(self.Poly1.integrate(self.RNaN, self.R1), self.RNaN)
        self.assertEqual(self.Poly1.integrate(self.R0, self.RNaN), self.RNaN)
        with self.assertRaises(TypeError):
            self.Poly1.integrate(0,1) # Limits must be RatNum

    def test_equality_and_hash(self):
        p1_copy = RatPoly({0: self.R1, 1: self.R2}) # Same as self.Poly1
        p_diff = RatPoly({0: self.R2, 1: self.R1})

        self.assertEqual(self.Poly1, p1_copy)
        self.assertNotEqual(self.Poly1, p_diff)
        self.assertEqual(self.NaNPoly, RatPoly({0: self.RNaN}))
        self.assertNotEqual(self.Poly1, self.NaNPoly)
        self.assertNotEqual(self.Poly1, "string") # Test against different type

        self.assertEqual(hash(self.Poly1), hash(p1_copy))
        # Hashes of non-equal objects are not guaranteed to be different,
        # but for these simple cases they likely will be.
        # self.assertNotEqual(hash(self.Poly1), hash(p_diff))
        self.assertEqual(hash(self.NaNPoly), hash(RatPoly({0: self.RNaN})))

    def test_string_representation(self):
        # Based on your __str__ which sorts by degree descending and uses " + "
        self.assertEqual(str(self.ZeroPoly), "0")
        self.assertEqual(str(self.NaNPoly), "NaN")
        self.assertEqual(str(self.ConstPoly), "2") # 2
        # Poly1 = 2*x + 1
        # Sorted keys: 1, 0. Terms: "2*x", "1"
        self.assertEqual(str(self.Poly1), "2*x + 1")
        # Poly2 = x^2 + 1/2*x
        # Sorted keys: 2, 1. Terms: "1*x^2", "1/2*x"
        self.assertEqual(str(self.Poly2), "1*x^2 + 1/2*x")
        # Poly with negative coefficient: x - 1
        p_x_minus_1 = RatPoly({0: self.Rm1, 1: self.R1})
        self.assertEqual(str(p_x_minus_1), "1*x + -1") # Current __str__ behavior

if __name__ == '__main__':
    unittest.main()

