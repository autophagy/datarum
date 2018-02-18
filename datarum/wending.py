# -*- coding: utf-8 -*-

from datetime import datetime, date, time
from .converter import from_date
from parse import parse


class wending(object):

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

    def __new__(self, gere, mónþ, dæg,
                tid=0, minute=0, second=0, millisecond=0):
        self = object.__new__(self)

        if gere < 0:
            raise ValueError("Gere must not be less than zero.")
        elif mónþ < 0 or mónþ > 13:
            raise ValueError("{} is an invalid mónþ.")
        elif dæg < 0:
            raise ValueError("Dæg must not be less than zero.")
        elif dæg > 30:
            raise ValueError("Dæg cannot be greater than 30.")
        elif (mónþ == 13 and dæg > 6):
            raise ValueError("Dæg cannot be greater than 6 for a Wending day.")

        self.time = time(tid, minute, second, millisecond)
        self.gere = gere
        self.mónþ = mónþ
        self.dæg = dæg
        return self

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

        return(format_string.format(daeg_zero=zero_pad(self.dæg),
                                    daeg=self.dæg,
                                    month=self._mónþas[self.mónþ-1],
                                    gere=self.gere,
                                    tid_zero=zero_pad(self.time.hour),
                                    tid=self.time.hour,
                                    minute_zero=zero_pad(self.time.minute),
                                    minute=self.time.minute,
                                    second_zero=zero_pad(self.time.second),
                                    second=self.time.second))

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


    @classmethod
    def now(cls):
        return from_date(datetime.now())

    def tuple(self):
        return (self.gere, self.mónþ, self.dæg)

    def __str__(self):
        return '{0}.{1}.{2} {3}'.format(self.gere, self.mónþ, self.dæg,
                                        self.time)

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

    def _compare(self, other):
        a = (self.gere, self.mónþ, self.dæg, self.time)
        b = (other.gere, other.mónþ, other.dæg, other.time)
        return 0 if a == b else 1 if a > b else -1
