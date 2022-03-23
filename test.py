import unittest
from bill_calculator import CurrencyConverter, Expenditure

class TestCurrencyConverter(unittest.TestCase):
    def test_currency_converter_CHA_to_TOK(self):
        converter = CurrencyConverter("fx_rates.csv")
        CHA_to_TOK_rate = 0.25
        self.assertEqual(converter.convert(1, "CHA", "TOK"), CHA_to_TOK_rate)
        self.assertEqual(converter.convert(100, "CHA", "TOK"), 100 * CHA_to_TOK_rate)

    def test_currency_converter_CHA_to_TAZ(self):
        converter = CurrencyConverter("fx_rates.csv")
        CHA_to_TAZ_rate = 0.5
        self.assertEqual(converter.convert(1, "CHA", "TAZ"), CHA_to_TAZ_rate)
        self.assertEqual(converter.convert(100, "CHA", "TAZ"), 100 * CHA_to_TAZ_rate)

    def test_currency_converter_TAZ_to_CHA(self):
        converter = CurrencyConverter("fx_rates.csv")
        TAZ_to_CHA_rate = 2
        self.assertEqual(converter.convert(1, "TAZ", "CHA"), TAZ_to_CHA_rate)
        self.assertEqual(converter.convert(100, "TAZ", "CHA"), 100 * TAZ_to_CHA_rate)

    def test_currency_converter_TAZ_to_TOK(self):
        converter = CurrencyConverter("fx_rates.csv")
        TAZ_to_TOK_rate = 0.5
        self.assertEqual(converter.convert(1, "TAZ", "TOK"), TAZ_to_TOK_rate)
        self.assertEqual(converter.convert(100, "TAZ", "TOK"), 100 * TAZ_to_TOK_rate)

    def test_currency_converter_TOK_to_TAZ(self):
        converter = CurrencyConverter("fx_rates.csv")
        TOK_to_TAZ_rate = 2
        self.assertEqual(converter.convert(1, "TOK", "TAZ"), TOK_to_TAZ_rate)
        self.assertEqual(converter.convert(100, "TOK", "TAZ"), 100 * TOK_to_TAZ_rate)

    def test_currency_converter_TOK_to_CHA(self):
        converter = CurrencyConverter("fx_rates.csv")
        TOK_to_CHA_rate = 4
        self.assertEqual(converter.convert(1, "TOK", "CHA"), TOK_to_CHA_rate)
        self.assertEqual(converter.convert(100, "TOK", "CHA"), 100 * TOK_to_CHA_rate)

    def test_unit_to_self_convertion(self):
        converter = CurrencyConverter("fx_rates.csv")
        self.assertEqual(converter.convert(1, "TOK", "TOK"), 1)
        self.assertEqual(converter.convert(1, "CHA", "CHA"), 1)
        self.assertEqual(converter.convert(1, "TAZ", "TAZ"), 1)

class TestExpenditure(unittest.TestCase):
    def test_expenditure_client_1_in_CHA(self):
        expenditure = Expenditure("platform_spend.csv", "fx_rates.csv")
        expenditure_in_CHA = 2500
        self.assertEqual(expenditure.get_expenditure(1, "CHA"), expenditure_in_CHA)

    def test_expenditure_client_1_in_TOK(self):
        expenditure = Expenditure("platform_spend.csv", "fx_rates.csv")
        expenditure_in_TOK = 625
        self.assertEqual(expenditure.get_expenditure(1, "TOK"), expenditure_in_TOK)

    def test_expenditure_client_2_in_TAZ(self):
        expenditure = Expenditure("platform_spend.csv", "fx_rates.csv")
        expenditure_in_TAZ = 300
        self.assertEqual(expenditure.get_expenditure(2, "TAZ"), expenditure_in_TAZ)
    
    def test_expenditure_client_2_in_TOK(self):
        expenditure = Expenditure("platform_spend.csv", "fx_rates.csv")
        expenditure_in_TOK = 150
        self.assertEqual(expenditure.get_expenditure(2, "TOK"), expenditure_in_TOK)

    def test_expenditure_client_3_in_TOK(self):
        expenditure = Expenditure("platform_spend.csv", "fx_rates.csv")
        expenditure_in_TOK = 15000
        self.assertEqual(expenditure.get_expenditure(3, "TOK"), expenditure_in_TOK)

    def test_expenditure_client_3_in_CHA(self):
        expenditure = Expenditure("platform_spend.csv", "fx_rates.csv")
        expenditure_in_CHA = 60000
        self.assertEqual(expenditure.get_expenditure(3, "CHA"), expenditure_in_CHA)


if __name__ == '__main__':
    unittest.main()
