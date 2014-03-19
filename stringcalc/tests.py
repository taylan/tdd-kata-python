from unittest import TestCase
from stringcalc import StringCalculator


class StringCalculatorTest(TestCase):

    def setUp(self):
        self.target = StringCalculator()

    def test_empty_string_gives_0(self):
        self.assertEqual(self.target.add(''), 0)

    def test_single_number_gives_itself(self):
        self.assertEqual(self.target.add('1'), 1)
        self.assertEqual(self.target.add('123'), 123)

    def test_two_numbers_gives_sum(self):
        self.assertEqual(self.target.add('1 2'), 3)
