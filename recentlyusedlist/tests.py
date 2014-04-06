import unittest
from recentlyusedlist import RecentlyUsedList


class RecentlyUsedListsTestCase(unittest.TestCase):
    def setUp(self):
        self.target = RecentlyUsedList()

    def _fill_list_basic(self):
        self.target.add('a')
        self.target.add('b')
        self.target.add('c')

    def test_new_list_has_length_zero(self):
        self.assertEqual(len(self.target), 0)

    def test_list_can_be_initialized_with_values(self):
        lst = RecentlyUsedList(['a', 'b', 'c'])
        self.assertListEqual(list(lst), ['a', 'b', 'c'])

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

    def test_most_recently_added_item_is_first(self):
        self._fill_list_basic()

        self.assertEqual(self.target[0], 'c')

    def test_least_recently_added_item_is_last(self):
        self._fill_list_basic()

        self.assertEqual(self.target[-1], 'a')

    def test_only_int_can_be_used_as_indexer(self):
        with self.assertRaises(TypeError):
            self.target['x']

    def test_accessing_non_existant_index_raises_index_error(self):
        with self.assertRaises(IndexError):
            self.target[0]

    def test_last_method_returns_least_recently_added_item(self):
        self._fill_list_basic()

        self.assertEqual(self.target.last(), 'a')

    def test_first_method_most_recently_added_item(self):
        self._fill_list_basic()

        self.assertEqual(self.target.first(), 'c')

    def test_can_be_converted_to_list(self):
        self._fill_list_basic()

        self.assertListEqual(list(self.target), ['c', 'b', 'a'])

    def test_can_be_reversed(self):
        self._fill_list_basic()

        self.assertListEqual(list(reversed(self.target)), ['a', 'b', 'c'])
