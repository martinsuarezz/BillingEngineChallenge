import argparse
import pandas as pd

class CurrencyConverter:
    """Class used for currency conversion."""

    def __init__(self, currency_rates_file: str):
        self.rates = pd.read_csv(currency_rates_file, index_col="Origin Currency")

    def convert(self, amount: int, from_currency: str, to_currency: str) -> int:
        """Converts an amount from one currency to another.

            Parameters:
            amount: The amount to convert.
            from_currency: The currency to convert from.
            to_currency: The currency to convert to.

            Returns:
            The converted amount.
        """
        return amount * self.rates.loc[from_currency, to_currency]

class Expenditure:
    """Class used for calculating clients expenditure."""

    def __init__(self, expenditure_file: str, rates_file: str):
        self.expenditure = pd.read_csv(expenditure_file)
        self.currency_converter = CurrencyConverter(rates_file)

    def get_expenditure(self, client_id, bill_currency) -> int:
        """Gets the expenditure amount for a certain client in certain currency.

            Parameters:
            client_id: id of the client to calculate the expenditure for.
            bill_currency: currency to use,

            Returns:
            The expenditure amount in the defined currency,
        """
        filtered_expenditure = self.expenditure.loc[self.expenditure['Client ID'] == client_id]
        expenditure = 0
        for _, row in filtered_expenditure.iterrows():
            expenditure += self.currency_converter.convert(row['Advertising Cost'],
                                                        row['Currency'], bill_currency)
        return expenditure

class BillingEngine:
    """Class used for creating the billing report."""

    def __init__(self, clients_file: str, rates_file: str, expenditure_file: str):
        self.clients = pd.read_csv(clients_file)
        self.expenditure = Expenditure(expenditure_file, rates_file)

    def create_billing_report(self, output_file_name: str):
        """Creates the billing reports and saves it in a csv file.

            Parameters:
            output_file_name: name of the output file
        """
        report = self.clients.copy()
        report['Total Amount'] = report.apply(lambda row:
                    self.expenditure.get_expenditure(row['Client ID'], row['Bill Currency']),
                    axis=1)
        report['Total Amount'] = report['Total Amount'] * (1 + report['Service Rate'])
        report.drop(columns=['Service Rate'], inplace=True)
        report.to_csv(output_file_name, index=False)

def main():
    """Main function of the application."""
    parser = argparse.ArgumentParser(description='Billing calculator')
    parser.add_argument('-c', '--clients', type=str,
                    required=False, default='clients.csv',
                    help='csv containing the clients information')
    parser.add_argument('-f', '--fx-rates', type=str,
                    required=False, default='fx_rates.csv',
                    help='csv containing the exchange rates information')
    parser.add_argument('-p', '--platform-spend', type=str,
                    required=False, default='platform_spend.csv',
                    help='csv containing the platform spending information')
    parser.add_argument('-o', '--output', type=str,
                    required=False, default='output.csv',
                    help='Output name for the resulting csv file')
    args = parser.parse_args()

    billing_engine = BillingEngine(args.clients, args.fx_rates, args.platform_spend)
    billing_engine.create_billing_report(args.output)

main()
