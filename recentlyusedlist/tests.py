import unittest
from recentlyusedlist import RecentlyUsedList


class RecentlyUsedListsTestCase(unittest.TestCase):
    def setUp(self):
        self.target = RecentlyUsedList()

    def test_new_list_has_length_zero(self):
        self.assertEqual(len(self.target), 0)

    def test_can_add_new_item(self):
        self.target.add('a')
        self.assertEqual(len(self.target), 1)

    def test_duplicate_items_not_allowed(self):
        self.target.add('a')
        self.target.add('a')
        self.target.add('b')
        self.assertEqual(len(self.target), 2)

    def test_null_insertions_not_allowed(self):
        self.target.add(None)
        self.assertEqual(len(self.target), 0)

    def test_empty_strings_not_allowed(self):
        self.target.add('')
        self.assertEqual(len(self.target), 0)
