"""
This script it to unit test math problem.
"""
import unittest
import math_problem as mp

class TestMathProblem(unittest.TestCase):
    def test_calc_product(self):
        self.assertEqual(mp.calc_product(2,3), 7, 'Incorrect product!')

    def test_calc_difference(self):
        self.assertEqual(mp.calc_difference(4,2), 2, 'Incorrect difference!')

    def test_calc_sum(self):
        self.assertEqual(sum([1,2,3]), 2, 'Incorrect summation!')

if __name__ == "__main__":
    unittest.main()