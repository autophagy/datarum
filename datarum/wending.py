import datetime


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

    def __init__(self, gere, mónþ, dæg):
        self.gere = gere
        self.mónþ = mónþ
        self.dæg = dæg

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
