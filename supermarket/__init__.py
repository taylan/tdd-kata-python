

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

    def __repr__(self):
        return 'CheckoutItem: {0}-#{1}'.format(self._item.sku, self._count)


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
    def total(self):
        totes = sum([p.count * p.item.price for sku, p in self._products.items()])
        valid_rules = [r for r in self._pricing_rules
                       if r.is_valid(self._products)]

        print(valid_rules)

        for rule in valid_rules:
            totes = rule.execute(self._products, totes)

        return totes


class PricingRule():
    def __init__(self, validator):
        self._validator = validator

    def is_valid(self, products):
        return self._validator(products)

    def execute(self, products, total):
        pass


class BuyXGetYFreePricingRule(PricingRule):
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


__all__ = ['Item', 'CheckoutRegister']
