from unittest import TestCase
from sevensegment import SevenSegment


class SevenSegmentTest(TestCase):
    def setUp(self):
        self.target = SevenSegment()

    def test_display_single_digit(self):
        self.assertEqual(self.target.render(0), '._.\n|.|\n|_|')
        self.assertEqual(self.target.render(7), '._.\n..|\n..|')

    def test_display_two_digits(self):
        self.assertEqual(self.target.render(12), '... ._.\n..| ._|\n..| |_.')

    def test_display_multiple_digits(self):
        self.assertEqual(self.target.render(738), '._. ._. ._.\n..| ._| |_|\n..| ._| |_|')
