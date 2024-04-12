import unittest
from fizzbuzz.fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz(self):
        self.assertEqual(fizzbuzz(3), "Fizz")
        self.assertEqual(fizzbuzz(5), "Buzz")
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
        self.assertEqual(fizzbuzz(7), "7")
        self.assertEqual(fizzbuzz(11), "11")

if __name__ == '__main__':
    unittest.main()