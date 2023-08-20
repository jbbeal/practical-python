# report.py
#
# Exercise 2.4

from fileparse import parse_csv
from stock import Stock
from tableformat import create_formatter

import csv

dow_converters = { h: float for h in ['price', 'open', 'low', 'high', 'change'] } | { h: int for h in ['volume', 'shares'] }
"Converter functions for numeric columns in reports."

def read_portfolio(portfolio_lines):
    return [
        Stock(p['name'], p['shares'], p['price'])
        for p in parse_csv(portfolio_lines, select=['name', 'shares', 'price'], converters=dow_converters)
    ]

def read_prices(prices_lines):
    return parse_csv(prices_lines, converters=dow_converters, headers=['name', 'price'])

def p_and_l(portfolio, prices):
    """Given a stock portfolio, represented as a list of dicts as returned by `read_portfolio` and a dict of current prices (as returned by
    `read_prices`), compute the total value of the portfolio and print overall gain and loss.

    """
    def summarize_holding(stock):
        holding = {
            'name': stock.name,
            'price': stock.price,
            'shares': stock.shares,
        }
        cur_price = prices[stock.name]
        holding['current_price'] = cur_price
        holding['original_price'] = stock.price
        holding['original_value'] = stock.cost
        holding['current_value'] = stock.shares * cur_price
        holding['gain'] = holding['current_value'] - holding['original_value']
        return holding
    return [ summarize_holding(h)
             for h in portfolio ]

def print_report(rep, formatter):
    """
    Given a profit-and-loss report (as returned by `p_and_l`, print the report in nicely formatted columns.
    """
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for r in rep:
        rowdata = [ r['name'], str(r['shares']), f'${r["price"]:0.2f}', f'{r["gain"]:0.2f}' ]
        formatter.row(rowdata)

def portfolio_report(portfolio_file='Data/portfolio.csv', prices_file='Data/prices.csv', fmt='txt'):
    with open(portfolio_file, 'rt') as port_file:
        with open(prices_file, 'rt') as pr_file:         
            portfolio = read_portfolio(port_file)
            prices = read_prices(pr_file)
            prices_dict = { p['name']: p['price'] for p in prices}
            print_report(p_and_l(portfolio, prices_dict), create_formatter(fmt))

def _main(argv):
    if len(argv) == 3:
        portfolio_report(argv[1], argv[2])
    elif len(argv) == 4:
        portfolio_report(argv[1], argv[2], argv[3])
    else:
        raise SystemExit(f'Usage: {sys.argv[0]} portfile pricefile')



if __name__ == '__main__':
    import sys

    _main(sys.argv)
