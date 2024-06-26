import unittest

from prime_num import is_prime

class TestPrime(unittest.TestCase):
    def test_float(self):
        self.assertFalse(is_prime(11.1))
    def test_zero(self):
        self.assertFalse(is_prime(0))
    def test_negative(self):
        self.assertFalse(is_prime(-1))
    def test_one(self):
        self.assertFalse(is_prime(1))
    def test_two(self):
        self.assertTrue(is_prime(2))
    def test_four(self):
        self.assertFalse(is_prime(4))
    def test_five(self):
        self.assertTrue(is_prime(5))
    def test_nine(self):
        self.assertFalse(is_prime(9))
    def test_eleven(self):
        self.assertTrue(is_prime(11))

if __name__=='__main__':
    unittest.main()