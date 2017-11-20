# -*- coding: utf-8 -*-

from datetime import datetime, date
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

    def __new__(self, gere, mónþ, dæg):
        self = object.__new__(self)
        self.gere = gere
        self.mónþ = mónþ
        self.dæg = dæg
        return self

    @classmethod
    def today(cls):
        today = datetime.combine(date.today(), datetime.min.time())
        return from_date(today)

    @classmethod
    def from_date_string(cls, date_string):
        dæg, mónþ, gere = date_string.split()
        return cls(int(gere), cls._easy_mónþas.index(mónþ.lower()) + 1, int(dæg))

    def formatted(self):
        return '{0} {1} {2}'.format(self.dæg,
                                    self._mónþas[self.mónþ-1],
                                    self.gere)

    def tuple(self):
        return (self.gere, self.mónþ, self.dæg)

    def __str__(self):
        return '{0}-{1}-{2}'.format(self.gere, self.mónþ, self.dæg)

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
