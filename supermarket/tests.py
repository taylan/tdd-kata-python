import unittest
from unittest.mock import Mock, MagicMock
from supermarket import CheckoutRegister, Item, PricingRule
from supermarket import BuyXGetYFreePricingRule


class SupermarketCheckoutTestCase(unittest.TestCase):
    def setUp(self):
        self.target = self._get_register()

    @staticmethod
    def _get_register():
        return CheckoutRegister()

    @staticmethod
    def _get_register_with_pricing_rules(rules):
        return CheckoutRegister(rules)

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

    def test_checkout_with_pricing_rule_checks_if_rule_is_valid(self):
        mock_rule = Mock(spec=PricingRule)
        target = self._get_register_with_pricing_rules([mock_rule])
        total = target.total

        self.assertTrue(mock_rule.is_valid.called)

    def test_checkout_pricing_rules_are_executed(self):
        mock_rule = Mock(spec=PricingRule)
        mock_rule._validator = lambda x: True
        target = self._get_register_with_pricing_rules([mock_rule])
        total = target.total

        self.assertTrue(mock_rule.execute.called)

    def test_checkout_only_valid_pricing_rules_are_executed(self):
        mock_rule1 = Mock(spec=PricingRule)
        mock_rule1.is_valid = MagicMock(return_value=True)

        mock_rule2 = Mock(spec=PricingRule)
        mock_rule2.is_valid = MagicMock(return_value=False)

        target = self._get_register_with_pricing_rules([mock_rule1, mock_rule2])
        total = target.total

        self.assertTrue(mock_rule1.execute.called)
        self.assertFalse(mock_rule2.execute.called)


class BuyXGetYFreePricingRuleTestCase(unittest.TestCase):
    def test_validity_check_returns_false_when_there_are_not_enough_products(self):
        # arrange
        item1 = Item('i1', 10)
        rule = BuyXGetYFreePricingRule(item1, 3, 1)
        register = CheckoutRegister([rule])

        # act
        for i in range(2):
            register.scan(item1)
        total = register.total

        #assert
        self.assertEqual(total, 20)

    def test_validity_check_returns_true_when_there_are_enough_products(self):
        # arrange
        item1 = Item('i1', 10)
        rule = BuyXGetYFreePricingRule(item1, 3, 1)
        register = CheckoutRegister([rule])

        # act
        for i in range(4):
            register.scan(item1)

        #assert
        self.assertTrue(rule.is_valid(register._products))

    def test_rule_calculates_discount_correctly(self):
        # arrange
        item1 = Item('i1', 10)
        rule = BuyXGetYFreePricingRule(item1, 3, 1)
        register = CheckoutRegister([rule])

        # act
        for i in range(4):
            register.scan(item1)
        total = register.total

        #assert
        self.assertEqual(total, 30)
