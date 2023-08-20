import unittest
from stock import Stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_cost(self):
        s = Stock('MSFT', 53, 48.7)
        self.assertEqual(s.cost, 53*48.7)

    def test_sell(self):
        s = Stock('AMZN', 100, 54.8)
        s.sell(25)
        self.assertEqual(s.shares, 75)
        self.assertEqual(s.cost, 75 * 54.8)

    def test_bad_shares(self):
        s = Stock('JPM', 100, 47.8)
        with self.assertRaises(TypeError):
            s.shares = '150'

if __name__ == '__main__':
    unittest.main()
