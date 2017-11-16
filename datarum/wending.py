import datetime


class wending(object):

    mónþas = [
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
        return '{0} {1} {2}'.format(self.dæg, self.mónþas[self.mónþ-1], self.gere)

    def tuple(self):
        return (self.gere, self.mónþ, self.dæg)

    def __str__(self):
        return '{0}-{1}-{2}'.format(self.gere, self.mónþ, self.dæg)