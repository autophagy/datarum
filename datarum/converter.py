# -*- coding: utf-8 -*-

from datetime import datetime, date, timedelta
from . import wending


# Revolutionary calendar starts on 22nd September 1792
incept = datetime(1792, 9, 21, 0, 0, 0)
incept_ts = -5594316808.0
DAYS_IN_YEAR = 365


def from_date(date):
    if type(date) is not datetime:
        raise ValueError('Supplied date must be of type datetime.')

    if date < incept:
        raise ValueError('The calendar begins at 1792-09-22. '
                         'You cannot convert a date earlier than this.')

    # Remove the time from the timestamp
    date_sans_time = datetime.combine(date, datetime.min.time())
    diff = date_sans_time.timestamp() - incept_ts
    w = to_wending_from_ordinal(int(round(diff / (24*60*60))))
    return w.replace(hour=date.hour, minute=date.minute, second=date.second,
                     microsecond=date.microsecond)


# We are using the 4/100/400 leap year rule for Wending dates.
# This means that every year divisible by 4 is a leap year, *except*
# if it's divisible by 100 too. Exceptions to these are divisible by 400.

# So, we essentially have 3 unique cycles in terms of days within a cycle
# that cannot be calculated by multipling num_of_years * 365.

# We have the number of days in every 4 year cycle:
_days_in_4g_cycle = 4 * DAYS_IN_YEAR + 1

# We also have days within a 100 year cycle, where a leap day is removed.
_days_in_100g_cycle = 25 * _days_in_4g_cycle - 1

# Finally, days within a 400 year cycle, where a leap is added back in.
_days_in_400g_cycle = 4 * _days_in_100g_cycle + 1

def to_wending_from_ordinal(total_days):
    total_days -= 1

    # First, calculate the number of 400 year cycles that proceed total_days.
    g400, total_days = divmod(total_days, _days_in_400g_cycle)
    gere = g400 * 400 + 1

    # Now, calc the number of preceeding 100 year cycles.
    g100, total_days = divmod(total_days, _days_in_100g_cycle)

    # Now, preceeding 4 year cycles, and the remaining single years.
    g4, total_days = divmod(total_days, _days_in_4g_cycle)
    g1, total_days = divmod(total_days, DAYS_IN_YEAR)

    gere += g100*100 + g4*4 + g1
    if g1 == 4 or g100 == 4:
        assert total_days == 0
        return wending.wending(gere-1, 13, 6)

    # Now we have the correct gere, total_days is the offset from 1 Hærfest.
    mónþ, total_days = divmod(total_days, 30)

    return wending.wending(gere, mónþ+1, total_days+1)


def to_gregorian(wending_date):
    if not isinstance(wending_date, wending.wending):
        raise ValueError('Supplied date must be of type wending.')

    dt = datetime(1,1,1,0,0,0)
    wending_time = datetime.combine(dt, wending_date.time())
    incept_time = datetime.combine(dt, incept.time())
    td = wending_time - incept_time

    return incept + td + timedelta(days=days_since_incept(wending_date))


def days_since_incept(wending_date):
    y = wending_date.year - 1
    year_days = y*DAYS_IN_YEAR + y//4 - y//100 + y//400
    month_days = (wending_date.month-1) * 30
    return year_days + month_days + (wending_date.day)


def romme_bises(gere):
    return (gere % 4 == 0 and gere % 100 != 0) or gere % 400 == 0
