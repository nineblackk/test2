# test_prime_numbers.py

import unittest
from prime_numbers import is_prime, find_primes

class TestPrimeNumbers(unittest.TestCase):
    
    def test_is_prime(self):
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(13))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(1))
    
    def test_find_primes(self):
        self.assertEqual(find_primes(10), [2, 3, 5])
        self.assertEqual(find_primes(20), [2, 3, 5, 7, 11, 13, 17, 19])

if __name__ == "__main__":
    unittest.main()
