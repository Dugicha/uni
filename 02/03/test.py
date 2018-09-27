import unittest
from main import (to_bin, to_dec, get_bit_size, get_dec_sign, flip_bits,
    excess_bias_dec_to_bin, excess_bias_bin_to_dec)

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

    def test_flip_bits(self):
        self.assertEqual(flip_bits("10"), "01")
        self.assertEqual(flip_bits("0"), "1")
        self.assertEqual(flip_bits("1"), "0")
        self.assertEqual(flip_bits("101111000001"), "010000111110")
        self.assertEqual(flip_bits("101"), "010")
        self.assertEqual(flip_bits("10000"), "01111")

    def test_get_dec_sign(self):
        self.assertEqual(get_dec_sign("+100"), "+")
        self.assertEqual(get_dec_sign("-7"), "-")
        self.assertEqual(get_dec_sign("12"), "+")
        self.assertEqual(get_dec_sign("0"), "+")
        self.assertEqual(get_dec_sign("-0"), "-")

    def test_excess_bias_dec_to_bin(self):
        self.assertEqual(excess_bias_dec_to_bin("1"), "1")
        self.assertEqual(excess_bias_dec_to_bin("0"), "0")
        self.assertEqual(excess_bias_dec_to_bin("-1"), "01")
        self.assertEqual(excess_bias_dec_to_bin("-2"), "00")
        self.assertEqual(excess_bias_dec_to_bin("2"), "110")
        self.assertEqual(excess_bias_dec_to_bin("3"), "111")
        self.assertEqual(excess_bias_dec_to_bin("-3"), "001")
        self.assertEqual(excess_bias_dec_to_bin("-4"), "000")
        self.assertEqual(excess_bias_dec_to_bin("-7"), "0001")
        self.assertEqual(excess_bias_dec_to_bin("7"), "1111")
        self.assertEqual(excess_bias_dec_to_bin("-8"), "0000")
        self.assertEqual(excess_bias_dec_to_bin("8"), "11000")
        self.assertEqual(excess_bias_dec_to_bin("69"), "11000101")
        self.assertEqual(excess_bias_dec_to_bin("-69"), "00111011")
        self.assertEqual(excess_bias_dec_to_bin("6"), "1110")
        self.assertEqual(excess_bias_dec_to_bin("5"), "1101")

    def test_excess_bias_dec_to_bin(self):
        self.assertEqual(excess_bias_bin_to_dec("1"), "1")
        self.assertEqual(excess_bias_bin_to_dec("0"), "0")
        self.assertEqual(excess_bias_bin_to_dec("01"), "-1")
        self.assertEqual(excess_bias_bin_to_dec("00"), "-2")
        self.assertEqual(excess_bias_bin_to_dec("110"), "2")
        self.assertEqual(excess_bias_bin_to_dec("111"), "3")
        self.assertEqual(excess_bias_bin_to_dec("001"), "-3")
        self.assertEqual(excess_bias_bin_to_dec("000"), "-4")
        self.assertEqual(excess_bias_bin_to_dec("0001"), "-7")
        self.assertEqual(excess_bias_bin_to_dec("1111"), "7")
        self.assertEqual(excess_bias_bin_to_dec("0000"), "-8")
        self.assertEqual(excess_bias_bin_to_dec("11000"), "8")
        self.assertEqual(excess_bias_bin_to_dec("11000101"), "69")
        self.assertEqual(excess_bias_bin_to_dec("00111011"), "-69")
        self.assertEqual(excess_bias_bin_to_dec("1110"), "6")
        self.assertEqual(excess_bias_bin_to_dec("1101"), "5")

if __name__ == "__main__":
    unittest.main()