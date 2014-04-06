import unittest
from recentlyusedlist import RecentlyUsedList


class RecentlyUsedListsTestCase(unittest.TestCase):
    def setUp(self):
        self.target = RecentlyUsedList()

    def test_new_list_has_length_zero(self):
        self.assertEqual(len(self.target), 0)

    def test_can_add_new_item(self):
        self.target.add(1)
        self.assertEqual(len(self.target), 1)
