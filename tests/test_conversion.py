from datarum import from_date
import unittest
from datetime import datetime


year_starts = [
    ((10, 1, 1), (1801, 9, 23)),
    ((11, 1, 1), (1802, 9, 23)),
    ((12, 1, 1), (1803, 9, 24)),
    ((13, 1, 1), (1804, 9, 23)),
    ((14, 1, 1), (1805, 9, 23)),
    ((223, 1, 1), (2014, 9, 22)),
    ((224, 1, 1), (2015, 9, 22)),
    ((225, 1, 1), (2016, 9, 22)),
    ((226, 1, 1), (2017, 9, 22)),
    ((227, 1, 1), (2018, 9, 22)),
    ((228, 1, 1), (2019, 9, 22)),
]

leaps = [
    ((3, 13, 6), (1795, 9, 22)),
    ((7, 13, 6), (1799, 9, 22)),
    ((11, 13, 6), (1803, 9, 23)),
]

romme = [
    ((221, 13, 5), (2013, 9, 21)),
    ((222, 13, 5), (2014, 9, 21)),
    ((224, 13, 6), (2016, 9, 21)),
    ((225, 13, 5), (2017, 9, 21)),
    ((226, 13, 5), (2018, 9, 21)),
    ((227, 13, 5), (2019, 9, 21)),
    ((228, 13, 6), (2020, 9, 21)),
    ((229, 13, 5), (2021, 9, 21)),
    ((230, 13, 5), (2022, 9, 21)),
]


class TestDatarumConversion(unittest.TestCase):

    def test_year_starts(self):
        for dat, gregorian in year_starts:
            gregorian_date = datetime(gregorian[0],
                                      gregorian[1],
                                      gregorian[2])
            c = from_date(gregorian_date)
            self.assertEqual(dat, c.tuple())

    def test_leaps(self):
        for dat, gregorian in leaps:
            gregorian_date = datetime(gregorian[0],
                                      gregorian[1],
                                      gregorian[2])
            c = from_date(gregorian_date)
            self.assertEqual(dat, c.tuple())

    def test_romme_leaps(self):
        for dat, gregorian in romme:
            gregorian_date = datetime(gregorian[0],
                                      gregorian[1],
                                      gregorian[2])
            c = from_date(gregorian_date)
            self.assertEqual(dat, c.tuple())