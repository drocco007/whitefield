from whitefield.schedule import parse_date

import pytest


def test_month_day_slashes():
    assert '2009-09-01' == str(parse_date("9/1/2009"))


def test_parse_human_date():
    assert '2010-02-26' == str(parse_date("February 26, 2010"))


def test_parse_invalid():
    with pytest.raises(ValueError):
        parse_date("python rocks!")


def test_parse_date_str_format():
    assert '2009-08-31' == str(parse_date("2009-08-31"))
