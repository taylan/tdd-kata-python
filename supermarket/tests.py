import unittest
from supermarket import CheckoutRegister, Item


class SupermarketCheckoutTestCase(unittest.TestCase):
    def setUp(self):
        self.target = CheckoutRegister()

    def test_when_item_added_total_price_is_updated(self):
        item1 = Item('i1', 10)
        self.target.scan(item1)

        self.assertEqual(self.target.total, 10)
