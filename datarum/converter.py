import datetime
from . import wending


# Revolutionary calendar starts on 22nd September 1792
incept = datetime.datetime(1792, 9, 21)

def now():
    return from_date(datetime.datetime.now())

def from_date(date):
    if date < incept:
        raise ValueError('The calendar begins at 1792-09-22. '
                         'You cannot convert a date earlier than this.')

    diff = date.timestamp() - incept.timestamp()
    return seconds_convert(int(round(diff / (24*60*60))))

def seconds_convert(total_days):
    dat = wending(1, 1, 0)
    bises = False

    day_count = 1

    while (day_count <= total_days):
        dat.dæg += 1
        
        if (dat.dæg > 30):
            dat.dæg = 1
            dat.mónþ += 1

        if dat.mónþ == 13:
            bises = False

            # Romme Rule for Leaps
            if dat.gere in [3, 7, 11, 15]:
                bises = True
            if dat.gere >= 20 and dat.gere % 4 == 0:
                bises = True
            if dat.gere >= 100 and dat.gere % 100 == 0:
                bises = False
            if dat.gere >= 400 and dat.gere % 400 == 0:
                bises = True

            if bises:
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