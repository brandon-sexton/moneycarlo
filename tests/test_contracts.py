import unittest

from src.moneycarlo.contracts import Contract


class TestContract(unittest.TestCase):
    def test_from_csv_line(self):
        ct = Contract.from_csv_line("2023,1,low,1000")
        self.assertEqual(ct.probability_of_win, 0.25)
        self.assertEqual(ct.value, 1000.0)
        self.assertEqual(ct.award_date.year, 2023)
        self.assertEqual(ct.award_date.month, 3)
        self.assertEqual(ct.award_date.day, 1)
