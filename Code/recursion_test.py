#!python

from recursion import factorial, permutations, combinations
import unittest


class FactorialTest(unittest.TestCase):
    def test_factorial_with_small_integers(self):
        # factorial should return the product n*(n-1)*...*2*1 for n >= 0
        assert factorial(0) == 1  # base case
        assert factorial(1) == 1  # base case
        assert factorial(2) == 2*1
        assert factorial(3) == 3*2*1
        assert factorial(4) == 4*3*2*1
        assert factorial(5) == 5*4*3*2*1
        assert factorial(6) == 6*5*4*3*2*1
        assert factorial(7) == 7*6*5*4*3*2*1
        assert factorial(8) == 8*7*6*5*4*3*2*1
        assert factorial(9) == 9*8*7*6*5*4*3*2*1
        assert factorial(10) == 10*9*8*7*6*5*4*3*2*1

    def test_factorial_with_large_integers(self):
        assert factorial(15) == 1307674368000
        assert factorial(20) == 2432902008176640000
        assert factorial(25) == 15511210043330985984000000
        assert factorial(30) == 265252859812191058636308480000000

    def test_factorial_with_negative_integers(self):
        # factorial should raise a ValueError for n < 0
        with self.assertRaises(ValueError, msg='function undefined for n < 0'):
            factorial(-1)
            factorial(-5)

    def test_factorial_with_floating_point_numbers(self):
        # factorial should raise a ValueError for non-integer n
        with self.assertRaises(ValueError, msg='function undefined for float'):
            factorial(2.0)
            factorial(3.14159)

class PermutationTest(unittest.TestCase):
    def test_permutation(self):
        assert permutations("0") == ["0"]
        assert permutations("1") == ["1"]
        assert permutations("2") == ["2"]
        assert permutations("3") == ["3"]
        assert permutations("12") == ["12", "21"]
        assert permutations("23") == ["23", "32"]
        three = permutations("123")
        three.sort()
        assert three == ["123", "132", "213", "231", "312", "321"]
        four = permutations("1234")
        four.sort()
        assert four == ['1234', '1234', '1324', '1324', '2134', '2134', '2314', '2314', '2341', '2341', '2431', '2431', '3124', '3124', '3214', '3214', '3241', '3241', '3421', '3421', '4231', '4231', '4321', '4321']
        
if __name__ == '__main__':
    unittest.main()
