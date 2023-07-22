# report.py
#
# Exercise 2.4

import csv

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        r = csv.reader(f)
        headers = next(r)
        for row in r:
            holding = (row[0], int(row[1]), float(row[2]))
            portfolio.append(holding)
    return portfolio

def read_portfolio_dict(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        r = csv.reader(f)
        headers = next(r)
        for row in r:
            holding = {
                'name': row[0],
                'shares': int(row[1]),
                'price': float(row[2])
            }
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    lookup = {}
    with open(filename, 'rt') as f:
        r = csv.reader(f)
        for row in r:
            try:
                if len(row) == 2:
                    lookup[row[0]] = float(row[1])
            except ValueError:
                print(f"Error parsing {row}")
    return lookup

def p_and_l(portfolio, prices):
    """
    Given a stock portfolio, represented as a list of dicts as returned by `read_portfolio_dict`
    and a dict of current prices (as returned by `read_prices`), compute the total value of the
    portfolio and print overall gain and loss.
    """
    cur_portfolio = []
    for record in portfolio:
        name = record['name']
        price = record['price']
        shares = record['shares']
        cur_price = prices[name]
        orig_value = shares * price
        cur_value = shares * cur_price
        cur_portfolio.append({
            'name': name,
            'shares': shares,
            'original_value': orig_value,
            'current_value': cur_value,
            'gain': cur_value - orig_value # negatives are losses
            })
    return cur_portfolio
