from ratnum import RatNum

class RatPoly:
    """
    Immutable polynomial with rational coefficients (RatNum).

    Representation fields:
        - _coeffs: dict[int, RatNum], where each key is a non-negative integer degree

    Representation invariant:
        - All keys in _coeffs are non-negative integers
        - Coefficients are non-zero and not NaN (NaN polynomial has single NaN coefficient)

    Abstraction function:
        - Represents sum of terms: _coeffs[d] * x^d
    """

    def __init__(self, coeffs=None):
        """
        @requires: coeffs must be a dict[int, RatNum] or None
        @modifies: nothing
        @effects: constructs a polynomial by cleaning zero and NaN terms
        @throws: none
        @returns: new RatPoly instance
        """
        self._coeffs = {}
        nan_detected = False
        if coeffs:
            for deg, coeff in coeffs.items():
                if coeff.is_nan():
                    nan_detected = True
                elif coeff != RatNum(0):
                    self._coeffs[deg] = coeff
        if nan_detected:
            self._coeffs = {0: RatNum(0, 0)}  # NaN polynomial
        #
        # if coeffs is None:
        #     return
        # for deg, coeff in coeffs.items():
        #     if not isinstance(deg, int) or deg < 0:
        #         continue
        #     if not isinstance(coeff, RatNum):
        #         nan_detected = True
        #         break
        #     if coeff.is_nan():
        #         nan_detected = True
        #         break
        #     if coeff != RatNum(0):
        #         temp_coeffs[deg] = coeff
        # if nan_detected:
        #     self._coeffs = {0: RatNum(0, 0)}
        # else:
        #     self._coeffs = temp_coeffs

    def is_nan(self):
        """
        @requires: none
        @modifies: nothing
        @effects: checks if the polynomial is NaN
        @throws: none
        @returns: True if polynomial is NaN
        """
        return any(coeff.is_nan() for coeff in self._coeffs.values())

    def degree(self):
        """
        @requires: none
        @modifies: nothing
        @effects: returns the highest degree of the polynomial
        @throws: none
        @returns: int, degree of the polynomial
        """
        if self.is_nan():
            return 0
        if not self._coeffs:
            return 0
        return max(self._coeffs)
        # return max(self._coeffs.keys())

    def get_coeff(self, deg):
        """
        @requires: deg is a non-negative integer
        @modifies: nothing
        @effects: returns the coefficient at given degree
        @throws: none
        @returns: RatNum coefficient for x^deg
        """
        if not isinstance(deg, int) or deg < 0:
            return RatNum(0)
        if self.is_nan():
            return RatNum(0,0) if deg == 0 else RatNum(0)
        return self._coeffs.get(deg, RatNum(0))

    def scale_coeff(self, scalar: RatNum):
        """
        @requires: scalar must be a RatNum
        @modifies: nothing
        @effects: scales all coefficients of the polynomial by the given scalar
        @throws: TypeError if scalar is not a RatNum
        @returns: new RatPoly with scaled coefficients
        """
        if not isinstance(scalar, RatNum):
            raise TypeError("Scalar must be a RatNum.")
        if self.is_nan() or scalar.is_nan():
            return RatPoly({0: RatNum(0, 0)})
        return RatPoly({d: c * scalar for d, c in self._coeffs.items()})

    def __neg__(self):
        """
        @requires: none
        @modifies: nothing
        @effects: returns the additive inverse of the polynomial
        @throws: none
        @returns: RatPoly with all coefficients negated
        """
        if self.is_nan():
            return RatPoly({0: RatNum(0, 0)})
        return RatPoly({d: -c for d, c in self._coeffs.items()})

    def __add__(self, other):
        """
        @requires: other must be a RatPoly
        @modifies: nothing
        @effects: adds two polynomials
        @throws: TypeError if other is not a RatPoly
        @returns: new RatPoly representing the sum or NaN if any is NaN
        """
        if not isinstance(other, RatPoly):
            raise TypeError("Can only add RatPoly to RatPoly.")
        if self.is_nan() or other.is_nan():
            return RatPoly({0: RatNum(0, 0)})
        result = self._coeffs.copy()
        for d, c in other._coeffs.items():
            result[d] = result.get(d, RatNum(0)) + c
        return RatPoly(result)

    def __sub__(self, other):
        """
        @requires: other must be a RatPoly
        @modifies: nothing
        @effects: subtracts other from self
        @throws: TypeError if other is not a RatPoly
        @returns: new RatPoly representing the difference
        """
        if not isinstance(other, RatPoly):
            raise TypeError("Can only subtract RatPoly from RatPoly.")
        return self + (-other)

    def __mul__(self, other):
        """
        @requires: other must be a RatPoly
        @modifies: nothing
        @effects: multiplies two polynomials
        @throws: TypeError if other is not a RatPoly or RatNum
        @returns: new RatPoly representing the product or NaN if any is NaN
        """
        if isinstance(other, RatNum):
            return self.scale_coeff(other)
        if not isinstance(other, RatPoly):
            raise TypeError("Can only multiply RatPoly by RatPoly or RatNum.")
        if self.is_nan() or other.is_nan():
            return RatPoly({0: RatNum(0, 0)})
        result = {}
        for d1, c1 in self._coeffs.items():
            for d2, c2 in other._coeffs.items():
                deg = d1 + d2
                result[deg] = result.get(deg, RatNum(0)) + (c1 * c2)
        return RatPoly(result)

    def __truediv__(self, other):
        """
        @requires: other must be a RatPoly
        @modifies: nothing
        @effects: Performs polynomial division of self by other
        @throws: 
        @returns: 
        """
        pass

    def eval(self, x: RatNum):
        """
        @requires: x must be a RatNum
        @modifies: nothing
        @effects: evaluates the polynomial at given x value
        @throws: TypeError if x is not a RatNum
        @returns: RatNum value of the polynomial at x
        """
        if not isinstance(x, RatNum):
            raise TypeError("Evaluation point x must be a RatNum.")
        if self.is_nan() or x.is_nan():
            return RatNum(0, 0)
        result = RatNum(0)
        for d, c in self._coeffs.items():
            term = c * RatNum(x._numerator ** d, x._denominator ** d)
            result += term
        return result

    def differentiate(self):
        """
        @requires: none
        @modifies: nothing
        @effects: Computes the derivative of this polynomial
        @throws: none
        @returns: RatPoly representing the derivative
        """
        if self.is_nan():
            return RatPoly({0: RatNum(0, 0)})
        if not self._coeffs:
            return RatPoly()
        deriv_coeffs = {}
        for deg, coeff in self._coeffs.items():
            if deg == 0:
                continue
            new_coeff = coeff * RatNum(deg) # d/dx (c*x^d) = (c*d)*x^(d-1)
            new_deg = deg - 1
            if new_coeff != RatNum(0):
                deriv_coeffs[new_deg] = new_coeff
        return RatPoly(deriv_coeffs)

    def anti_differentiate(self, C: RatNum):
        """
        @requires: C must be a RatNum representing the constant of integration
        @modifies: nothing
        @effects: Computes an antiderivative (indefinite integral) of this polynomial
        @throws: TypeError if C is not a RatNum
        @returns: A new RatPoly representing the antiderivative
        """
        if not isinstance(C, RatNum):
            raise TypeError("Constant of integration C must be a RatNum.")
        if self.is_nan() or C.is_nan():
            return RatPoly({0: RatNum(0, 0)})
        anti_deriv_coeffs = {}
        if C != RatNum(0):
            anti_deriv_coeffs[0] = C
        for deg, coeff in self._coeffs.items():
            new_deg = deg + 1 # Integral (c*x^d) dx = c/(d+1) * x^(d+1)
            new_coeff = coeff / RatNum(new_deg)
            if new_coeff.is_nan():
                return RatPoly({0: RatNum(0,0)})
            current_val_at_new_deg = anti_deriv_coeffs.get(new_deg, RatNum(0))
            combined_coeff = current_val_at_new_deg + new_coeff
            if combined_coeff != RatNum(0):
                anti_deriv_coeffs[new_deg] = combined_coeff
            elif new_deg in anti_deriv_coeffs: 
                del anti_deriv_coeffs[new_deg]
        return RatPoly(anti_deriv_coeffs)

    def integrate(self, a: RatNum, b: RatNum) -> RatNum:
        """
        @requires: a and b must be RatNum representing the limits of integration
        @modifies: nothing
        @effects: Computes the definite integral of this polynomial from a to b
        @throws: TypeError if a or b are not RatNum
        @returns: RatNum representing the value of the definite integral
        """
        if not isinstance(a, RatNum) or not isinstance(b, RatNum):
            raise TypeError("Integration limits a and b must be RatNum.")
        if self.is_nan() or a.is_nan() or b.is_nan():
            return RatNum(0, 0)
        antiderivative = self.anti_differentiate(RatNum(0))
        if antiderivative.is_nan(): 
            return RatNum(0,0)
        val_at_b = antiderivative.eval(b) # Integral = F(b) - F(a)
        val_at_a = antiderivative.eval(a)
        if val_at_b.is_nan() or val_at_a.is_nan():
            return RatNum(0,0)
        return val_at_b - val_at_a
    
    def value_of(self, x: RatNum):
        """
        Alias for eval(x)
        """
        return self.eval(x)

    def __eq__(self, other):
        """
        @requires: other must be a RatPoly
        @modifies: nothing
        @effects: checks equality of two polynomials
        @throws: none
        @returns: True if all degrees and coefficients match
        """
        if not isinstance(other, RatPoly):
            return False
        if self.is_nan():
            return other.is_nan()
        if other.is_nan():
            return False
        return isinstance(other, RatPoly) and self._coeffs == other._coeffs

    def __hash__(self):
        """
        @requires: none
        @modifies: nothing
        @effects: computes hash of the polynomial
        @throws: none
        @returns: int hash value
        """
        if self.is_nan():
            return hash((0, RatNum(0,0)))
        return hash(tuple(sorted(self._coeffs.items())))

    def __str__(self):
        """
        @requires: none
        @modifies: nothing
        @effects: converts the polynomial to string
        @throws: none
        @returns: human-readable string of the polynomial
        """
        if self.is_nan():
            return "NaN"
        if not self._coeffs:
            return "0"
        terms = []
        for deg in sorted(self._coeffs.keys(), reverse=True):
            coeff = self._coeffs[deg]
            if deg == 0:
                terms.append(str(coeff))
            elif deg == 1:
                terms.append(f"{coeff}*x")
            else:
                terms.append(f"{coeff}*x^{deg}")
        return " + ".join(terms)
