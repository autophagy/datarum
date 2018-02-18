from datarum import wending
import unittest


class TestWendingComparison(unittest.TestCase):

    def test_unequal(self):
        w1 = wending(226, 3, 14, 12, 5, 4)
        w2 = wending(234, 5, 23, 11, 32, 45)

        self.assertTrue(w1 != w2)
        self.assertFalse(w1 == w2)

    def test_equal(self):
        w1 = wending(226, 3, 14, 3, 44, 21)
        w2 = wending(226, 3, 14, 3, 44, 21)

        self.assertTrue(w1 == w2)
        self.assertFalse(w1 != w2)

    def test_greater_than_date(self):
        w1 = wending(226, 3, 14)
        w2 = wending(213, 5, 23)

        self.assertTrue(w1 > w2)
        self.assertFalse(w1 < w2)

    def test_greater_than_time(self):
        w1 = wending(226, 3, 14, 13, 54, 12)
        w2 = wending(226, 3, 14, 12, 54, 12)

        self.assertTrue(w1 > w2)
        self.assertFalse(w1 < w2)

        w1 = wending(226, 3, 14, 12, 55, 12)
        w2 = wending(226, 3, 14, 12, 54, 12)

        self.assertTrue(w1 > w2)
        self.assertFalse(w1 < w2)

        w1 = wending(226, 3, 14, 12, 54, 13)
        w2 = wending(226, 3, 14, 12, 54, 12)

        self.assertTrue(w1 > w2)
        self.assertFalse(w1 < w2)

    def test_less_than_date(self):
        w1 = wending(226, 3, 14)
        w2 = wending(213, 5, 23)

        self.assertTrue(w2 < w1)
        self.assertFalse(w2 > w1)

    def test_less_than_time(self):
        w1 = wending(226, 3, 14, 11, 54, 12)
        w2 = wending(226, 3, 14, 12, 54, 12)

        self.assertTrue(w1 < w2)
        self.assertFalse(w1 > w2)

        w1 = wending(226, 3, 14, 12, 53, 12)
        w2 = wending(226, 3, 14, 12, 54, 12)

        self.assertTrue(w1 < w2)
        self.assertFalse(w1 > w2)

        w1 = wending(226, 3, 14, 12, 54, 11)
        w2 = wending(226, 3, 14, 12, 54, 12)

        self.assertTrue(w1 < w2)
        self.assertFalse(w1 > w2)
