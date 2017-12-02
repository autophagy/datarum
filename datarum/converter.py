# -*- coding: utf-8 -*-

from datetime import datetime, date, timedelta
from . import wending


# Revolutionary calendar starts on 22nd September 1792
incept = datetime(1792, 9, 21)
DAYS_IN_YEAR = 365


def from_date(date):
    if type(date) is not datetime:
        raise ValueError('Supplied date must be of type datetime.')

    if date < incept:
        raise ValueError('The calendar begins at 1792-09-22. '
                         'You cannot convert a date earlier than this.')

    # Remove the time from the timestamp
    date = datetime.combine(date, datetime.min.time())
    diff = date.timestamp() - incept.timestamp()
    return to_wending(int(round(diff / (24*60*60))))


def to_wending(total_days):
    dat = wending.wending(1, 1, 0)
    bises = False

    day_count = 1

    while (day_count <= total_days):
        dat.dæg += 1

        if (dat.dæg > 30):
            dat.dæg = 1
            dat.mónþ += 1

        if dat.mónþ == 13:
            if romme_bises(dat.gere):
                if dat.dæg > 6:
                    dat.dæg = 1
                    dat.mónþ = 1
                    dat.gere += 1
            else:
                if dat.dæg > 5:
                    dat.dæg = 1
                    dat.mónþ = 1
                    dat.gere += 1

        day_count += 1

    return dat


def to_gregorian(wending_date):
    if not isinstance(wending_date, wending.wending):
        raise ValueError('Supplied date must be of type wending.')

    return incept + timedelta(days=days_since_incept(wending_date) + 1)


def days_since_incept(wending_date):
    year_days = 0

    for i in range(1, wending_date.gere):
        if romme_bises(i):
            year_days += DAYS_IN_YEAR + 1
        else:
            year_days += DAYS_IN_YEAR

    month_days = (wending_date.mónþ-1) * 30

    return year_days + month_days + (wending_date.dæg-1)


def romme_bises(gere):
    if gere in [3, 7, 11]:
        return True
    elif gere < 15:
        return False

    return (gere % 4 == 0 and gere % 100 != 0) or gere % 400 == 0
