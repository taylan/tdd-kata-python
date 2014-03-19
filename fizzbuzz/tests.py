from unittest import TestCase
from fizzbuzz import FizzBuzz


class FizzBuzzTest(TestCase):
    def setUp(self):
        self.target = FizzBuzz()

    def test_multiples_of_three_return_fizz(self):
        self.assertEqual(self.target.calc_fizz_buzz(3), 'Fizz')
        self.assertEqual(self.target.calc_fizz_buzz(9), 'Fizz')
        self.assertEqual(self.target.calc_fizz_buzz(81), 'Fizz')

    def test_multiples_of_five_return_buzz(self):
        self.assertEqual(self.target.calc_fizz_buzz(5), 'Buzz')
        self.assertEqual(self.target.calc_fizz_buzz(25), 'Buzz')

    def test_multiples_of_fifteen_return_fizzbuzz(self):
        self.assertEqual(self.target.calc_fizz_buzz(45), 'FizzBuzz')
        self.assertEqual(self.target.calc_fizz_buzz(75), 'FizzBuzz')

    def test_values_less_than_one_return_none(self):
        self.assertIsNone(self.target.calc_fizz_buzz(0))
        self.assertIsNone(self.target.calc_fizz_buzz(-1))

    def test_values_greater_than_100_return_none(self):
        self.assertIsNone(self.target.calc_fizz_buzz(101))
        self.assertIsNone(self.target.calc_fizz_buzz(200))
