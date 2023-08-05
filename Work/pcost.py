# pcost.py
#
# Exercise 1.27

from report import read_portfolio

def portfolio_cost(portfolio_lines):
    portfolio = read_portfolio(portfolio_lines)
    return sum([ p['price'] * p['shares'] for p in portfolio])


if __name__ == '__main__':
    from sys import argv

    if len(argv) != 2:
        raise SystemExit(f'USAGE: {argv[0]} portfile')
    with open(argv[1], 'rt') as f:
        cost = portfolio_cost(f)
        print(f'Total cost: {cost}')
    
