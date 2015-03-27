from datetime import timedelta, date
from parsedatetime import Constants
from parsedatetime.parsedatetime import Calendar


ONE_DAY = timedelta(days=1)
_calendar = Calendar(Constants())


def parse_date(date_string):
    # bizarre omission: parsedatetime doesn't handle the default string
    # format returned by datetime.date objects!  Special case…
    try:
        year, month, day = map(int, date_string.split("-"))
        return date(year,  month,  day)
    except:
         pass

    date_struct, parse_code = _calendar.parse(date_string)

    if parse_code == 0:
        raise ValueError("Couldn't parse the date from: " + date_string)

    return date(*(date_struct[:3]))


from .model import DaySchedule
