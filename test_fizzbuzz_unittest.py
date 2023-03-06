import unittest

from fizz_buzz import *


class FizzBuzzTest(unittest.TestCase):
    def test_divisible_by_3(self):
        return_value = fizzbuzz(9)
        self.assertEqual("Fizz", return_value)

    def test_divisible_by_5(self):
        return_value = fizzbuzz(10)
        self.assertEqual("Buzz", return_value)

    def test_divisible_by_3_and_5(self):
        return_value = fizzbuzz(15)
        self.assertEqual("FizzBuzz", return_value)

    def test_not_divisible_by_3_and_5(self):
        return_value = fizzbuzz(17)
        self.assertEqual("17", return_value)    

    def test_fails_for_invalid_number_input(self):
        with self.assertRaises(Exception) as context:
            fizzbuzz("invalid")
            self.assertTrue("Invalid input" in str(context.exception))


if __name__ == '__main__':
    unittest.main()