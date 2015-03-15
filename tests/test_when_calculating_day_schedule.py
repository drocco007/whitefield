from datetime import date
import pytest

from whitefield.schedule import DaySchedule

@pytest.fixture
def schedule():
    return DaySchedule("8/31/2009")


def test_can_create_day_schedule(schedule):
    assert schedule


def test_day_schedule_defines_day(schedule):
    assert 'Monday' == schedule.day


def test_schedule_defines_day_code(schedule):
    assert 'A' == schedule.day_code


def test_schedule_defines_day_type(schedule):
    assert 'A' == schedule.day_type


def test_entire_schedule_included(schedule):
    assert ('8:10-8:25', 'Advisee') == schedule.schedule[1]


@pytest.mark.parametrize('period', [('3', '10:30-11:25'), ('Lunch', '12:30-1:00')])
def test_can_retrieve_time_for_period(schedule, period):
    name, time = period
    assert time == schedule[name]


def test_can_navigate_previous_day(schedule):
    assert date(2009, 8, 30) == schedule.day_before


def test_can_navigate_next_day(schedule):
    assert date(2009, 9, 1) == schedule.day_after
