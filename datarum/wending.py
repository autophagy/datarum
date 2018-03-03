# -*- coding: utf-8 -*-

from datetime import datetime, date, time, timedelta
from .converter import from_date, days_since_incept, to_wending_from_ordinal, romme_bises, to_gregorian
from parse import parse


class wending(object):

    MINYEAR = 0
    MAXYEAR = 9999

    _mónþas = [
        u'Hærfest',
        u'Mist',
        u'Forst',
        u'Snáw',
        u'Regn',
        u'Wind',
        u'Sǽd',
        u'Blóstm',
        u'Mǽdland',
        u'Ríp',
        u'Hát',
        u'Wæstm',
        u'Wending'
    ]

    _easy_mónþas = [
        u'haerfest',
        u'mist',
        u'forst',
        u'snaw',
        u'regn',
        u'wind',
        u'saed',
        u'blostm',
        u'maedland',
        u'rip',
        u'hat',
        u'waestm',
        u'wending'
    ]

    # // Constructors //

    def __new__(self, gere, mónþ, dæg,
                tid=0, minute=0, second=0, microsecond=0):
        self = object.__new__(self)

        if not self.MINYEAR <= gere <= self.MAXYEAR:
            raise ValueError("Gere must be in range {0}..{1}".format(self.MINYEAR, self.MAXYEAR), gere)
        if not 1 <= mónþ <= 13:
            raise ValueError("Mónþ must be in range 1..13", mónþ)
        if not 1 <= dæg <= 30:
            raise ValueError("Dæg must be in range 1..30", dæg)
        if mónþ == 13:
            max_days = 6 if romme_bises(gere) else 5
            if not 1 <= dæg <= max_days:
                raise ValueError("Dæg must be in range 1..{} for a Wending day".format(max_days), dæg)
        if not 0 <= tid <= 23:
            raise ValueError("Tid must be in range 0..23", tid)
        if not 0 <= minute <= 59:
            raise ValueError("Minute must be in range 0..59", minute)
        if not 0 <= second <= 59:
            raise ValueError("Second must be in range 0..59", second)
        if not 0 <= microsecond <= 999999:
            raise ValueError("Microsecond must be in range 0..999999")

        self._gere = gere
        self._mónþ = mónþ
        self._dæg = dæg
        self._tid = tid
        self._minute = minute
        self._second = second
        self._microsecond = microsecond
        return self

    # Returns the current datetime as Wending.
    @classmethod
    def now(cls):
        return from_date(datetime.now())

    # Returns a wending date from an ordinal (the number of days from the incept)
    @classmethod
    def fromordinal(cls, o):
        return to_wending_from_ordinal(o)

    # Return a wending date from a datetime.
    @classmethod
    def fromdatetime(cls, dt):
        return from_date(dt)

    # Accessor Properties

    @property
    def year(self):
        return self._gere

    @property
    def month(self):
        return self._mónþ

    @property
    def day(self):
        return self._dæg

    @property
    def hour(self):
        return self._tid

    @property
    def minute(self):
        return self._minute

    @property
    def second(self):
        return self._second

    @property
    def microsecond(self):
        return self._microsecond

    # daeg_zero   :: Dæg of Mónþ as zero padded number
    # daeg        :: Dæg of Mónþ as decimal number
    # month       :: Mónþ as formatted string
    # gere        :: Gere as decimal number
    # tid_zero    :: Hour as zero padded number
    # tid         :: Hour as decimal number
    # minute_zero :: minute as zero padded decimal
    # minute      :: minute as decimal number
    # second_zero :: second as zero padded decimal
    # second      :: second as decimal

    def strftime(self, format_string):
        def zero_pad(number):
            if number < 10:
                return '0{}'.format(number)
            else:
                return number

        return(format_string.format(daeg_zero=zero_pad(self._dæg),
                                    daeg=self._dæg,
                                    month=self._mónþas[self._mónþ-1],
                                    gere=self._gere,
                                    tid_zero=zero_pad(self._tid),
                                    tid=self._tid,
                                    minute_zero=zero_pad(self._minute),
                                    minute=self._minute,
                                    second_zero=zero_pad(self._second),
                                    second=self._second))

    @classmethod
    def strptime(cls, wending_string, format_string):
        def unzero(number):
            if number is not None and number[0] == '0':
                return number[1:]
            else:
                return number

        def get_mónþ(month_string):
            if month_string is None:
                return None
            if month_string.lower() in cls._easy_mónþas:
                return cls._easy_mónþas.index(month_string.lower()) + 1
            elif month_string in cls._mónþas:
                return cls._mónþas.index(month_string) + 1
            else:
                return None

        items = parse(format_string, wending_string).named

        daeg = unzero(items.get('daeg_zero', None)) or items.get('daeg', None)
        month = get_mónþ(items.get('month', None))
        gere = items.get('gere', None)
        tid = unzero(items.get('tid_zero', None)) or items.get('tid', None)
        minute = unzero(items.get('minute_zero', None)) or items.get('minute', None)
        second = unzero(items.get('second_zero', None)) or items.get('second', None)

        if daeg == None:  raise ValueError("No valid dæg found in wending string.")
        if month == None: raise ValueError("No valid mónþ found in wending string.")
        if gere == None:  raise ValueError("No valid gere found in wending string.")

        return cls(int(gere), month, int(daeg),
                   int(tid or 0), int(minute or 0), int(second or 0))

    def replace(self, year=None, month=None, day=None, hour=None, minute=None,
                second=None, microsecond=None):
        year = self.year if year is None else year
        month = self.month if month is None else month
        day = self.day if day is None else day
        hour = self.hour if hour is None else hour
        minute = self.minute if minute is None else minute
        second = self.second if second is None else second
        microsecond = self.microsecond if microsecond is None else microsecond
        return type(self)(year, month, day, hour, minute, second, microsecond)

    def tuple(self):
        return (self._gere, self._mónþ, self._dæg,
                self._tid, self._minute, self._second)

    def toordinal(self):
        return days_since_incept(self)

    def todatetime(self):
        return to_gregorian(self)

    def weekday(self):
        return (self.toordinal() + 4) % 7

    def time(self):
        return time(self._tid, self._minute, self._second, self._microsecond)

    def __repr__(self):
        rep_string = "{module}.{name}({tuple})"
        return rep_string.format(module=self.__class__.__module__,
                                 name=self.__class__.__qualname__,
                                 tuple=", ".join(list(map(str, self.tuple()))))

    def __str__(self):
        return '{0}.{1}.{2} {3}'.format(self._gere, self._mónþ, self._dæg,
                                        self.time())

    def __eq__(self, other):
        if isinstance(other, wending):
            return self._compare(other) == 0
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, wending):
            return self._compare(other) <= 0
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, wending):
            return self._compare(other) < 0
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, wending):
            return self._compare(other) >= 0
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, wending):
            return self._compare(other) > 0
        return NotImplemented

    def __add__(self, other):
        if not isinstance(other, timedelta):
            return NotImplemented

        delta = timedelta(self.toordinal(),
                          hours=self._tid,
                          minutes=self._minute,
                          seconds=self._second)

        delta += other
        h, r = divmod(delta.seconds, 3600)
        m, s = divmod(r, 60)

        if delta.days > 0:
            return to_wending_from_ordinal(delta.days).replace(hour=h,
                                                               minute=m,
                                                               second=s)
        else:
            raise OverflowError("Result out of range.")

    __radd__ = __add__

    def __sub__(self, other):
        if not isinstance(other, wending):
            if isinstance(other, timedelta):
                return self + -other
            return NotImplemented
        return timedelta(days=self.toordinal()-other.toordinal(),
                         hours=self._tid - other.hour,
                         minutes=self._minute - other.minute,
                         seconds=self._second - other.second)

    def _compare(self, other):
        a = (self._gere, self._mónþ, self._dæg, self.time())
        b = (other.year, other.month, other.day, other.time())
        return 0 if a == b else 1 if a > b else -1
