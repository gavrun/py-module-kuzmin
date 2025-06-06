"""
This module demonstrates the use of doctest
"""

def cross_product(vec1, vec2):
        """

        This function computes the cross product of two 3-element numeric vectors.

        Keyword arguments:
        vec1, vec2 -- tuples each representing a vector with three numeric elements.

        Return value:
        A 3-element tuple of the cross product vec1 x vec2

        Examples:

        >>> cross_product((1, 2, 3), (4, 5, 6))
        (-3, 6, -3)

        """

        # cross = (vec1[0] * vec2[2] - vec1[2] * vec2[1],
        #          vec1[2] * vec2[0] - vec1[0] * vec2[2],
        #          vec1[0] * vec2[1] - vec1[1] * vec2[0])
        cross = (vec1[1] * vec2[2] - vec1[2] * vec2[1],
                 vec1[2] * vec2[0] - vec1[0] * vec2[2],
                 vec1[0] * vec2[1] - vec1[1] * vec2[0])
        return cross

if __name__ == "__main__":
        import doctest
        doctest.testmod()
