

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


class CheckoutRegister():
    def __init__(self):
        self._products = []

    def scan(self, item):
        self._products.append(item.price)

    @property
    def total(self):
        return sum(self._products)
