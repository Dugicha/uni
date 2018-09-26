import unittest
from main import (to_bin, to_dec, get_bit_size, get_dec_sign, 
    excess_bias_dec_to_bin)

class TestMain(unittest.TestCase):

    def test_to_bin(self):
        self.assertEqual(to_bin(0), "0")
        self.assertEqual(to_bin(1), "1")
        self.assertEqual(to_bin(2), "10")
        self.assertEqual(to_bin(11), "1011")
        self.assertEqual(to_bin(64), "1000000")
        self.assertEqual(to_bin(784), "1100010000")

    def test_to_dec(self):
        self.assertEqual(to_dec("0"), 0)
        self.assertEqual(to_dec("1"), 1)
        self.assertEqual(to_dec("10"), 2)
        self.assertEqual(to_dec("1011"), 11)
        self.assertEqual(to_dec("1000000"), 64)
        self.assertEqual(to_dec("1100010000"), 784)

    def test_get_bit_size(self):
        self.assertEqual(get_bit_size(7), 3)
        self.assertEqual(get_bit_size(8), 4)
        self.assertEqual(get_bit_size(0), 1)
        self.assertEqual(get_bit_size(1), 1)
        self.assertEqual(get_bit_size(127), 7)
        self.assertEqual(get_bit_size(128), 8)

    def test_get_dec_sign(self):
        self.assertEqual(get_dec_sign("+100"), "+")
        self.assertEqual(get_dec_sign("-7"), "-")
        self.assertEqual(get_dec_sign("12"), "+")
        self.assertEqual(get_dec_sign("0"), "+")
        self.assertEqual(get_dec_sign("-0"), "-")

    def test_excess_bias_dec_to_bin(self):
        pass

if __name__ == "__main__":
    unittest.main()