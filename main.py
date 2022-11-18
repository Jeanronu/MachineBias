""""
This function print a table with the results on the analyze_data file

>>> print_table()
╒══════════════════════════════════════╤═════════╤════════════════════╕
│                                      │ White   │ African-American   │
╞══════════════════════════════════════╪═════════╪════════════════════╡
│ Label High risk but didn't re-offend │ 23.5%   │ 44.8%              │
├──────────────────────────────────────┼─────────┼────────────────────┤
│ Label Low risk but re-offend         │ 47.7%   │ 28.0%              │
╘══════════════════════════════════════╧═════════╧════════════════════╛

"""""

from tabulate import *
from analyze_data import defendants_percent


def print_table():
    data = [["Label High risk but didn't re-offend", defendants_percent("w", "n", "High"),
             defendants_percent("b", "n", "High")],
            ["Label Low risk but re-offend", defendants_percent("w", "y", "Low"), defendants_percent("b", "y", "Low")]]

    Header = ["", "White", "African-American"]  # the first empty one is to put the two rows name

    print(tabulate(data, headers=Header, tablefmt="fancy_grid"))
