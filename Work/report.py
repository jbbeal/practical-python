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
        for i, row in enumerate(r, start=2):
            row_dict = dict(zip(headers, row))
            try:
                holding = dict(zip(['name','shares','price'],(row_dict['name'], int(row_dict['shares']), float(row_dict['price']))))
                portfolio.append(holding)
            except ValueError:
                print(f"Error parsing line {i}")
    return portfolio

def read_prices(filename):
    lookup = {}
    with open(filename, 'rt') as f:
        r = csv.reader(f)
        for i, row in enumerate(r):
            try:
                if len(row) == 2:
                    lookup[row[0]] = float(row[1])
            except ValueError:
                print(f"Error parsing row {i}")
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
            'original_price': price,
            'current_price': cur_price,
            'original_value': orig_value,
            'current_value': cur_value,
            'gain': cur_value - orig_value # negatives are losses
            })
    return cur_portfolio

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

def file_to_dict(filename: str, select=None, converters={}, headers=None) -> dict:
    """Reads a CSV file and returns a list of dictionary items representing each row. The first row of the CSV file will be read as a list of
    column headers which will be used as the keys in all dictionary items.  By default, all fields will be returned as strings. You can
    provide a `converters` argument as a dictionary from header name to conversion function.  """
    with open(filename, 'rt') as f:
        r = csv.reader(f)
        headers = next(r) if headers is None else headers
        select = headers if select is None else select
        return [
            {
                header: converters.get(header, str)(value)
                for header, value in zip(headers, row)
                if header in select
            }
            for row in r
        ]

dow_converters = { h: float for h in ['price', 'open', 'low', 'high', 'change'] } | { h: int for h in ['volume', 'shares'] }
    
