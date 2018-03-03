from datarum import wending
from datetime import timedelta, datetime
import unittest


class TestWendingOperations(unittest.TestCase):

    expected = [
    ((226, 3, 6, 3, 44, 0),    (226, 3, 6, 3, 10, 0),    (0, 2040)),
    ((226, 1, 1, 0, 0, 0),     (230, 1, 1, 1, 10, 0),    (-1462, 82200)),
    ((230, 1, 1, 1, 10, 0),    (226, 1, 1, 0, 0, 0),     (1461, 4200)),
    ((224, 13, 6, 10, 10, 10), (225, 1, 1, 10, 10, 10),  (-1, 0)),
    ((225, 1, 1, 10, 10, 10),  (224, 13, 6, 10, 10, 10), (1, 0)),
    ]

    def test_wending_subtraction(self):
        for w1_tuple, w2_tuple, expected_td in self.expected:
            w1 = wending(*w1_tuple)
            w2 = wending(*w2_tuple)
            self.assertEqual(timedelta(*expected_td), w1-w2)

    def test_wending_addition(self):
        for expected_wending, w1_tuple, td_tuple in self.expected:
            w1 = wending(*w1_tuple)
            td = timedelta(*td_tuple)
            self.assertEqual(wending(*expected_wending), w1+td)


class TestWendingDateFeatures(unittest.TestCase):

    expected_weekdays = [
    ((230, 8,  11),  5),
    ((176, 4,  5),   1),
    ((224, 13, 6),   2),
    ((225, 1,  1),   3),
    ((225, 13, 5),   3),
    ((226, 1,  1),   4)
    ]

    def test_today_weekday(self):
        w_now = wending.now()
        d_now = datetime.now()
        self.assertEqual(w_now.weekday(), d_now.weekday())

    def test_wending_weekdays(self):
        for w_tuple, expected_weekday in self.expected_weekdays:
            w = wending(*w_tuple)
            self.assertEqual(w.weekday(), expected_weekday)
            self.assertEqual(w.todatetime().weekday(), expected_weekday)
