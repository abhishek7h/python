import requests

from_currency = str(input(" ~ Enter the currency that you'd would like to convert to: ")).upper()

to_currency = str(input(" ~ Enter the currency that you'd like to convert to: ")).upper()

amount = float(input(f" ~ Enter the amount in {from_currency}: "))

respone = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")

print(f"{amount} {from_currency} is {respone.json()['rates'][to_currency]} {to_currency}")