import unittest
from unittest.mock import Mock, MagicMock
from supermarket import CheckoutRegister, Item, PricingRule
from supermarket import (BuyXOfItemGetYFreePricingRule,
                         BuyItemXGetItemYFreePricingRule,
                         FlatDiscountPricingRule,
                         FlatDiscountOverCertainBasketSizePricingRule)


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


class PricingRuleBaseTestCase(unittest.TestCase):
    def test_pricing_rule_base_is_valid_raises_not_implemented_error(self):
        rule = PricingRule()
        with self.assertRaises(NotImplementedError):
            rule.is_valid([])

    def test_pricing_rule_base_execute_raises_not_implemented_error(self):
        rule = PricingRule()
        with self.assertRaises(NotImplementedError):
            rule.execute([], 0)


class BuyXOfItemGetYFreePricingRuleTestCase(unittest.TestCase):
    def test_validity_check_returns_false_when_there_are_not_enough_products(self):
        # arrange
        item1 = Item('i1', 10)
        rule = BuyXOfItemGetYFreePricingRule(item1, 3, 1)
        register = CheckoutRegister([rule])

        # act
        for i in range(2):
            register.scan(item1)
        total = register.total

        #assert
        self.assertFalse(rule.is_valid(register._products))

    def test_validity_check_returns_true_when_there_are_enough_products(self):
        # arrange
        item1 = Item('i1', 10)
        rule = BuyXOfItemGetYFreePricingRule(item1, 3, 1)
        register = CheckoutRegister([rule])

        # act
        for i in range(4):
            register.scan(item1)

        #assert
        self.assertTrue(rule.is_valid(register._products))

    def test_rule_calculates_discount_correctly(self):
        # arrange
        item1 = Item('i1', 10)
        rule = BuyXOfItemGetYFreePricingRule(item1, 3, 1)
        register = CheckoutRegister([rule])

        # act
        for i in range(4):
            register.scan(item1)
        total = register.total

        #assert
        self.assertEqual(total, 30)


class BuyItemXGetItemYFreePricingRuleTestCase(unittest.TestCase):
    def test_validity_check_returns_false_when_item_x_is_not_in_register(self):
        item1 = Item('i1', 10)
        item2 = Item('i2', 20)
        rule = BuyItemXGetItemYFreePricingRule(item1, item2)
        register = CheckoutRegister([rule])

        register.scan(item2)

        self.assertFalse(rule.is_valid(register._products))

    def test_validity_check_returns_false_when_item_y_is_not_in_register(self):
        item1 = Item('i1', 10)
        item2 = Item('i2', 20)
        rule = BuyItemXGetItemYFreePricingRule(item1, item2)
        register = CheckoutRegister([rule])

        register.scan(item1)

        self.assertFalse(rule.is_valid(register._products))

    def test_validity_check_returns_true_when_both_items_are_in_register(self):
        item1 = Item('i1', 10)
        item2 = Item('i2', 20)
        rule = BuyItemXGetItemYFreePricingRule(item1, item2)
        register = CheckoutRegister([rule])

        register.scan(item1)
        register.scan(item2)

        self.assertTrue(rule.is_valid(register._products))

    def test_rule_calculates_discount_correctly(self):
        item1 = Item('i1', 10)
        item2 = Item('i2', 20)
        rule = BuyItemXGetItemYFreePricingRule(item1, item2)
        register = CheckoutRegister([rule])

        register.scan(item1)
        register.scan(item2)

        self.assertEqual(register.total, 10)

    def test_rule_discounts_correctly_when_there_are_more_Xs_than_Ys(self):
        item1 = Item('i1', 10)
        item2 = Item('i2', 20)
        rule = BuyItemXGetItemYFreePricingRule(item1, item2)
        register = CheckoutRegister([rule])

        for i in range(4):
            register.scan(item1)
        for i in range(2):
            register.scan(item2)

        self.assertEqual(register.total, 40)

    def test_rule_discounts_correctly_when_there_are_more_Ys_than_Xs(self):
        item1 = Item('i1', 10)
        item2 = Item('i2', 20)
        rule = BuyItemXGetItemYFreePricingRule(item1, item2)
        register = CheckoutRegister([rule])

        for i in range(4):
            register.scan(item1)
        for i in range(7):
            register.scan(item2)

        self.assertEqual(register.total, 100)


class FlatDiscountPricingRuleTestCase(unittest.TestCase):
    def test_validity_check_succeeds_when_discounted_item_is_in_register(self):
        item1 = Item('i1', 10)
        rule = FlatDiscountPricingRule(item1, 0.1)
        register = CheckoutRegister([rule])
        register.scan(item1)

        self.assertTrue(rule.is_valid(register._products))

    def test_init_with_negative_discount_value_raises_value_error(self):
        with self.assertRaises(ValueError):
            FlatDiscountPricingRule(Item('i1', 10), -1)

    def test_init_with_zero_discount_value_raises_value_error(self):
        with self.assertRaises(ValueError):
            FlatDiscountPricingRule(Item('i1', 10), 0)

    def test_init_with_discount_greater_than_1_raises_value_error(self):
        with self.assertRaises(ValueError):
            FlatDiscountPricingRule(Item('i1', 10), 2)

    def test_init_with_non_float_discount_value_raises_value_error(self):
        with self.assertRaises(ValueError):
            FlatDiscountPricingRule(Item('i1', 10), 1)

    def test_rule_discounts_correctly_for_single_item(self):
        item1 = Item('i1', 100)
        rule = FlatDiscountPricingRule(item1, 0.2)
        register = CheckoutRegister([rule])
        register.scan(item1)

        self.assertEqual(register.total, 80)

    def test_rule_discounts_correctly_for_multiple_items(self):
        item1 = Item('i1', 100)
        rule = FlatDiscountPricingRule(item1, 0.2)
        register = CheckoutRegister([rule])
        for i in range(10):
            register.scan(item1)

        self.assertEqual(register.total, 800)


class FlatDiscountOverCertainBasketSizePricingRuleTestCase(unittest.TestCase):
    def test_discount_is_not_applied_when_total_cost_under_limit(self):
        rule = FlatDiscountOverCertainBasketSizePricingRule(200, 0.1)
        register = CheckoutRegister([rule])

        self.assertFalse(rule.is_valid(register._products))

    def test_discount_is_applied_correctly(self):
        rule = FlatDiscountOverCertainBasketSizePricingRule(200, 0.1)
        register = CheckoutRegister([rule])

        item1 = Item('i1', 30)
        for i in range(10):
            register.scan(item1)

        self.assertEqual(register.total, 270)
