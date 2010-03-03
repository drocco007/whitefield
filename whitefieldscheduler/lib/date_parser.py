# coding=utf-8

"""
date_parser.py
==================

Wrapper utility for the parsedatetime library that allows arbitrary string
dates to be parsed to python date objects.

© 2008 Daniel J. Rocco
Licensed under the Creative Commons Attribution-Noncommercial-Share Alike 3.0 United States License
http://creativecommons.org/licenses/by-nc-sa/3.0/us/

"""

from datetime import date

from parsedatetime.parsedatetime import Calendar
from parsedatetime.parsedatetime_consts import Constants as CalendarConstants


_date_parser = Calendar(CalendarConstants())

def parse_date(_date):
    """Parse a date string to a date object.

    >>> str(parse_date("9/1/2009"))
    '2009-09-01'
    >>> str(parse_date("February 26, 2010"))
    '2010-02-26'
    >>> str(parse_date("python rocks!"))
    Traceback (most recent call last):
    ...
    ValueError: Couldn't parse the date from: python rocks!
    >>> str(parse_date("2009-08-31"))
    '2009-08-31'
    """
    # bizarre omission: parsedatetime doesn't handle the default string
    # format returned by datetime.date objects!  Special case…
    try:
        year, month, day = map(int, _date.split("-"))
        return date(year,  month,  day)
    except:
         pass

    date_struct, parse_code = _date_parser.parse(_date)

    if parse_code == 0:
        raise ValueError("Couldn't parse the date from: " + _date)

    return date(*(date_struct[:3]))

# ====================================================================
# doctest test harness

def _test(_verbose=False):
    import doctest
    doctest.testmod(verbose=_verbose, optionflags=(doctest.ELLIPSIS |
                                            doctest.REPORT_NDIFF |
                                            doctest.NORMALIZE_WHITESPACE))

# ====================================================================
# test stub: run doctests if this file is run directly

if __name__ == "__main__":
    _test()

