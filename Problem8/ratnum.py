import math 

class RatNum:
    """
    Immutable rational number class. Supports NaN representation.

    Representation fields:
        - _numerator: int
        - _denominator: int (positive, except 0 for NaN)

    Representation invariant:
        - _denominator > 0 or (_denominator == 0 and _numerator == 0 for NaN)
        - numerator and denominator are in reduced form (gcd = 1)

    Abstraction function:
        - Represents the rational number _numerator / _denominator,
          unless _denominator == 0, which represents NaN.
    """

    def __init__(self, numerator: int, denominator: int = 1):
        """
        @requires: denominator can be zero to represent NaN
        @modifies: nothing
        @effects: constructs a reduced rational number or a NaN if denominator == 0
        @throws: none
        @returns: new RatNum instance
        """
        if denominator == 0:
            self._numerator = 0
            self._denominator = 0
        else:
            if denominator < 0:
                numerator, denominator = -numerator, -denominator
            g = math.gcd(numerator, denominator)
            self._numerator = numerator // g
            self._denominator = denominator // g

    def is_nan(self) -> bool:
        """
        @requires: none
        @modifies: nothing
        @effects: checks whether the number is NaN
        @throws: none
        @returns: True if the number is NaN, False otherwise
        """
        return self._denominator == 0

    def is_positive(self) -> bool:
        """
        @requires: number must not be NaN
        @modifies: nothing
        @effects: checks whether the number is positive
        @throws: none
        @returns: True if positive
        """
        return not self.is_nan() and self._numerator > 0

    def is_negative(self) -> bool:
        """
        @requires: number must not be NaN
        @modifies: nothing
        @effects: checks whether the number is negative
        @throws: none
        @returns: True if negative
        """
        return not self.is_nan() and self._numerator < 0

    def float_value(self) -> float:
        """
        @requires: none
        @modifies: nothing
        @effects: converts the rational number to a float
        @throws: none
        @returns: float approximation of the rational number
        """
        if self.is_nan():
            return float('nan')
        return self._numerator / self._denominator

    def int_value(self) -> int:
        """
        @requires: none
        @modifies: nothing
        @effects: converts the rational number to an integer (truncation)
        @throws: none
        @returns: integer approximation
        """
        if self.is_nan():
            return 0
        return int(self.float_value())

    def __neg__(self):
        """
        @requires: none
        @modifies: nothing
        @effects: returns the additive inverse
        @throws: none
        @returns: new RatNum with negated value
        """
        if self.is_nan():
            return RatNum(0, 0)
        return RatNum(-self._numerator, self._denominator)

    def __add__(self, other):
        """
        @requires: other must be RatNum
        @modifies: nothing
        @effects: adds two RatNum values
        @throws: none
        @returns: sum of two RatNum values or NaN if either is NaN
        """
        if self.is_nan() or other.is_nan():
            return RatNum(0, 0)
        num = self._numerator * other._denominator + other._numerator * self._denominator
        den = self._denominator * other._denominator
        return RatNum(num, den)

    def __sub__(self, other):
        """
        @requires: other must be RatNum
        @modifies: nothing
        @effects: subtracts other from self
        @throws: none
        @returns: result of subtraction
        """
        return self + (-other)

    def __mul__(self, other):
        """
        @requires: other must be RatNum
        @modifies: nothing
        @effects: multiplies two RatNum values
        @throws: none
        @returns: product of two RatNum values or NaN if either is NaN
        """
        if self.is_nan() or other.is_nan():
            return RatNum(0, 0)
        return RatNum(self._numerator * other._numerator, self._denominator * other._denominator)

    def __truediv__(self, other):
        """
        @requires: other must be RatNum
        @modifies: nothing
        @effects: divides self by other
        @throws: none
        @returns: result of division or NaN if invalid
        """
        if self.is_nan() or other.is_nan() or other._numerator == 0:
            return RatNum(0, 0)
        return RatNum(self._numerator * other._denominator, self._denominator * other._numerator)

    def compare_to(self, other) -> int:
        """
        @requires: other must be RatNum
        @modifies: nothing
        @effects: compares self with other
        @throws: none
        @returns: 1 if self > other, -1 if self < other, 0 if equal
        """
        if self.is_nan() and other.is_nan():
            return 0
        if self.is_nan():
            return 1
        if other.is_nan():
            return -1
        diff = (self - other).float_value()
        return (diff > 0) - (diff < 0)

    def gcd(self, other):
        """
        @requires: other must be RatNum
        @modifies: nothing
        @effects: computes the greatest common divisor of self and other numerators
        @throws: none
        @returns: int GCD of numerators (denominator not considered)
        """
        if self.is_nan() or other.is_nan():
            return 0
        return math.gcd(self._numerator, other._numerator)

    def __eq__(self, other):
        """
        @requires: other must be RatNum
        @modifies: nothing
        @effects: checks equality
        @throws: none
        @returns: True if equal
        """
        return isinstance(other, RatNum) and \
               self._numerator == other._numerator and \
               self._denominator == other._denominator

    def __hash__(self):
        """
        @requires: none
        @modifies: nothing
        @effects: returns a hash value
        @throws: none
        @returns: hash of the RatNum
        """
        return hash((self._numerator, self._denominator))

    def __str__(self):
        """
        @requires: none
        @modifies: nothing
        @effects: returns string representation
        @throws: none
        @returns: human-readable string
        """
        if self.is_nan():
            return "NaN"
        if self._denominator == 1:
            return f"{self._numerator}"
        return f"{self._numerator}/{self._denominator}"
