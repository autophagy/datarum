from datarum import wending
import unittest


class TestWendingStrftime(unittest.TestCase):

    wending_date = wending(226, 3, 14, 7, 20, 0)

    def test_strftime_all_elements(self):
        s = '{daeg} {month} {gere} // {tid}.{minute}.{second}'
        expected_string = '14 Forst 226 // 7.20.0'
        self.assertEqual(expected_string,  self.wending_date.strftime(s))

    def test_strftime_all_zeropadded_elements(self):
        s = '{daeg} {month} {gere} // {tid_zero}.{minute_zero}.{second_zero}'
        expected_string = '14 Forst 226 // 07.20.00'
        self.assertEqual(expected_string,  self.wending_date.strftime(s))

class TestWendingStrptime(unittest.TestCase):

    def test_strptime_only_date(self):
        s = '226 Regn 30'
        f = '{gere} {month} {daeg}'
        w = wending.strptime(s, f)
        self.assertEqual(s, w.strftime(f))

    def test_strptime_all_elements(self):
        s = '226 Regn 30 (23.54.12)'
        f = '{gere} {month} {daeg} ({tid}.{minute}.{second})'
        w = wending.strptime(s, f)
        self.assertEqual(s, w.strftime(f))

    def test_strptime_zero_padded(self):
        s = '226 Regn 30 (23.05.02)'
        f = '{gere} {month} {daeg} ({tid}.{minute_zero}.{second_zero})'
        w = wending.strptime(s, f)
        self.assertEqual(s, w.strftime(f))
