from whitefield.schedule import DaySchedule


def json_schedule(date_string):
    schedule = DaySchedule(date_string)

    return {
        'date': schedule.date,
        'day': schedule.day,
        'school': schedule.school,
        'day_code': schedule.day_code,
        'modifier': schedule.modifier,
        'day_type': schedule.day_type,
        'periods': schedule.periods,
        'schedule': schedule.schedule,
    }
