# coding=utf-8

"""
schedule.py
==================

Provides higher-level access to the Whitefield schedule through the
DaySchedule class; we use flexible date parsing to read "friendly" date
strings

>>> DaySchedule("8/20/2009").schedule == DaySchedule("August 20, 2009").schedule
True


© 2008–2011 Daniel J. Rocco

Licensed under the Creative Commons Attribution-Noncommercial-Share
Alike 3.0 United States License

    http://creativecommons.org/licenses/by-nc-sa/3.0/us/

"""

from datetime import timedelta

from .data import day_code, day_periods, schedule, specials, lookup_day_code, \
    lookup_schedule
from . import parse_date, ONE_DAY


class DaySchedule(object):
    """The schedule for a given day.

    >>> schedule = DaySchedule("8/31/2009")
    >>> schedule.day
    'Monday'
    >>> schedule.day_code
    'A'
    >>> schedule.day_type
    'A'


    To get the entire schedule, use the schedule property

    >>> schedule.schedule[1]
    ('8:10-8:25', 'Advisee')


    To find the time of a particular period

    >>> schedule['3']
    '10:30-11:25'
    >>> schedule['Lunch']
    '12:30-1:00'


    You can also retrieve the day before or after this schedule's date

    >>> schedule.day_before
    datetime.date(2009, 8, 30)
    >>> schedule.day_after
    datetime.date(2009, 9, 1)
    """
    def __init__(self, _date, school='us'):
        self.date = parse_date(_date)
        self.period_times = {}
        self.school = school or 'us'
        self.day_code, self.modifier = lookup_day_code(self.date)
        self.periods, self.schedule = lookup_schedule(
            self.school, self.date, self.day_code, self.modifier)

        # FIXME: remove nasty stateful dependency in _label
        self.schedule = [self._label(period) for period in self.schedule]

    @property
    def date_str(self):
        return self.date.strftime("%A %B %%s, %Y") % str(self.date.day)

    @property
    def short_date_str(self):
        return self.date.strftime("%a %B %%s") % str(self.date.day)

    @property
    def day(self):
        return self.date.strftime("%A")

    @property
    def day_type(self):
        """Describes the day, e.g. "B", "Late G", "Arts", etc."""

        return " ".join((self.modifier, self.day_code)).strip()

    @property
    def day_before(self):
        """Return the date before this date."""

        return self.date - ONE_DAY

    @property
    def day_after(self):
        """Return the date after this date."""

        return self.date + ONE_DAY

    def _label(self, period):
        time, event = period

        try:
            event = str(self.periods[event])
        except TypeError:
            pass

        self.period_times[event] = time

        return time, event

    def __str__(self):
        if not self.day_type:
            return self.date_str

        return "-".join((self.date_str, self.day_type))

    def __getitem__(self, key):
        """Return the time slot for a given period.

        >>> schedule = DaySchedule("8/27/2009")
        >>> schedule['Lunch']
        '12:50-1:20'
        """

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

    ## print DaySchedule("8/19/2009")
    ## print
    ## print DaySchedule("August 20, 2009")
    ## print
    ## print DaySchedule("8/21/2009")
    ## print
    ## print DaySchedule("September 1, 2009")
    print(DaySchedule("8/27/2009"))
    print(DaySchedule("8/29/2009"))
    print(DaySchedule("4/30/2010"))
    print(DaySchedule("5/1/2010"))
    print(DaySchedule("5/2/2010"))
    print(DaySchedule("5/3/2010"))
    print(DaySchedule("5/21/2010"))
    print(DaySchedule("12/6/2010"))
    print(DaySchedule("12/6/2010").schedule)
    print(DaySchedule("12/7/2010"))
    print(DaySchedule("12/7/2010").schedule)

