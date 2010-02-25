# coding=utf-8

"""
.py
==================



© 2008 Daniel J. Rocco
Licensed under the Creative Commons Attribution-Noncommercial-Share Alike 3.0 United States License
http://creativecommons.org/licenses/by-nc-sa/3.0/us/


For a given day code, the order of class periods is given in day_period, 
so we can find the class period order with

>>> day_periods[day_code["8/21/2009"][0]]
[1, 5, 6, 7, 2, 3]
>>> day_periods[day_code["8/28/2009"][0]]
[2, 3, 4, 5, 6, 7]

The modifier tells us the schedule for the day: 

>>> schedule[day_code["9/1/2009"][1]][0]
('7:45-8:10', 'Extra Help')
>>> schedule[day_code["8/31/2009"][1]][2]
('8:30-9:25', 'Class')
"""

"""
Encode a string date to a (day code, modifier) pair, either of which
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

"""
Define the schedule for a given modifier. 
"""
schedule = {
    "": [("7:45-8:10", "Extra Help"), 
         ("8:10-8:25", "Advisee"),
         ("8:30-9:25", "Class"),
         ("9:30-10:25", "Class"),
         ("10:30-11:25", "Class"),
         ("11:30-12:25", "Class"),
         ("12:30-1:00", "Lunch"),
         ("1:05-2:00", "Class"),
         ("2:05-3:00", "Class"),
         ],
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


