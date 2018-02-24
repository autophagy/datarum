from datarum import wending
import unittest

expected = [
    ((100, 1,  1,  0, 0, 0), 36160),
    ((175, 8,  23, 0, 0, 0), 63785),
    ((201, 4,  7,  0, 0, 0), 73145),
    ((226, 13, 2,  0, 0, 0), 82541),
    ((230, 10, 17, 0, 0, 0), 83927),
    ((300, 3,  3,  0, 0, 0), 109270),
]


class TestOrdinalFunctions(unittest.TestCase):

    def test_days_since_incept(self):
        for dat, days in expected:
            w = wending(*dat)
            self.assertEqual(w.toordinal(), days)

    def test_days_to_wending(self):
        for dat, days in expected:
            w = wending.fromordinal(days)
            self.assertEqual(w.tuple(), dat)
