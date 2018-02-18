import datarum
import unittest
import datetime


class TestConversionExceptions(unittest.TestCase):

    def test_from_gregorian_null(self):
        with self.assertRaises(ValueError):
            d1 = datarum.from_date(None)

    def test_from_before_inception(self):
        dt = datetime.datetime(1500, 1, 1)

        with self.assertRaises(ValueError):
            d1 = datarum.from_date(dt)

    def test_to_gregorian_null(self):
        with self.assertRaises(ValueError):
            d1 = datarum.to_gregorian(None)


class TestWendingExceptions(unittest.TestCase):

    def test_invalid_from_string(self):
        with self.assertRaises(ValueError):
            w1 = datarum.wending.strptime("Hello World", "{daeg} {month}")

        with self.assertRaises(ValueError):
            w1 = datarum.wending.strptime("21 Bompo 221",
                                          "{daeg} {month} {gere}")

        with self.assertRaises(ValueError):
            w1 = datarum.wending.strptime("300 Forst 226",
                                          "{daeg} {month} {gere}")

    def test_invalid_dates(self):
        with self.assertRaises(ValueError):
            w1 = datarum.wending(-10, 1, 226)

        with self.assertRaises(ValueError):
            w1 = datarum.wending(10, -201, 226)

        with self.assertRaises(ValueError):
            w1 = datarum.wending(10, 1, -10226)

        with self.assertRaises(ValueError):
            w1 = datarum.wending(300, 3, 226)

        with self.assertRaises(ValueError):
            w1 = datarum.wending(10, 1000, 226)
