class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        return self.shares * self.price

    def sell(self, shares_to_sell):
        if shares_to_sell > self.shares:
            raise ValueError(f"Cannot sell more shares ({shares_to_sell}) than you own ({self.shares})")
        self.shares -= shares_to_sell

    def __repr__(self):
        return f'Stock({self.name},{self.shares:d},{self.price:.2f})'
