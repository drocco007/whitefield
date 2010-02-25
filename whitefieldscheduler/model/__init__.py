# coding=utf-8

"""
.py
==================



© 2008 Daniel J. Rocco
Licensed under the Creative Commons Attribution-Noncommercial-Share Alike 3.0 United States License
http://creativecommons.org/licenses/by-nc-sa/3.0/us/


For a given day code, the order of class periods is given here, so we 
can  find the class period order with

>>> day_periods[day_code["8/21/2009"][0]]
[1, 5, 6, 7, 2, 3]
"""

"""
Encode a string date to a (date code, modifier) pair, either of which
may be empty.
"""
day_code = {
    "8/18/2009": ("A", "Late"),
    "8/19/2009": ("B", "Late"),
    "8/20/2009": ("C", "Chapel"),
    "8/21/2009": ("D", ""),
    "8/24/2009": ("", "Trip"),
    "8/25/2009": ("", "Trip"),
    "8/26/2009": ("E", "Late"),
    "8/27/2009": ("F", "Chapel"),
    "8/28/2009": ("G", "Pep"),
    "8/31/2009": ("A", ""),
    "9/1/2009": ("B", ""),
    # …
}

"""
Define the periods for a given day code. 
"""
day_periods = {
    "A": [1, 2, 3, 4, 5, 6],
    "B": [1, 7, 2, 3, 4, 5],
    "C": [1, 6, 7, 2, 3, 4],
    "D": [1, 5, 6, 7, 2, 3],
    "E": [1, 4, 5, 6, 7, 2],
    "F": [1, 3, 4, 5, 6, 7],
    "G": [2, 3, 4, 5, 6, 7],
}


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
    _test(True)


