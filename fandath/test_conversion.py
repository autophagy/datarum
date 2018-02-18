from datarum import from_date, to_gregorian, wending
import unittest
from datetime import datetime


year_starts = [
    ((10, 1, 1, 16, 45, 10), (1801, 9, 23, 16, 45, 10)),
    ((11, 1, 1, 16, 45, 10), (1802, 9, 23, 16, 45, 10)),
    ((12, 1, 1, 16, 45, 10), (1803, 9, 24, 16, 45, 10)),
    ((13, 1, 1, 16, 45, 10), (1804, 9, 23, 16, 45, 10)),
    ((14, 1, 1, 16, 45, 10), (1805, 9, 23, 16, 45, 10)),
    ((223, 1, 1, 16, 45, 10), (2014, 9, 22, 16, 45, 10)),
    ((224, 1, 1, 16, 45, 10), (2015, 9, 22, 16, 45, 10)),
    ((225, 1, 1, 16, 45, 10), (2016, 9, 22, 16, 45, 10)),
    ((226, 1, 1, 16, 45, 10), (2017, 9, 22, 16, 45, 10)),
    ((227, 1, 1, 16, 45, 10), (2018, 9, 22, 16, 45, 10)),
    ((228, 1, 1, 16, 45, 10), (2019, 9, 22, 16, 45, 10)),
]

leaps = [
    ((3, 13, 6, 16, 45, 10), (1795, 9, 22, 16, 45, 10)),
    ((7, 13, 6, 16, 45, 10), (1799, 9, 22, 16, 45, 10)),
    ((11, 13, 6, 16, 45, 10), (1803, 9, 23, 16, 45, 10)),
]

romme = [
    ((221, 13, 5, 16, 45, 10), (2013, 9, 21, 16, 45, 10)),
    ((222, 13, 5, 16, 45, 10), (2014, 9, 21, 16, 45, 10)),
    ((224, 13, 6, 16, 45, 10), (2016, 9, 21, 16, 45, 10)),
    ((225, 13, 5, 16, 45, 10), (2017, 9, 21, 16, 45, 10)),
    ((226, 13, 5, 16, 45, 10), (2018, 9, 21, 16, 45, 10)),
    ((227, 13, 5, 16, 45, 10), (2019, 9, 21, 16, 45, 10)),
    ((228, 13, 6, 16, 45, 10), (2020, 9, 21, 16, 45, 10)),
    ((229, 13, 5, 16, 45, 10), (2021, 9, 21, 16, 45, 10)),
    ((230, 13, 5, 16, 45, 10), (2022, 9, 21, 16, 45, 10)),
]


class TestWendingConversion(unittest.TestCase):

    def test_year_starts(self):
        for dat, gregorian in year_starts:
            gregorian_date = datetime(*gregorian)
            c = from_date(gregorian_date)
            self.assertEqual(dat, c.tuple())

    def test_leaps(self):
        for dat, gregorian in leaps:
            gregorian_date = datetime(*gregorian)
            c = from_date(gregorian_date)
            self.assertEqual(dat, c.tuple())

    def test_romme_leaps(self):
        for dat, gregorian in romme:
            gregorian_date = datetime(*gregorian)
            c = from_date(gregorian_date)
            self.assertEqual(dat, c.tuple())


class TestGregorianConversion(unittest.TestCase):

    def test_year_starts(self):
        for dat, gregorian in year_starts:
            wending_date = wending(*dat)
            g = to_gregorian(wending_date)
            self.assertEqual(gregorian, (g.year, g.month, g.day, g.hour,
                                         g.minute, g.second))

    def test_leaps(self):
        for dat, gregorian in leaps:
            wending_date = wending(*dat)
            g = to_gregorian(wending_date)
            self.assertEqual(gregorian, (g.year, g.month, g.day, g.hour,
                                         g.minute, g.second))

    def test_romme_leaps(self):
        for dat, gregorian in romme:
            wending_date = wending(*dat)
            g = to_gregorian(wending_date)
            self.assertEqual(gregorian, (g.year, g.month, g.day, g.hour,
                                         g.minute, g.second))
