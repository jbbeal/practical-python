# report.py
#
# Exercise 2.4

from fileparse import parse_csv

import csv

dow_converters = { h: float for h in ['price', 'open', 'low', 'high', 'change'] } | { h: int for h in ['volume', 'shares'] }
"Converter functions for numeric columns in reports."

def read_portfolio(portfolio_lines):
    return parse_csv(portfolio_lines, select=['name', 'shares', 'price'], converters=dow_converters)

def read_prices(prices_lines):
    return parse_csv(prices_lines, converters=dow_converters, headers=['name', 'price'])

def p_and_l(portfolio, prices):
    """Given a stock portfolio, represented as a list of dicts as returned by `read_portfolio` and a dict of current prices (as returned by
    `read_prices`), compute the total value of the portfolio and print overall gain and loss.

    """
    def summarize_holding(holding):
        price = holding['price']
        shares = holding['shares']
        cur_price = prices[holding['name']]
        holding['current_price'] = cur_price
        holding['original_price'] = price
        holding['original_value'] = shares * price
        holding['current_value'] = shares * cur_price
        holding['gain'] = holding['current_value'] - holding['original_value']
        return holding
    return [ summarize_holding(h)
             for h in portfolio ]

def print_report(rep):
    """
    Given a profit-and-loss report (as returned by `p_and_l`, print the report in nicely formatted columns.
    """
    def print_headers():
        sep = '-'
        print(f"{'Name':<8s} {'Shares':>10s} {'Price':>10s} {'Change':>10s}")
        print(sep*8,sep*10,sep*10,sep*10)
    def format(line):
        print(f"{line[0]:<8s} {line[1]:>10d} {line[2]:>10s} {line[3]:>10.2f}")
    def currency(num):
        return f"${num:0,.2f}"
    
    print_headers()
    for line in rep:
        format((line['name'], line['shares'], currency(line['current_price']), line['current_price'] - line ['original_price']))

def portfolio_report(portfolio_file='Data/portfolio.csv', prices_file='Data/prices.csv'):
    with open(portfolio_file, 'rt') as port_file:
        with open(portfolio_file, 'rt') as pr_file:         
            portfolio = read_portfolio(port_file)
            prices = read_prices(pr_file)
            prices_dict = { p['name']: p['price'] for p in prices}
            print_report(p_and_l(portfolio, prices_dict))

def _main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage: {sys.argv[0]} portfile pricefile')
    portfolio_report(argv[1], argv[2])


if __name__ == '__main__':
    import sys

    _main(sys.argv)
