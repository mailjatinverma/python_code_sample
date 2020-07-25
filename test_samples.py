"""Module to test the samples module functionality"""

import unittest

from python_code_sample.samples import sum_primes, is_triangle



class TestSamples(unittest.TestCase):
    """TestClass for Samples module functionality test"""

    def test_sum_primes(self):
        """tests the sum_primes method"""
        self.assertEqual(sum_primes(10), 17)
        self.assertEqual(sum_primes(977), 73156)
        self.assertRaises(TypeError, sum_primes(12.5))
        # TypeError: 'float' object cannot be interpreted as an integer

    def test_is_triangle(self):
        """tests the is_triangle method"""
        self.assertTrue(is_triangle(3, 4, 5))
        self.assertFalse(is_triangle(1, 4, 2))
        self.assertFalse(is_triangle(4, 4, 8))


if __name__ == '__main__':
    unittest.main()
