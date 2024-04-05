import requests

class CountryData:
    def __init__(self, url):
        self.url = url
        self.data = None

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.data = response.json()
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

    def display_countries_currencies(self):
        if self.data:
            for country in self.data:
                name = country.get('name', {}).get('common')
                currencies = country.get('currencies', {})
                currency_names = [c.get('name') for c in currencies.values()]
                currency_symbols = [c.get('symbol') for c in currencies.values()]
                print(f"Country: {name}, Currencies: {currency_names}, Symbols: {currency_symbols}")

    def countries_with_currency(self, currency_name):
        currency_countries = []
        if self.data:
            for country in self.data:
                currencies = country.get('currencies', {})
                for currency_code, currency_info in currencies.items():
                    if currency_info.get('name') == currency_name:
                        currency_countries.append(country.get('name', {}).get('common'))
        return currency_countries

    def display_countries_with_dollar(self):
        dollar_countries = self.countries_with_currency("United States dollar")
        print("Countries with United States dollar as currency:")
        for country in dollar_countries:
            print(country)

    def display_countries_with_euro(self):
        euro_countries = self.countries_with_currency("Euro")
        print("Countries with Euro as currency:")
        for country in euro_countries:
            print(country)

# URL for fetching country data
url = "https://restcountries.com/v3.1/all"

# Create an instance of CountryData
country_data = CountryData(url)

# Fetch data from the URL
country_data.fetch_data()

# Display countries, currencies, and symbols
country_data.display_countries_currencies()

# Display countries with dollar as currency
country_data.display_countries_with_dollar()

# Display countries with EURO as currency
country_data.display_countries_with_euro()