from datetime import timedelta, date
from parsedatetime.parsedatetime import Calendar

ONE_DAY = timedelta(days=1)
_calendar = Calendar()


def parse_date(date_string):
    date_struct, parse_code = _calendar.parse(date_string)

    if parse_code == 0:
        raise ValueError("Couldn't parse the date from: " + date_string)

    return date(*(date_struct[:3]))


from .model import DaySchedule
