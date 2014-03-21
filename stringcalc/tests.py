from unittest import TestCase
from stringcalc import StringCalculator


class StringCalculatorTest(TestCase):

    def _init_calculator(self):
        return StringCalculator()

    def setUp(self):
        self.target = self._init_calculator()

    def test_empty_string_gives_0(self):
        self.assertEqual(self.target.add(''), 0)

    def test_multiple_empty_string_gives_0(self):
        self.assertEqual(self.target.add(' '), 0)

    def test_single_number_gives_itself(self):
        self.assertEqual(self.target.add('1'), 1)
        self.assertEqual(self.target.add('123'), 123)

    def test_two_numbers_gives_sum(self):
        self.assertEqual(self.target.add('1,2'), 3)

    def test_new_line_allowed_as_seperator(self):
        self.assertEqual(self.target.add('1\n2'), 3)

    def test_new_line_with_empty_line_disallowed(self):
        self.assertEqual(self.target.add('1,\n'), '')

    def test_different_delimiters_in_input(self):
        self.assertEqual(self.target.add('1\n2,3'), 6)
        self.assertEqual(self.target.add('1,2\n3'), 6)

    def test_custom_delimiter_specification(self):
        self.assertEqual(self.target.add('//;\n1;2;3'), 6)
