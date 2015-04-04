from whitefield.schedule import DaySchedule
from whitefield.schedule.data import available_for_sign_up


def json_schedule(date_string, school=None):
    schedule = DaySchedule(date_string, school=school)

    return {
        'date': schedule.date,
        'day': schedule.day,
        'school': schedule.school,
        'day_code': schedule.day_code,
        'modifier': schedule.modifier,
        'day_type': schedule.day_type,
        'day_before': schedule.day_before,
        'day_after': schedule.day_after,
        'periods': schedule.periods,
        'schedule': schedule.schedule,
        'available_for_sign_up': available_for_sign_up,
    }
