import unittest
from leapyear import is_leap_year


class LeapYearTestCase(unittest.TestCase):
    def test_leap_year_if_divisible_by_4(self):
        self.assertTrue(is_leap_year(4))
        self.assertTrue(is_leap_year(1600))
        self.assertTrue(is_leap_year(1200))

    def test_not_leap_year_if_divisible_by_100(self):
        self.assertFalse(is_leap_year(1800))
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(2500))

    def test_leap_year_if_divisible_by_400(self):
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(2400))
