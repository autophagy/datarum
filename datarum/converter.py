# -*- coding: utf-8 -*-

from datetime import datetime, date, timedelta
from . import wending


# Revolutionary calendar starts on 22nd September 1792
incept = datetime(1792, 9, 21, 0, 0, 0)
DAYS_IN_YEAR = 365


def from_date(date):
    if type(date) is not datetime:
        raise ValueError('Supplied date must be of type datetime.')

    if date < incept:
        raise ValueError('The calendar begins at 1792-09-22. '
                         'You cannot convert a date earlier than this.')

    # Remove the time from the timestamp
    date_sans_time = datetime.combine(date, datetime.min.time())
    diff = date_sans_time.timestamp() - incept.timestamp()
    return to_wending(int(round(diff / (24*60*60))), date.time())


def to_wending(total_days, wending_time=None):
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

    if wending_time:
        dat.time = wending_time

    return dat


def to_gregorian(wending_date):
    if not isinstance(wending_date, wending.wending):
        raise ValueError('Supplied date must be of type wending.')

    dt = datetime(1,1,1,0,0,0)
    wending_time = datetime.combine(dt, wending_date.time)
    incept_time = datetime.combine(dt, incept.time())
    td = wending_time - incept_time

    return incept + td + timedelta(days=days_since_incept(wending_date) + 1)


def days_since_incept(wending_date):
    y = wending_date.gere - 1
    year_days = y*DAYS_IN_YEAR + y//4 - y//100 + y//400
    month_days = (wending_date.mónþ-1) * 30
    return year_days + month_days + (wending_date.dæg-1)


def romme_bises(gere):
    return (gere % 4 == 0 and gere % 100 != 0) or gere % 400 == 0
