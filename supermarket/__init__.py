

class Item():
    def __init__(self, sku, price):
        self._sku = sku
        self._price = price

    @property
    def sku(self):
        return self._sku

    @property
    def price(self):
        return self._price


class CheckoutItem():
    def __init__(self, item, count=0):
        self._item = item
        self._count = count

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, val):
        self._count = val

    @property
    def item(self):
        return self._item


class CheckoutRegister():
    def __init__(self, pricing_rules=None):
        self._products = {}
        self._pricing_rules = pricing_rules or []

    def scan(self, item):
        prod = self._products.get(item.sku, CheckoutItem(item))
        prod.count += 1
        self._products[item.sku] = prod

    @property
    def unique_item_count(self):
        return len(self._products.keys())

    @property
    def total_without_discount(self):
        return sum([p.count * p.item.price for sku, p in self._products.items()])

    @property
    def total(self):
        totes = self.total_without_discount
        valid_rules = [r for r in self._pricing_rules
                       if r.is_valid(self._products)]

        for rule in valid_rules:
            totes = rule.execute(self._products, totes)

        return totes


class PricingRule():
    def is_valid(self, products):
        raise NotImplementedError()

    def execute(self, products, total):
        raise NotImplementedError()


class BuyXOfItemGetYFreePricingRule(PricingRule):
    """
    Pricing rule for 'Buy X quantity of one item, get Y quantity free'.
    So if it's "Buy 3, get 1 free for item 'i1'", when there are 4 of 'i1'
    in the register, the customer will only pay for 3.

    This rule acheives that buy subtracting the cost of the free item
    from the total.
    """

    def __init__(self, item, x, y):
        self._item = item
        self._x = x
        self._y = y

    def is_valid(self, products):
        ci = products.get(self._item.sku, None)
        return ci and ci.count >= (self._x + self._y)

    def execute(self, products, total):
        return total - (self._item.price *
                        (products.get(self._item.sku).count //
                         (self._x + self._y)))


class BuyItemXGetItemYFreePricingRule(PricingRule):
    """
    Pricing rule for buy 1 of item X, get item Y free.
    So if it's "Buy item i1, get item i2 free", when there are 1 i1 and 1 i2
    in the register, the 1 i2 will be free.

    If there are 4 i1s and 7 i2s, the customer will pay for 4 i1s and 3 i2s.
    """

    def __init__(self, item1, item2):
        self._item1 = item1
        self._item2 = item2

    def is_valid(self, products):
        return products.get(self._item1.sku, None) \
            and products.get(self._item2.sku)

    def execute(self, products, total):
        item_1_count = products[self._item1.sku].count
        item_2_count = products[self._item2.sku].count

        return total - (min(item_1_count, item_2_count) * self._item2.price)


class FlatDiscountPricingRule(PricingRule):
    def __init__(self, item, discount):
        self._item = item
        self._discount = discount
        if not isinstance(self._discount, float) or not 0 < self._discount <= 1:
            raise ValueError()

    def is_valid(self, products):
        return products.get(self._item.sku, None)

    def execute(self, products, total):
        ci = products[self._item.sku]
        return total - (ci.count * ci.item.price * self._discount)


class FlatDiscountOverCertainBasketSizePricingRule(PricingRule):
    def __init__(self, lower_limit, discount):
        self._lower_limit = lower_limit
        self._discount = discount

    def is_valid(self, products):
        return sum([p.count * p.item.price
                    for sku, p in products.items()]) > self._lower_limit

    def execute(self, products, total):
        return total - (total * self._discount)
