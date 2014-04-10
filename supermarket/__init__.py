

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
    def __init__(self):
        self._products = {}

    def scan(self, item):
        prod = self._products.get(item.sku, CheckoutItem(item))
        prod.count += 1
        self._products[item.sku] = prod

    @property
    def unique_item_count(self):
        return len(self._products.keys())

    @property
    def total(self):
        return sum([p.count * p.item.price for sku, p in self._products.items()])


__all__ = ['Item', 'CheckoutRegister']
