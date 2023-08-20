import unittest
from stock import Stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEquals(s.name, 'GOOG')
        self.assertEquals(s.shares, 100)
        self.assertEquals(s.price, 490.1)

if __name__ == '__main__':
    unittest.main()
