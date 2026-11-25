
import requests


class CurrencyConverter:
    def __init__(self):
        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
        response = requests.get(url)
        data = response.json()

        for currency in data:
            if currency["cc"] == "USD":
                self.rate = currency["rate"]

    def convert(self, amount):
        return amount / self.rate


converter = CurrencyConverter()

amount = float(input("Введіть суму в гривнях: "))

print("Сума в доларах:", round(converter.convert(amount), 2))
