import unittest
from supermarket import CheckoutRegister, Item


class SupermarketCheckoutTestCase(unittest.TestCase):
    def setUp(self):
        self.target = CheckoutRegister()

    def test_when_item_added_total_price_is_updated(self):
        item1 = Item('i1', 10)
        self.target.scan(item1)

        self.assertEqual(self.target.total, 10)

    def test_multiple_item_prices_calculated_correctly(self):
        item1 = Item('i1', 10)
        item2 = Item('i2', 30)

        self.target.scan(item1)
        self.target.scan(item2)

        self.assertEqual(self.target.total, 40)

