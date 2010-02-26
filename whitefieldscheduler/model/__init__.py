# coding=utf-8

"""
.py
==================



© 2008 Daniel J. Rocco
Licensed under the Creative Commons Attribution-Noncommercial-Share Alike 3.0 United States License
http://creativecommons.org/licenses/by-nc-sa/3.0/us/


For a given day code, the order of class periods is given in day_period, 
so we can find the class period order with

>>> day_periods[day_code[parse_date("8/21/2009")][0]]
[1, 5, 6, 7, 2, 3]
>>> day_periods[day_code[parse_date("8/28/2009")][0]]
[2, 3, 4, 5, 6, 7]

The modifier tells us the schedule for the day: 

>>> schedule[day_code[parse_date("9/1/2009")][1]][0]
('7:45-8:10', 'Extra Help')
>>> schedule[day_code[parse_date("8/31/2009")][1]][2]
('8:30-9:25', 0)

Higher-level access is provided using the DaySchedule class; we use
flexible date parsing to read "friendly" date strings

>>> DaySchedule("8/20/2009").schedule == DaySchedule("August 20, 2009").schedule
True
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
    """
    date_struct, parse_code = _date_parser.parse(_date)

    if parse_code == 0:
        raise ValueError("Couldn't parse the date from: " + _date)

    return date(*(date_struct[:3]))

days = "Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split()

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
    # 
}

# convert day code dates to date objects
day_code = dict(zip(map(parse_date, day_code.keys()), day_code.values()))

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
         ("8:30-9:25", 0),
         ("9:30-10:25", 1),
         ("10:30-11:25", 2),
         ("11:30-12:25", 3),
         ("12:30-1:00", "Lunch"),
         ("1:05-2:00", 4),
         ("2:05-3:00", 5),
         ],
    "Late": [("8:45-9:10", "Extra Help"), 
         ("9:10-9:25", "Advisee"),
         ("9:30-10:15", 0),
         ("10:20-11:05", 1),
         ("11:10-11:55", 2),
         ("12:00-12:45", 3),
         ("12:50-1:20", "Lunch"),
         ("1:25-2:10", 4),
         ("2:15-3:00", 5),
         ],
    "Chapel": [("7:45-8:10", "Extra Help"), 
         ("8:10-8:55", 0),
         ("9:00-10:15", "Chapel/Advisee"),
         ("10:20-11:05", 1),
         ("11:10-11:55", 2),
         ("12:00-12:45", 3),
         ("12:50-1:20", "Lunch"),
         ("1:25-2:10", 4),
         ("2:15-3:00", 5),
         ],
}

class DaySchedule(object):
    """The schedule for a given day.

    >>> schedule = DaySchedule("8/31/2009")
    >>> schedule.day
    'Monday'
    >>> schedule.day_code
    'A'

    To get the entire schedule, use the schedule property
    
    >>> schedule.schedule[1]
    ('8:10-8:25', 'Advisee')

    To find the time of a particular period
    
    >>> schedule['3']
    '10:30-11:25'
    >>> schedule['Lunch']
    '12:30-1:00'
    """
    def __init__(self, _date):
        self.date = parse_date(_date)
        self.day_code, self.modifier = day_code[self.date]
        self.periods = day_periods[self.day_code]
        self._schedule = schedule[self.modifier]
        self.day = days[self.date.weekday()]
        self.period_times = {}

    @property
    def schedule(self):
         return map(self._label, self._schedule)

    def _label(self, period):
        if isinstance(period[1], int):
            period = (period[0], str(self.periods[period[1]]))

        self.period_times[period[1]] = period[0]
        return period

    def __str__(self):
        return str({
            "date": str(self.date),
            "day_code": self.day_code,
            "day": self.day,
            "schedule": self.schedule,
            })

    def __getitem__(self, key):
        return self.period_times[key]

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

    print DaySchedule("8/19/2009")
    print
    print DaySchedule("August 20, 2009")
    print
    print DaySchedule("8/21/2009")
