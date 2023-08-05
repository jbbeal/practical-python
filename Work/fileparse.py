# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(lines, select=None, converters={}, headers=None, silence_errors=False) -> dict:
    """Reads lines of CSV data and returns a list of dictionary items representing each row. The first row of the CSV file will be read as a
    list of column headers which will be used as the keys in all dictionary items.  By default, all fields will be returned as strings. You
    can provide a `converters` argument as a dictionary from header name to conversion function.

    """
    r = csv.reader(lines)
    headers = next(r) if headers is None else headers
    select = headers if select is None else select
    rows_as_dict = []
    for row in r:
        if (row == []):
            continue
        try:
            rows_as_dict.append(
                {
                    header: converters.get(header, str)(value)
                    for header, value in zip(headers, row)
                    if header in select
                }
            )
        except ValueError as e:
            if not silence_errors:
                print(f"Couldn't convert {row} because {e}")
    return rows_as_dict

