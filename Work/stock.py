class Stock:
    __slots__ = ['name', '_shares', 'price']
    def __init__(self, name, shares, price):
        self.name = name
        self._shares = shares
        self.price = price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError('shares must be an integer')
        if value < 0:
            raise ValueError('shares cannot be negative')
        self._shares = value

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, shares_to_sell):
        if shares_to_sell > self.shares:
            raise ValueError(f"Cannot sell more shares ({shares_to_sell}) than you own ({self.shares})")
        self.shares -= shares_to_sell

    def __repr__(self):
        return f'Stock({self.name},{self.shares:d},{self.price:.2f})'


class NewStock(Stock):
    def yow(self):
        print('Yow!')

