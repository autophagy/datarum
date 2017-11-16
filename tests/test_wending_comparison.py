from datarum import wending
import unittest


class TestWendingComparison(unittest.TestCase):

    def test_unequal(self):
        w1 = wending(226, 3, 14)
        w2 = wending(234, 5, 23)

        self.assertTrue(w1 != w2)
        self.assertFalse(w1 == w2)

    def test_equal(self):
        w1 = wending(226, 3, 14)
        w2 = wending(226, 3, 14)

        self.assertTrue(w1 == w2)
        self.assertFalse(w1 != w2)

    def test_greater_than(self):
        w1 = wending(226, 3, 14)
        w2 = wending(213, 5, 23)

        self.assertTrue(w1 > w2)
        self.assertFalse(w1 < w2)

    def test_less_than(self):
        w1 = wending(226, 3, 14)
        w2 = wending(213, 5, 23)

        self.assertTrue(w2 < w1)
        self.assertFalse(w2 > w1)
