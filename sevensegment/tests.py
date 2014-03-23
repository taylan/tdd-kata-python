from unittest import TestCase
from sevensegment import SevenSegment


class SevenSegmentTest(TestCase):
    def setUp(self):
        self.target = SevenSegment()

    def test_display_single_digit(self):
        self.assertEqual(self.target.render(0), '._.\n|.|\n|_|')
