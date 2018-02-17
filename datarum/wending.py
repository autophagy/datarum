# -*- coding: utf-8 -*-

from datetime import datetime, date, time
from .converter import from_date


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
    # easy_month  :: Mónþ without any special characters
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
                                    easy_month=self._easy_mónþas[self.mónþ-1],
                                    gere=self.gere,
                                    tid_zero=zero_pad(self.time.hour),
                                    tid=self.time.hour,
                                    minute_zero=zero_pad(self.time.minute),
                                    minute=self.time.minute,
                                    second_zero=zero_pad(self.time.second),
                                    second=self.time.second))

    @classmethod
    def now(cls):
        return from_date(datetime.now())

    @classmethod
    def from_date_string(cls, date_string):
        try:
            d, m, g = date_string.split()
        except ValueError:
            raise ValueError("{} is not a valid date string"
                             .format(date_string))

        if m.lower() in cls._easy_mónþas:
            mónþas_index = cls._easy_mónþas.index(m.lower()) + 1
        else:
            raise ValueError("{} is not a valid mónþ.".format(m))

        return cls(int(g), cls._easy_mónþas.index(m.lower()) + 1, int(d))

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
        a = (self.gere, self.mónþ, self.dæg)
        b = (other.gere, other.mónþ, other.dæg)
        return 0 if a == b else 1 if a > b else -1
