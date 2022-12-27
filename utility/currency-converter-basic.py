def bruh():
    list = ['USD', 'EUR', 'GBP', 'BTC', 'CAD']
    print(list)
    currency = input("Enter the currency you want to convert to INR: ")
    if currency == "USD":
        usd = int(input("> Enter USD ($): "))
        inr = usd * 82.85
        print(f"${usd} is ₹{inr} ")
    elif currency == "EUR":
        euro = int(input("Enter EURO (€): "))
        inr = euro * 88.33
        print(f"€{euro} is ₹{inr} ")
    elif currency == "GBP":
        gbp = int(input("Enter POUND STERLING (£): "))
        inr = gbp * 99.93
        print(f"£{gbp} is ₹{inr} ")
    elif currency == "BTC":
        btc = int(input("Enter BTC (₿): "))
        inr = btc * 1395644.23
        print(f"₿{btc} is ₹{inr} ")
    elif currency == "CAD":
        cad = int(input("Enter CAD ($): "))
        inr = cad * 61.23
        print(f"${cad} is ₹{inr} ")
    repeat = input("Would you like to run again? ")
    if repeat == "yes":
        bruh()
    else: 
        exit()
bruh()