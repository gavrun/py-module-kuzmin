import unittest
 
def square(n):
    return n*n
 
def cube(n):
    return n*n*n
 
class Test(unittest.TestCase):
    def test_square(self):
        self.assertEquals(square(2), 4)
 
    def test_cube1(self):
        self.assertEquals(cube(2), 8)

    def test_cube2(self):
        self.assertEquals(cube('abc'), 8)
