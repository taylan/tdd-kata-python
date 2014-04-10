import unittest
from supermarket import CheckoutRegister, Item


class SupermarketCheckoutTestCase(unittest.TestCase):
    def setUp(self):
        self.target = CheckoutRegister()

    @staticmethod
    def _get_items(count):
        return [Item('i{0}'.format(i), i * 10) for i in range(1, count+1)]

    def _scan_items(self, count):
        for item in self._get_items(count):
            self.target.scan(item)

    def test_when_item_added_total_price_is_updated(self):
        self._scan_items(1)

        self.assertEqual(self.target.total, 10)

    def test_multiple_item_prices_calculated_correctly(self):
        self._scan_items(2)

        self.assertEqual(self.target.total, 30)

    def test_checkout_with_multiple_items_shows_correct_item_count(self):
        self._scan_items(2)

        self.assertEqual(self.target.unique_item_count, 2)
